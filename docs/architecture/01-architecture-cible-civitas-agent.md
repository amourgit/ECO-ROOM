# Architecture cible — CIVITAS Agent Runtime (LangGraph)

> Remplace intégralement `services/peer`. S'appuie sur l'état des lieux
> ([`00-etat-des-lieux.md`](./00-etat-des-lieux.md)), sur les deux notes d'architecture
> fournies (fusion Control Plane / Data Plane dans un état unifié LangGraph), et sur les
> précisions apportées : **suppression totale du `peer`**, **isolation stricte par room** (détaillée
> dans [`03-isolation-et-orchestration.md`](./03-isolation-et-orchestration.md)), et **couverture
> exhaustive des actions navigateur** (détaillée dans
> [`02-catalogue-outils-agent.md`](./02-catalogue-outils-agent.md)).

---

## 1. Principes directeurs

1. **Jitsi reste un moteur de conférence indépendant.** CIVITAS ne transforme jamais Jitsi en
   application CIVITAS ; il ne fait qu'y participer, comme n'importe quel participant (via le
   navigateur headless) et l'observer (via le webhook Prosody).
2. **Séparation physique stricte Control Plane / Data Plane, consolidation logique unique dans
   l'état de l'agent.** Les deux plans ne partagent jamais de transport ; ils convergent
   uniquement dans le `ConferenceAgentState` de chaque instance LangGraph (§5).
3. **`peer` disparaît en tant que concept.** Il n'existe plus de process qui "gère plusieurs
   rooms en interne" : chaque room a son propre **CIVITAS Agent**, processus isolé de bout en
   bout (état, contexte, mémoire, session de raisonnement, navigateur headless).
4. **LangGraph est le runtime de raisonnement**, pas un module optionnel greffé après coup :
   toute décision ("dois-je répondre ?", "avec quel outil ?", "sous quelle forme ?") passe par
   le graphe, plus jamais par une cascade de `if/elif` en dur.
5. **Rien n'est perdu de ce qui marche déjà** : `EventBus`, `SpeakerTracker`, `ContextStore`,
   `GeminiSession`, `CivitasBrowser`, le schéma Postgres `room_configs`/`room_history_entries`,
   les topics Kafka existants — tout est repris et réintégré comme modules internes du CIVITAS
   Agent (cf. doc 00 §9), pas réécrit from scratch.
6. **Le catalogue d'outils doit couvrir, de façon explicite, tout ce qu'un participant humain
   peut faire dans le navigateur Jitsi** — pas seulement kick/mute/chat comme aujourd'hui.
   Détail exhaustif : doc 02.
7. **Isolation totale par room** : si un CIVITAS Agent plante dans une room, aucune autre room
   n'est affectée — ni au niveau process, ni au niveau état/mémoire/contexte. Détail : doc 03.

---

## 2. Les 4 domaines

```
╔══════════════════════════════════════════════════════════════════════════════╗
║                              ÉCOSYSTÈME CIVITAS                              ║
╚══════════════════════════════════════════════════════════════════════════════╝

1. JITSI                     conférence temps réel (Prosody / Jicofo / JVB / Web)
                              — acté, non modifié, "boîte noire" à deux portes d'entrée

2. CIVITAS CONTROL PLANE     événements structurels + commandes de contrôle
                              — event-bridge, Kafka, CIVITAS Agent Orchestrator

3. CIVITAS AI AGENT RUNTIME  perception, état, mémoire, raisonnement, actions
                              — UN process CIVITAS Agent par room (LangGraph)

4. CIVITAS PLATFORM          données métier, IAM, APIs, RAG, observabilité
                              — room-config (conservé), Postgres, Redis, Qdrant (nouveau),
                                MinIO (nouveau), monitoring (conservé)
```

Ce découpage reprend exactement les 4 domaines proposés dans la note d'architecture d'origine ;
la seule adaptation est que "CIVITAS Control Plane" inclut ici explicitement le nouvel
**Orchestrateur** (évolution de `room-spawner`, doc 03), qui est le composant qui matérialise
concrètement la frontière entre "un flux Kafka partagé par toutes les rooms" et "un process
agent strictement dédié à une seule room".

---

## 3. Control Plane cible

### 3.1 Ce qui ne change pas

Le chemin `Prosody → mod_muc_webhook.lua → event-bridge → Kafka` est conservé **à l'identique**
(doc 00 §2.1, §3). Il reste la seule source d'événements *serveur* (création/destruction de
room, entrée/sortie MUC). Aucune modification du plugin Prosody n'est nécessaire ni proposée —
Jitsi est acté.

### 3.2 Ce qui change : le dernier maillon (fan-out vers l'agent isolé)

Aujourd'hui, `room-spawner` consomme Kafka et appelle un **unique** `peer-service` partagé
(`POST /peer/join`). Demain, l'**Orchestrateur** (doc 03) reste le seul consommateur Kafka
(`jitsi.room.events`, `jitsi.participant.events`), mais :

- Sur `muc-room-created` (+ vérification `room-config`) → **fait naître un nouveau process
  CIVITAS Agent dédié à cette room** (et seulement à elle), au lieu d'appeler un service
  partagé.
- Sur tout événement suivant pour ce `room_id` → **forward HTTP** vers l'ingress de contrôle de
  *ce* process précis (`POST http://civitas-agent-<room>:<port>/control/event`) — jamais vers
  les autres.
- Sur `muc-room-destroyed` (ou crash détecté) → **détruit** ce process précis et retire sa
  route.

```
JITSI ──(events)──► event-bridge ──► Kafka ──► CIVITAS Agent Orchestrator
                                                        │
                                     (spawn / route / health / teardown — PAR room_id)
                                                        │
                          ┌─────────────────────────────┼─────────────────────────────┐
                          ▼                              ▼                              ▼
                  CIVITAS Agent               CIVITAS Agent                  CIVITAS Agent
                  room = "salle-A"            room = "salle-B"               room = "salle-C"
                  (process isolé)             (process isolé)                (process isolé)
```

Cette évolution ne change ni les topics Kafka, ni leur schéma, ni le rôle métier de
l'orchestrateur (toujours "qui doit être actif où") — elle change uniquement **ce qu'il fait
naître** en bout de chaîne : un process isolé au lieu d'un appel à un service partagé. Détail
complet (mécanisme de spawn, registre de routage, santé, teardown) : doc 03.

### 3.3 Commandes CIVITAS → Jitsi (sens retour)

Comme aujourd'hui, il n'existe pas de canal "webhook retour" vers Prosody : toute commande vers
Jitsi (kick, mute, chat, sujet, verrouillage, enregistrement…) passe par le navigateur headless
de l'agent (porte n°2, doc 00 §2.2), exposée comme un catalogue d'outils LangGraph (doc 02). Le
Control Plane sert uniquement à **informer** l'agent de la structure de la réunion, jamais à
agir dessus.

---

## 4. Data Plane cible

### 4.1 Ce qui ne change pas dans le principe

Le canal reste le navigateur headless de **chaque** agent : tracks WebRTC entrants (audio des
participants) → pont Python (`AudioPipe`) → moteur de parole → PCM sortant → `replaceTrack()`.
Vision : capture d'écran ponctuelle → description. Ce sont les modules `perception/` et
`speech/` du CIVITAS Agent (§8), directement portés de `services/peer/app/audio`,
`services/peer/app/speaker`, `services/peer/app/gemini`.

### 4.2 Ce qui change : le point d'arrivée dans le raisonnement

Aujourd'hui, la décision "dois-je répondre, et comment" est câblée en dur dans
`PeerInstance._on_participant_speech`. Demain, le flux audio brut est toujours absorbé par le
moteur de parole (Gemini Live, doc 00 §4.1 — fusion VAD+ASR+TTS assumée et conservée), mais sa
sortie (transcription complète par tour, `turn_id` inclus) devient un **événement sémantique**
injecté dans le graphe LangGraph via le nœud `ingest_data_event` (§6), exactement comme un
événement de Control Plane entre par `ingest_control_event`. Le graphe décide *ensuite*, de
façon uniforme, qu'il s'agisse d'un événement structurel ou d'un événement de contenu.

```
DATA PLANE (par agent, isolé)                    CONTROL PLANE (par agent, isolé)
────────────────────────────────                  ────────────────────────────────
JVB → navigateur headless                          Orchestrateur (forward HTTP,
  → AudioPipe (PCM)                                  scoping room_id garanti)
  → GeminiSession (VAD+ASR+TTS fusionnés)                    │
  → transcript complet + turn_id                             │
              │                                               │
              ▼                                               ▼
       ingest_data_event                             ingest_control_event
              │                                               │
              └───────────────────┬───────────────────────────┘
                                   ▼
                         update_state (ConferenceAgentState, §5)
                                   ▼
                              route → reason → act
```

### 4.3 Vision — même traitement

`capture_frame()` + description Gemini devient un outil (`vision.describe_screen`, doc 02) que
le graphe peut décider d'appeler dans le nœud `act`, plutôt qu'un branchement conditionnel
`if "regarde" in text`. Le mot-clé reste un signal d'entrée possible (détecté par `route`), mais
ce n'est plus la seule voie : le raisonnement LLM peut aussi décider d'appeler cet outil de
lui-même si le contexte le justifie (ex: "l'agent a été chargé de vérifier une diapositive").

---

## 5. État unifié — `ConferenceAgentState`

Repris directement de la note d'architecture d'origine, adapté aux types déjà en usage dans le
dépôt (`SpeechEntry`, `ParticipantInfo`, `RoomConfig`) pour rester compatible avec l'existant.

```python
class ParticipantState(TypedDict):
    endpoint_id: str
    display_name: str
    role: str                    # "moderator" | "participant"
    is_muted: bool
    is_video_muted: bool
    raised_hand: bool
    audio_level: float
    joined_at: str                # ISO8601

class ConversationEntry(TypedDict):
    speaker_id: str | None
    speaker_name: str
    text: str
    entry_type: str               # "participant" | "agent" | "chat"
    turn_id: str | None
    timestamp: str

class MediaState(TypedDict):
    dominant_speaker_id: str | None
    dominant_speaker_name: str
    current_speaker_id: str | None
    current_speaker_name: str
    last_screen_description: str | None
    recording_active: bool

class ConferenceMeta(TypedDict):
    room_id: str                  # invariant du process — cf. doc 03 (une seule valeur possible)
    subject: str | None
    locked: bool
    lobby_enabled: bool
    av_moderation_enabled: bool
    started_at: str

class AgentAction(TypedDict):
    tool: str
    args: dict
    reason: str                   # justification produite par le nœud `reason`
    requested_at: str

class ConferenceAgentState(TypedDict):
    conference: ConferenceMeta
    participants: dict[str, ParticipantState]     # clé = endpoint_id
    conversation: list[ConversationEntry]         # fenêtre glissante, cf. §7
    media: MediaState
    current_topic: str | None
    agenda: list[str]
    pending_actions: list[AgentAction]
    response_mode: str             # "audio" | "text" | "none" — cf. response_policy conservé
    agent_status: str              # "starting" | "active" | "silent" | "stopping"
```

Invariant fondamental de la cible : **`conference.room_id` est fixé une fois pour toutes au
démarrage du process** (variable d'environnement `ROOM_ID`, doc 03 §2) et n'est jamais réassigné
— il n'existe donc, par construction, aucun chemin de code qui puisse faire lire ou écrire
l'état d'une autre room que la sienne. C'est la garantie d'isolation la plus forte du système :
elle est vraie même en cas de bug applicatif, car elle est structurelle (un process = un
`room_id`), pas seulement conventionnelle (un `WHERE room_id = ...` qu'on pourrait oublier).

---

## 6. Le graphe LangGraph — nœuds explicites

Chaque process CIVITAS Agent instancie **un seul graphe**, pour **une seule room**. Nœuds
(implémentés dans `app/graph/nodes/`, cf. §8 pour l'arborescence complète) :

| Nœud | Entrée | Rôle | Sortie |
|---|---|---|---|
| `ingest_control_event` | événement forwardé par l'Orchestrateur (participant joined/left, room created/destroyed) | normalise l'événement Control Plane brut | événement structurel typé |
| `ingest_data_event` | transcript Gemini Live (turn_id), description vision, événement `JITSI_EVENTS_JS` (mute, main levée, réaction, sondage, sujet, verrouillage…) | normalise l'événement Data Plane / navigateur | événement sémantique ou structurel fin typé |
| `update_state` | événement typé (des deux nœuds ci-dessus) | fusionne dans `ConferenceAgentState` (participants, conversation, media, conference) | état mis à jour |
| `route` | état mis à jour | décide si une réaction est nécessaire (reprend `response_policy` existant : mot-clé d'invocation, demande orale explicite, mode `silent`/`on_call`/`proactive`) | `respond` \| `ignore` \| `tool_only` |
| `reason` | état + contexte court + mémoire longue (§7) + RAG optionnel | appel LLM : construit la décision (parler, écrire, quel(s) outil(s), avec quels arguments) — remplace la cascade `if/elif` de `PeerInstance` | un ou plusieurs `AgentAction` + texte de réponse éventuel |
| `act` | `AgentAction[]` | exécute les outils via le registre (doc 02) avec vérification des permissions `room_config.permissions` + `tools_allowed` | résultats d'outils, effets Jitsi réels |
| `speak` | texte de réponse (si `response_mode == audio`) | pousse vers `GeminiSession`/AudioPipe/navigateur/JVB | audio diffusé |
| `persist` | état + actions + transcript | écrit sur Kafka (`room.transcriptions`, `room.agent.actions`) + déclenche le checkpoint LangGraph (§7) | — |

Boucle du graphe : `ingest_* → update_state → route → (reason → act → speak?) → persist →
retour à l'écoute`. Les watchers d'aujourd'hui (`_watch_connection`, `_watch_alone`,
600s → auto-stop) restent des tâches asyncio de fond, hors graphe (comme aujourd'hui) —
LangGraph orchestre le raisonnement réactif, pas la supervision de bas niveau du navigateur.

### 6.1 Mode `proactive` — enfin implémentable

Le commentaire du code actuel ("non implémenté dans la v3, prévu pour LangGraph") trouve ici sa
réponse : en mode `proactive`, le nœud `route` peut renvoyer `respond` même sans mention du nom
de l'agent, sur la base d'un jugement du nœud `reason` (ex: silence prolongé après une question
posée à la cantonade, ou détection d'un point d'agenda non traité) — chose impossible avec une
simple recherche de mot-clé.

---

## 7. Mémoire — trois niveaux, room_id partout, jamais de fuite inter-room

Reprend et complète le modèle à deux niveaux déjà en place (doc 00 §5.3) :

| Niveau | Portée | Support | Quand il est lu | Isolation |
|---|---|---|---|---|
| **1. State (chaud)** | ce qui est vrai *maintenant* | RAM du process (`ConferenceAgentState`) | à chaque nœud du graphe | garantie **structurelle** (§5) : un process = un `room_id` |
| **2. Memory (tiède)** | historique de la réunion en cours + réunions passées | Postgres `room_history_entries` (existant, **schéma inchangé**) via `room-config` | réhydratation au démarrage (`get_room_history`, conservé), réinjection à chaque (re)connexion du moteur de parole (`context_provider`, conservé) | garantie par requête (`WHERE room_id = :room_id`) — **déjà correcte aujourd'hui**, aucune modification requise |
| **3. Checkpoint LangGraph (froid, nouveau)** | état complet du graphe (curseur, `pending_actions`, pas seulement le texte) | Postgres, table dédiée `civitas_agent_checkpoints`, `thread_id = room_id` | reprise après crash/redémarrage du process d'**une seule** room | garantie par **construction** : le process ne connaît qu'un seul `thread_id` possible (le sien), il ne peut physiquement pas charger le checkpoint d'une autre room |
| **RAG (optionnel, nouveau)** | base de connaissances (documents, procédures) — **organisationnelle**, pas forcément liée à une seule room | Qdrant, collection scoping par `knowledge_base_id` (`extra_config` de `room_configs`) | appel explicite de l'outil `rag.query_knowledge_base` (doc 02), soumis à `permissions.can_use_rag` | scoping par `knowledge_base_id`, pas par `room_id` — une base de connaissances peut légitimement être partagée entre plusieurs rooms d'une même organisation ; ce n'est pas un état *agent*, c'est une donnée *plateforme* (domaine 4) |

Redis (nouveau, optionnel v1) : verrous et coordination éphémère à très courte durée de vie
(ex: éviter un double `act()` concurrent sur une même room lors d'un rattrapage Kafka), clés
namespacées `civitas:agent:<room_id>:*`. Absence de Redis = dégradation gracieuse (le process
reste mono-thread par room de toute façon, le risque de concurrence intra-room est donc déjà
faible) — non bloquant pour le MVP.

Le point important, répété volontairement car c'est l'exigence centrale de cette refonte : **à
aucun niveau de cette pile mémoire il n'existe de mécanisme qui puisse mélanger deux rooms** —
soit par construction (niveaux 1 et 3), soit par une clause de filtrage déjà présente et
inchangée depuis l'existant (niveau 2).

---

## 8. Architecture interne du CIVITAS Agent — arborescence modulaire

Nouveau service : `services/civitas-agent/` (remplace `services/peer/`). Un process = une
instance de cette arborescence = une room (`ROOM_ID` fourni à la création du process, doc 03).

```
services/civitas-agent/
├── Dockerfile
├── requirements.txt
├── .env.example
├── README.md
└── app/
    ├── main.py                    # FastAPI de contrôle — SCOPÉ À CETTE SEULE ROOM
    ├── config.py                  # Settings, dont ROOM_ID (obligatoire, immuable)
    ├── state.py                   # ConferenceAgentState + sous-types (§5)
    │
    ├── graph/                     # ── LE RUNTIME LANGGRAPH ──
    │   ├── build.py                # assemblage du StateGraph, nœuds + arêtes (§6)
    │   ├── checkpoint.py           # PostgresSaver, thread_id = ROOM_ID uniquement
    │   └── nodes/
    │       ├── ingest.py           # ingest_control_event, ingest_data_event
    │       ├── state_update.py     # update_state
    │       ├── routing.py          # route (reprend response_policy.py conservé)
    │       ├── reasoning.py        # reason (appel LLM texte, construit les AgentAction)
    │       ├── acting.py           # act (exécute via tools/registry.py)
    │       └── persistence.py      # persist (Kafka + checkpoint)
    │
    ├── perception/                 # ── DATA PLANE : capteurs ──
    │   ├── audio_pipe.py            # = services/peer/app/audio/pipe.py (conservé)
    │   ├── speaker_tracker.py       # = services/peer/app/speaker/tracker.py (conservé)
    │   └── vision.py                # capture_frame() + orchestration description
    │
    ├── speech/                     # ── DATA PLANE : moteur de parole ──
    │   ├── engine.py                 # interface/port abstraite (speak, listen, transcript)
    │   ├── gemini_live.py           # = services/peer/app/gemini/session.py (implémentation par défaut du port)
    │   └── response_policy.py       # = services/peer/app/peer/response_policy.py (conservé)
    │
    ├── browser/                    # ── PORTE D'ACTION/CAPTEUR VERS JITSI ──
    │   └── driver.py                 # = services/peer/app/browser/browser.py, étendu (doc 02)
    │
    ├── tools/                      # ── CATALOGUE D'OUTILS (doc 02, cœur de la modularité) ──
    │   ├── registry.py               # enregistrement + gating par permissions/tools_allowed
    │   ├── chat_tools.py
    │   ├── presence_tools.py
    │   ├── moderation_tools.py
    │   ├── room_tools.py
    │   ├── media_tools.py
    │   ├── vision_tools.py
    │   ├── platform_tools.py         # appels CIVITAS Platform (domaine 4 — get_user, create_task…)
    │   └── rag_tools.py
    │
    ├── context/
    │   └── store.py                  # = services/peer/app/context/store.py (conservé, niveau 1)
    │
    ├── memory/
    │   └── client.py                  # = services/peer/app/room/config_client.py, renommé/étendu (niveau 2)
    │
    ├── events/
    │   ├── bus.py                     # = services/peer/app/events/bus.py (conservé)
    │   └── handlers.py                # = services/peer/app/events/handlers.py (conservé, alimente ingest_data_event)
    │
    ├── kafka/
    │   ├── producer.py                # = services/peer/app/kafka/producer.py (conservé)
    │   └── control_ingress.py         # NOUVEAU — reçoit le forward HTTP de l'Orchestrateur (§3.2)
    │
    └── room/
        └── config_client.py           # = services/peer/app/room/config_client.py (conservé)
```

Chaque flèche "= chemin existant (conservé)" ci-dessus signifie : **le code est porté avec un
minimum de modifications** (renommage de package, adaptation à un `ROOM_ID` unique au lieu d'un
paramètre `room_id` parmi d'autres) — pas réécrit. C'est un principe volontaire : la richesse
fonctionnelle déjà validée en production (reconnexion Gemini, accumulation de transcription par
tour, prejoin bypass, RTC spy...) ne doit pas être perdue au passage à LangGraph.

### 8.1 `main.py` — un contrôle strictement local à la room

L'API HTTP exposée par chaque process n'a plus besoin de `{room_id}` dans ses routes (contrairement
à `peer-service` aujourd'hui, `POST /peer/{room_id}/kick`) puisqu'il n'existe qu'une seule room
possible pour ce process :

```
POST /control/event          # ingress Control Plane (forward Orchestrateur, §3.2)
POST /admin/send_text
POST /admin/send_chat
POST /admin/kick              {participant_id, reason}
POST /admin/mute              {participant_id}
GET  /admin/moderator_status
GET  /admin/state             # snapshot ConferenceAgentState — debug/observabilité
GET  /health
POST /shutdown                # arrêt propre demandé par l'Orchestrateur (doc 03 teardown)
```

C'est une simplification volontaire par rapport à `peer-service` (qui devait démultiplexer par
`room_id` dans chaque route puisqu'un seul process servait toutes les rooms) — une conséquence
directe et bienvenue de l'isolation par process.

---

## 9. Permissions — exploitation enfin réelle du schéma existant

`room_configs.permissions` (`can_speak`, `can_write_chat`, `can_use_tools`, `can_use_rag`,
`can_moderate`) et `tools_allowed` (liste JSON) existent déjà dans le schéma (doc 00 §6.1) mais
n'étaient reliés à aucun mécanisme réel puisque le `peer` actuel n'a que 5 actions fixes,
non nommées comme des "outils". La cible relie enfin ce schéma à `tools/registry.py` :

- Chaque outil du catalogue (doc 02) déclare la **capacité** dont il dépend
  (`can_moderate` pour kick/mute/lock, `can_speak` pour parler, `can_write_chat` pour écrire,
  `can_use_rag` pour interroger une base de connaissances).
- `tools_allowed`, si non vide, agit comme une **liste blanche explicite** par-dessus les
  capacités (permet de restreindre encore plus finement, ex: autoriser `can_moderate=true` mais
  `tools_allowed=["moderation.mute_participant"]` seulement, sans `kick_participant`).
- Le nœud `act` (§6) consulte le registre avant tout appel réel — un outil refusé produit un
  résultat structuré (`{"allowed": false, "reason": ...}`) réinjecté dans l'état, exactement sur
  le modèle déjà en place pour `kick_participant`/`mute_participant` aujourd'hui
  (`{"allowed": false, "ok": false, "error": ...}` dans `PeerInstance`, doc 00 §5.4) — ce
  pattern de double-niveau d'échec (refusé côté CIVITAS vs. échoué côté Jitsi) est **conservé
  et généralisé à tous les outils**, pas seulement kick/mute.

---

## 10. Interfaces (ports) pour rester remplaçable

Deux points de variabilité anticipés, matérialisés en interfaces Python (`Protocol`/ABC) plutôt
qu'en appels directs, sans changer le choix par défaut (Gemini Live) :

- **`speech/engine.py`** — port `SpeechEngine` (`start`, `stop`, `send_audio`, `send_text`,
  `send_image`, callbacks `on_transcription`/`on_speech`/`on_audio`). `gemini_live.py`
  l'implémente. Permettra plus tard un pipeline décomposé (VAD dédié + ASR dédié + TTS dédié)
  sans toucher au graphe LangGraph ni aux outils — **non fait dans cette phase**, juste rendu
  possible.
- **`tools/platform_tools.py`** — clients vers la CIVITAS Platform (domaine 4) définis par
  interface HTTP simple (`get_user`, `get_meeting`, `create_task`, `create_minutes`,
  `create_vote`…), pour que l'ajout de nouvelles APIs métier n'impacte jamais le graphe ni le
  reste du catalogue d'outils.

---

## 11. Suite du document

- **Catalogue exhaustif des outils** (mapping actions humaines → outils CIVITAS Agent, groundé
  sur l'API réelle `IJitsiConference`/`lib-jitsi-meet`) : [`02-catalogue-outils-agent.md`](./02-catalogue-outils-agent.md)
- **Isolation stricte par room, orchestrateur, déploiement** : [`03-isolation-et-orchestration.md`](./03-isolation-et-orchestration.md)
- **Plan de migration phasé, fichier par fichier** : [`04-plan-migration.md`](./04-plan-migration.md)
