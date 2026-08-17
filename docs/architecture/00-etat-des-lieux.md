# État des lieux — Architecture actuelle CIVITAS (avant remplacement du `peer`)

> Document produit par lecture exhaustive du dépôt `ECO-ROOM` (code, docker-compose,
> `.env.example`, modèles de données, CLI, plugin Prosody) au moment où la décision est prise
> de **supprimer complètement le service `peer`** et de le remplacer par le **CIVITAS Agent
> Runtime** (LangGraph). Ce document fige la référence "avant" ; le document
> [`01-architecture-cible-civitas-agent.md`](./01-architecture-cible-civitas-agent.md) décrit
> la cible.
>
> Périmètre : **Jitsi lui-même (Prosody/Jicofo/JVB/Web, conteneurisation, TLS, provisioning
> système) est considéré comme acté et stable** — il n'est décrit ici que comme un
> "boîtier noir" avec lequel CIVITAS interagit par deux portes d'entrée précises (webhook
> Prosody, et navigateur headless via `lib-jitsi-meet`). Aucune remise en cause de la couche
> Jitsi n'est proposée dans ce document ni dans la cible.

---

## 1. Vue d'ensemble — les 6 services CIVITAS existants

| # | Service | Répertoire | Container | Port | Rôle en une phrase |
|---|---------|-----------|-----------|------|---------------------|
| 1 | Kafka (+ UI + exporter) | `kafka/` | `civitas-kafka`, `civitas-kafka-ui`, `civitas-kafka-exporter` | 9092/9094, 8090, 9308 | Bus d'événements central, seul canal asynchrone du système |
| 2 | Event Bridge | `event-bridge/` | `civitas-event-bridge` | 8100 | Traduit les webhooks Prosody (XMPP/MUC) en événements Kafka |
| 3 | Room Config | `services/room-config/` | `civitas-room-config` | 8010 | Source de vérité de la config agent par room (Postgres) + mémoire de réunion persistante |
| 4 | Room Spawner | `services/room-spawner/` | `civitas-room-spawner` | 8011 | Orchestrateur : décide qui doit rejoindre/quitter quelle room, pilote le peer |
| 5 | **Peer Service** ⚠️ **à remplacer** | `services/peer/` | `civitas-peer` | 8002 | **Processus unique** hébergeant **tous** les agents IA actifs (1 `PeerInstance` par room, dans le même process Python) |
| 6 | Monitoring | `monitoring/` | Prometheus/Loki/Promtail/Grafana | 9091/3100/3000 | Observabilité transverse |

Complément : `cli/civitas` (script Python stdlib) pilote l'intégralité de ces API HTTP.
`services/room-spawner/app/peer_client.py` et `services/room-spawner/app/room_config_client.py`
sont les deux seuls clients HTTP internes utilisés par l'orchestrateur.

---

## 2. Le chemin d'entrée Jitsi → CIVITAS (aujourd'hui)

Il n'existe que **deux portes d'entrée réelles** entre Jitsi et CIVITAS. Tout le reste du
système est construit dessus.

### 2.1 Porte n°1 — Webhook Prosody (`mod_muc_webhook.lua`)

Fichier : `jitsi/prosody-plugins-custom/mod_muc_webhook.lua`. C'est un **module MUC** Prosody
(chargé via `XMPP_MUC_MODULES=muc_webhook`) qui hook exactement **4 événements** côté serveur
XMPP et les POST vers `event-bridge` (`http://civitas-event-bridge:8100/webhook`), avec un
header `X-Civitas-Webhook-Secret` (HMAC comparé à temps constant côté event-bridge) :

```
muc-room-created
muc-room-destroyed
muc-occupant-joined
muc-occupant-left
```

> **Point important pour la cible** : c'est la **totalité** du signal "control plane serveur"
> disponible aujourd'hui. `event-bridge/main.py` référence aussi `muc-message`,
> `occupant-affiliation-changed`, `occupant-role-changed` dans sa table de routage
> (`TOPIC_MAP`), mais ces 3 événements ne sont **pas** hookés par le plugin Prosody actuel —
> ils ne peuvent donc jamais arriver en pratique par cette voie. Toute logique CIVITAS qui a
> besoin de finesse (qui parle, qui lève la main, qui change de rôle, qui écrit dans le chat…)
> passe exclusivement par la **porte n°2**.

### 2.2 Porte n°2 — Navigateur headless (`lib-jitsi-meet`, via Playwright)

C'est le canal réellement riche. `services/peer/app/browser/browser.py` fait rejoindre à un
Chrome headless (Playwright) l'URL `https://meet.civitas.local/<room_id>` comme un
participant normal, puis injecte trois scripts JS dans la page :

- **`RTC_SPY_JS`** — intercepte `RTCPeerConnection.setLocalDescription` pour garantir le
  `replaceTrack()` de l'audio de synthèse (sortant) au bon moment après chaque renégociation SDP.
- **`AUDIO_BRIDGE_JS`** — pont audio bidirectionnel entre le DOM (tracks WebRTC réels) et
  Python (WebSocket local), cf. §5.
- **`JITSI_EVENTS_JS`** — s'abonne à **tous** les événements `JitsiMeetJS.events.conference`
  exposés par `window.APP.conference._room` et les remonte à Python via
  `page.expose_function("__civitasEvent", ...)`.

C'est donc `window.APP.conference._room` (l'objet `JitsiConference` interne de l'app React
Jitsi Meet) qui sert à la fois de **capteur** (tous les événements) et d'**actionneur** (kick,
mute, chat, lecture du rôle) pour CIVITAS aujourd'hui. Aucun appel ne passe par une API REST
Jitsi/Jicofo dédiée — tout transite par le DOM du participant headless, exactement comme le
ferait un humain dans son navigateur.

---

## 3. Control Plane actuel

```
Prosody (MUC)
   │  hook (4 événements seulement)
   ▼
mod_muc_webhook.lua
   │  HTTP POST + X-Civitas-Webhook-Secret
   ▼
event-bridge :8100  (process UNIQUE, état _room_state en RAM pour TOUTES les rooms)
   │  publie sur Kafka, enrichi d'un snapshot de présence
   ▼
Kafka
   ├── jitsi.room.events         (muc-room-created / muc-room-destroyed / fallback)
   ├── jitsi.participant.events  (muc-occupant-joined / muc-occupant-left / role/affiliation)
   ├── jitsi.chat.events         (référencé, jamais alimenté en pratique — cf. §2.1)
   └── room.presence             (snapshot de présence à chaque event participant)
   │  consumer group civitas-room-spawner (offset committé APRÈS traitement, at-least-once)
   ▼
room-spawner :8011  (process UNIQUE, état _active_rooms: set[str] en RAM pour TOUTES les rooms)
   │  vérifie room-config (peer_enabled), puis HTTP
   ▼
peer-service :8002  →  POST /peer/join {room_id}  /  POST /peer/leave/{room_id}
```

En parallèle, room-spawner expose des **endpoints modérateur manuels** (`/moderator/inject`,
`/eject`, `/standby`, `/activate`, `/kick`, `/mute`, `/status/{room_id}`) qui court-circuitent
Kafka pour un pilotage humain immédiat (CLI ou API directe) — mêmes effets finaux, appelés
directement plutôt que déclenchés par un événement Prosody.

### 3.1 Ce que le Control Plane transporte

Uniquement de la **structure** : une room est née/est morte, quelqu'un est entré/sorti au sens
XMPP MUC (JID, nick, rôle, affiliation). **Aucun contenu** (ni audio, ni texte de chat, ni
qui-parle-en-ce-moment) ne transite par ce chemin.

### 3.2 Ce que le Control Plane ne fait PAS aujourd'hui

- Pas de commande CIVITAS → Jitsi via ce canal (le sens `event-bridge → Prosody` n'existe pas :
  toutes les commandes vers Jitsi passent par le navigateur headless, porte n°2).
- Pas de granularité fine (mute/unmute, main levée, réaction, sondage, sujet, verrouillage…) —
  uniquement via `JITSI_EVENTS_JS` côté navigateur (porte n°2), jamais via le webhook Prosody.

---

## 4. Data Plane actuel

Le terme "Data Plane" recouvre ici deux flux bien distincts dans le code actuel, tous deux
portés par le navigateur headless (porte n°2) :

### 4.1 Audio temps réel (WebRTC ↔ Gemini Live)

```
Participant (micro)
   │ WebRTC / JVB
   ▼
Chrome headless — track distant capté via TRACK_ADDED (lib-jitsi-meet)
   │ Web Audio API → AudioWorklet PCMSender → Int16 16kHz
   ▼ WebSocket local (ws://127.0.0.1:<port_dynamique>)
AudioPipe (Python, services/peer/app/audio/pipe.py)
   │ on_audio_in(pcm)
   ▼
GeminiSession.send_audio(pcm)  →  Gemini Live (gemini-2.5-flash-native-audio-preview-12-2025)
   │ réponse audio (PCM 24kHz) + transcription entrante ET sortante (deltas accumulés par tour)
   ▼
AudioPipe.send_audio(pcm_24k) → WebSocket → Chrome
   │ AudioContext(24kHz) → MediaStreamDestination → RTCPeerConnection.replaceTrack()
   ▼
JVB → tous les participants entendent la réponse de CIVITAS
```

**Particularité architecturale majeure à retenir pour la cible** : il n'y a **pas** de VAD, ASR
et TTS séparés dans le système actuel. **Gemini Live fait tout en un seul flux bidirectionnel
duplex** (VAD implicite + transcription entrante + génération de réponse + transcription
sortante + synthèse vocale, dans une seule session "Live"). C'est un choix pragmatique déjà en
production, pas une étape intermédiaire non finalisée.

### 4.2 Vision (capture d'écran à la demande)

`CivitasBrowser.capture_frame()` fait un `page.screenshot()` JPEG, encodé en base64, envoyé à
Gemini (`GeminiSession.send_image`) avec un prompt de description. Déclenché uniquement sur
mot-clé ("regarde", "écran", "screenshot"…) détecté dans `PeerInstance._on_participant_speech`
ou `_on_chat_message`. Pas de flux vidéo continu, pas de flux vidéo sortant côté agent
(`config.startWithVideoMuted=true` — CIVITAS n'a jamais de caméra).

### 4.3 Ce que le Data Plane ne fait PAS aujourd'hui

- Pas de traitement vidéo continu (frame sampling, vision model en continu).
- Pas de sortie vidéo/écran de la part de l'agent (pas de partage d'écran agent, pas d'avatar
  vidéo).
- Le "Data Plane" au sens du document de référence (audio brut → VAD → ASR → événement
  sémantique) est **télescopé** : Gemini Live absorbe VAD+ASR+réponse+TTS en une boîte, ce qui
  est un choix assumé (latence minimale, un seul fournisseur), mais qui **couple fortement**
  "compréhension" et "génération de réponse audio" — il n'y a pas aujourd'hui de point d'arrêt
  propre entre "j'ai compris ce qui a été dit" et "je décide de répondre et comment", cette
  décision étant en réalité prise en Python *avant* l'envoi à Gemini (mots-clés d'invocation
  dans `_on_participant_speech`/`_on_chat_message`), pas par un raisonnement outillé.

---

## 5. Architecture interne du `peer` (le composant qui disparaît)

### 5.1 Le problème central : isolation par room absente

`services/peer/docker-compose.yml` ne déclare **qu'un seul service** `peer` → **un seul
container** `civitas-peer` → **un seul process Python** → **un seul `PeerManager` singleton**
(`app/peer/manager.py`) qui maintient un dictionnaire `_instances: dict[str, PeerInstance]`,
une entrée par room, **toutes exécutées comme des tâches `asyncio` dans le même event loop, le
même interpréteur Python, le même container Docker, la même limite `shm_size: 2gb` partagée**.

Conséquences concrètes :

- Un crash non rattrapé dans **une seule** `PeerInstance` (exception dans un handler
  `EventBus`, deadlock asyncio, fuite mémoire d'un Chrome headless Playwright, bug de la lib
  `google-genai` encore en preview…) peut faire tomber **tout le process** `civitas-peer`, donc
  **toutes les rooms actives simultanément**, quel que soit le nombre de réunions en cours.
- Même si l'exception reste contenue (le `try/except` de `EventBus.emit` protège déjà les
  *handlers*, et `PeerManager.create`/`destroy` sont individuellement `try/except`-és), toutes
  les instances se partagent : la même limite `shm_size` Chromium (donc le même risque de crash
  `/dev/shm` plein si une room a beaucoup de threads de rendu), le même quota de connexions
  sortantes vers l'API Gemini, le même garbage collector Python (un GC pause long dans une room
  chargée impacte la latence audio de toutes les autres), et la même surface de code partagée
  (un bug introduit pour une fonctionnalité d'une room peut planter le process entier, y
  compris pour des rooms qui n'utilisent pas cette fonctionnalité).
- Redémarrer le service pour une seule room en difficulté (ex: session Gemini bloquée) oblige
  aujourd'hui à redémarrer **tout le container**, donc à couper **tous les agents actifs**.

`event-bridge` (`_room_state: dict` en RAM, toutes rooms) et `room-spawner`
(`_active_rooms: set[str]`, toutes rooms) ont la même forme "un seul process pour toutes les
rooms", mais c'est **beaucoup moins grave** dans leur cas : ils ne portent aucun raisonnement,
aucune session IA, aucun navigateur headless — juste du routage d'événements et un peu d'état
éphémère reconstructible (présence) ou rejouable (offsets Kafka non committés en cas d'échec).
Un crash y est un incident bref et sans perte de données, pas une coupure de service pour
toutes les réunions en cours. **C'est bien le `peer` qui concentre tout le risque
d'isolation**, et c'est bien lui que la cible doit corriger en premier.

### 5.2 Composition d'une `PeerInstance` (ce qui doit être préservé/porté, pas réinventé)

```
PeerInstance(room_id)
├── ContextStore         — historique en RAM (50+ dernières entrées), source rapide du contexte Gemini
├── SpeakerTracker       — fusion DOMINANT_SPEAKER_CHANGED (signal JVB certifié) + AUDIO_LEVEL (complément)
├── EventBus             — pub/sub interne, déjà pensé "LangGraph-ready" dans les commentaires du code
│   ├── handler: speaker    → met à jour SpeakerTracker
│   ├── handler: log        → log structuré
│   ├── handler: kafka      → republie une partie des événements Jitsi sur Kafka
│   └── handler: moderation → réactions automatiques (parle muté, main levée)
├── AudioPipe            — pont WebSocket local Python ↔ navigateur (PCM)
├── GeminiSession         — session Gemini Live avec boucle de reconnexion, heartbeat, accumulation
│                           des transcriptions par tour (turn_id), réinjection de mémoire à chaque
│                           (re)connexion (`context_provider`, lecture RAM pure, jamais réseau)
└── CivitasBrowser        — Chrome headless Playwright (capteur + actionneur, cf. §2.2)
```

Ce module est déjà commenté "Architecture modulaire LangGraph-ready" et "Pour ajouter une
fonctionnalité LangGraph, il suffit d'implémenter un handler" — **la cible ne part donc pas de
zéro** : elle formalise une intention déjà présente dans le code, elle ne l'invente pas.

### 5.3 Résilience mémoire — modèle à deux niveaux (à conserver tel quel)

1. **Coupure Gemini / reconnexion** (cas fréquent) → réinjection instantanée depuis
   `ContextStore` en RAM, aucune I/O réseau.
2. **Crash/redémarrage complet du process peer** → réhydratation depuis Postgres via
   `room-config` (`GET /rooms/{room_id}/history`) au prochain `start()`.

C'est un bon modèle — la cible lui ajoute un **troisième niveau** (checkpoint LangGraph, cf.
doc 01 §7) sans rien retirer aux deux premiers.

### 5.4 Actions actuellement exposées par `CivitasBrowser` (le carnet d'actions "navigateur")

| Méthode Python | Effet Jitsi réel | Pré-requis |
|---|---|---|
| `send_chat(text)` | `SEND_MESSAGE` (Redux `window.APP.store.dispatch`) | — |
| `kick_participant(id, reason)` | `JitsiConference.kickParticipant(id, reason)` | rôle `moderator` du peer dans la room |
| `mute_participant(id)` | `JitsiConference.muteParticipant(id, 'audio')` | rôle `moderator` — **ne peut jamais réactiver** (restriction Jitsi standard) |
| `get_moderator_status()` | lecture `JitsiParticipant.getRole()` du peer lui-même | — |
| `capture_frame()` | `page.screenshot()` JPEG | — |

C'est un sous-ensemble **très réduit** de ce qu'un participant humain peut faire dans
l'interface Jitsi Meet. Le document
[`02-catalogue-outils-agent.md`](./02-catalogue-outils-agent.md) dresse la liste exhaustive des
actions humaines disponibles (grantModerator, lock/unlock, sujet, enregistrement, réactions,
sondages, lobby, modération AV, lever/baisser la main, etc.) et leur statut vis-à-vis du
`CivitasBrowser` actuel — c'est le principal chantier fonctionnel de la cible, au-delà du
simple remplacement `peer` → `CIVITAS Agent`.

### 5.5 Événements actuellement capturés (`JITSI_EVENTS_JS`)

`USER_JOINED`, `USER_LEFT`, `USER_ROLE_CHANGED`, `DISPLAY_NAME_CHANGED`,
`DOMINANT_SPEAKER_CHANGED`, `TALK_WHILE_MUTED`, `NOISY_MIC`, `TRACK_MUTE_CHANGED`,
`MESSAGE_RECEIVED`, `PRIVATE_MESSAGE_RECEIVED`, `REACTION_RECEIVED`,
`PARTICIPANT_PROPERTY_CHANGED` (dont `raisedHand`), `POLL_RECEIVED`, `POLL_ANSWER_RECEIVED`,
`SUBJECT_CHANGED`, `LOCK_STATE_CHANGED`, `KICKED`, `PARTICIPANT_KICKED`,
`PARTICIPANTS_SNAPSHOT`, `AUDIO_LEVEL`. C'est une bonne couverture côté **capteur** — la cible
la conserve intégralement (cf. doc 01 §5).

### 5.6 Logique de décision actuelle (à remplacer par le graphe LangGraph)

Aujourd'hui, "faut-il répondre, et comment" est une suite de conditions `if` codées en dur dans
`PeerInstance._on_participant_speech` / `_on_chat_message`, plus la fonction pure
`response_policy.decide_chat_response_mode`. C'est **fonctionnellement correct et déjà bien
isolé** (fonction pure testable), mais ce n'est **pas un raisonnement outillé** : pas de
planification, pas d'appel d'outils arbitraires, pas de mémoire long terme consultée avant de
répondre, pas de RAG. C'est exactement le trou que LangGraph doit combler (doc 01 §6-§8).

---

## 6. Modèle de données actuel (Room Config Service)

### 6.1 Table `room_configs` (config agent par room — **conservée telle quelle dans la cible**)

`room_id` (PK) · `agent_name` · `system_prompt` · `behavior_mode`
(`on_call`/`proactive`/`silent`) · `language` · `can_speak` · `can_write_chat` ·
`can_use_tools` · `can_use_rag` · `can_moderate` · `peer_enabled` · `invocation_keywords`
(JSON) · `tools_allowed` (JSON) · `extra_config` (JSON) · `is_active` · `status`
(`pending`/`confirmed`) · `source` · `jitsi_confirmed_at` · `created_at` · `updated_at`.

> `can_use_tools=false` par défaut et `tools_allowed=[]` par défaut aujourd'hui : la
> permission structurelle pour un catalogue d'outils existe déjà dans le schéma, elle n'a
> simplement jamais été exploitée puisque le peer actuel n'a pas de notion d'"outil" — c'est un
> point d'ancrage direct pour la cible (doc 01 §9, doc 02).

### 6.2 Table `room_history_entries` (mémoire de réunion durable — **conservée telle quelle**)

`id` · `room_id` (indexé avec `occurred_at`) · `speaker_id` · `speaker_name` · `entry_type`
(`participant`/`agent`/`chat`) · `text` · `extra` (JSON libre, notamment `turn_id`) ·
`occurred_at` · `created_at`. Alimentée par un consumer Kafka embarqué dans room-config
(`room.transcriptions`, offset committé uniquement après écriture DB — at-least-once).

### 6.3 `behavior_mode` — sémantique actuelle

| Mode | Comportement actuel |
|---|---|
| `on_call` (défaut) | écoute tout, ne répond que si son nom est mentionné |
| `proactive` | identique à `on_call` **"non implémenté dans la v3, prévu pour LangGraph"** (commentaire du code lui-même) |
| `silent` | présent, n'intervient jamais, mais continue d'écouter/logguer |

---

## 7. Kafka — topics actuels

| Topic | Producteur(s) | Consommateur(s) | Contenu |
|---|---|---|---|
| `jitsi.room.events` | event-bridge, peer | room-spawner | création/destruction de room + fallback |
| `jitsi.participant.events` | event-bridge, peer | room-spawner | entrée/sortie, rôle, mute, main levée, réaction, kick |
| `jitsi.chat.events` | event-bridge (référencé, non alimenté) | — | — |
| `room.presence` | event-bridge | — | snapshot de présence temps réel |
| `room.transcriptions` | peer | room-config (consumer embarqué) | transcriptions participant/agent/chat |
| `room.agent.actions` | peer | — | actions de l'agent (vision, kick, mute…) |

Rétention 7 jours, 1 broker KRaft (pas de réplication — SPOF infra assumé, hors périmètre de
ce document).

---

## 8. CLI (`cli/civitas`)

Zéro dépendance (stdlib), couvre `room` (reserve/create/get/list/update/delete/context/history),
`peer` (inject/eject/standby/activate/active/instances/status/kick/mute/send-text/send-chat),
`webhook` (simulateurs + lecture d'état event-bridge), `kafka` (topics/consume via
`docker exec`), `health`, `config`. C'est un client HTTP pur — **aucune logique métier** n'y
vit. Il devra être étendu pour piloter le nouveau CIVITAS Agent (doc 04 §migration CLI), mais
sa structure (résolution de config à 4 niveaux, sous-commandes argparse) reste valable telle
quelle.

---

## 9. Synthèse — ce que la cible doit strictement préserver vs. strictement remplacer

| Élément | Décision |
|---|---|
| Jitsi (Prosody/Jicofo/JVB/Web), TLS, provisioning système | **Inchangé** — hors périmètre |
| Webhook Prosody → event-bridge → Kafka (control plane structurel) | **Conservé**, devient la source du Control Plane du CIVITAS Agent |
| `lib-jitsi-meet` via navigateur headless (capteur + actionneur) | **Conservé et étendu** — reste le seul canal riche vers Jitsi, cf. doc 02 |
| Gemini Live comme moteur audio (VAD+ASR+TTS fusionnés) | **Conservé** comme "moteur de parole" par défaut, mais isolé derrière une interface (port) pour rester remplaçable |
| `ContextStore` (RAM) + réhydratation Postgres (room-config) | **Conservé**, complété par un 3ᵉ niveau (checkpoint LangGraph) |
| `room_configs` / `room_history_entries` (schéma Postgres) | **Conservé tel quel** |
| `EventBus` + handlers | **Conservé**, devient la couche de normalisation en amont du graphe LangGraph |
| `PeerManager` (singleton multi-room dans un seul process) | **Supprimé** — remplacé par un process/container **par room**, supervisé par un orchestrateur (doc 03) |
| `PeerInstance` (logique de décision if/else) | **Supprimé** — remplacé par le graphe LangGraph (`CIVITAS Agent Runtime`, doc 01) |
| `CivitasBrowser` (5 actions exposées) | **Conservé comme socle**, étendu à un catalogue d'outils quasi-exhaustif (doc 02) |
| Room Spawner (orchestration mono-process) | **Fait évoluer** vers l'orchestrateur multi-process (doc 03) — même rôle, autre mécanique interne |
| CLI | **Étendu**, structure conservée |

Le document suivant ([`01-architecture-cible-civitas-agent.md`](./01-architecture-cible-civitas-agent.md))
détaille la cible point par point.
