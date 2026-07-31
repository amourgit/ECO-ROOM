# ECO-ROOM / CIVITAS — Documentation Technique Complète

> **Plateforme de réunion intelligente avec agent IA intégré**  
> Stack : Jitsi Meet · Kafka · Gemini Live · Playwright · FastAPI · PostgreSQL · Grafana

---

## Table des matières

1. [Vue d'ensemble du projet](#1-vue-densemble-du-projet)
2. [Architecture globale](#2-architecture-globale)
3. [Services & composants détaillés](#3-services--composants-détaillés)
   - 3.1 [Kafka — Bus de messages](#31-kafka--bus-de-messages)
   - 3.2 [Event Bridge](#32-event-bridge--civitas-jitsi-event-bridge-v2)
   - 3.3 [Room Config Service](#33-room-config-service)
   - 3.4 [Room Spawner](#34-room-spawner)
   - 3.5 [Peer Service](#35-peer-service--civitas-peer-v3)
   - 3.6 [Monitoring Stack](#36-monitoring-stack)
4. [Flux de données complets](#4-flux-de-données-complets)
5. [Topologie réseau & ports](#5-topologie-réseau--ports)
6. [Configuration globale](#6-configuration-globale)
7. [Certificats TLS](#7-certificats-tls)
8. [Scripts de démarrage/arrêt](#8-scripts-de-démarragestop)
9. [Kafka Topics](#9-kafka-topics)
10. [Modèle de données Room Config](#10-modèle-de-données-room-config)
11. [Modes de comportement de l'agent](#11-modes-de-comportement-de-lagent)
12. [Architecture interne du Peer (détail profond)](#12-architecture-interne-du-peer-détail-profond)

---

## 1. Vue d'ensemble du projet

**ECO-ROOM** (nom de code dépôt) est la couche infrastructure et logique de la plateforme **CIVITAS**, un système qui injecte un agent IA nommé **CIVITAS** dans des salles de réunion **Jitsi Meet**. L'agent peut :

- **Écouter** tous les participants en temps réel via l'API audio WebRTC de Jitsi
- **Transcrire** les paroles via **Google Gemini Live** (`gemini-2.5-flash-native-audio-preview`)
- **Répondre vocalement** (audio bidirectionnel en temps réel via Gemini Live)
- **Répondre par chat** (texte dans le chat Jitsi)
- **Voir la réunion** (capture d'écran via Playwright + analyse vision Gemini)
- **Identifier le locuteur** (dominant speaker JVB + niveaux audio)
- **Modérer** (signaler les mains levées, parler muté, etc.)
- **Publier des événements Kafka** (transcriptions, événements room, actions agent)

Le système est conçu pour un déploiement sur un serveur Linux local (IP `192.168.1.89`), avec des certificats TLS auto-signés pour le domaine `civitas.local`.

---

## 2. Architecture globale

```
┌─────────────────────────────────────────────────────────────────────────┐
│                          RÉSEAU civitas-net (Docker)                     │
│                                                                           │
│  ┌──────────────┐     webhooks      ┌─────────────────┐                 │
│  │  Jitsi Meet  │ ─────────────────▶│  Event Bridge   │                 │
│  │  (Prosody    │                   │  :8100          │                 │
│  │   XMPP MUC) │◀──── Browser ─────│                 │                 │
│  └──────┬───────┘   (Playwright)    └────────┬────────┘                 │
│         │                                    │ publish                   │
│         │ WebRTC/JVB                         ▼                           │
│         │                          ┌─────────────────┐                  │
│         │                          │     KAFKA        │                  │
│         │                          │  :9092 / :9094  │                  │
│         │                          └────────┬────────┘                  │
│         │                                   │ consume                    │
│         │                          ┌────────▼────────┐                  │
│         │                          │  Room Spawner   │                  │
│         │                          │  :8011          │                  │
│         │                          └────────┬────────┘                  │
│         │                                   │ HTTP POST /peer/join       │
│         │                          ┌────────▼────────┐                  │
│         │                          │  Room Config    │                  │
│         │                          │  :8010 + PG     │                  │
│         │                          └────────┬────────┘                  │
│         │                                   │ contexte agent             │
│         │                          ┌────────▼────────┐                  │
│         │◀────── Chrome headless ──│  Peer Service   │                  │
│         │        Playwright        │  :8002          │                  │
│         │        Audio WS          │                 │◀──▶ Gemini Live  │
│         │                          └─────────────────┘    (Google API)  │
│                                                                           │
│  ┌────────────────────────────────────────────────────────┐              │
│  │  MONITORING                                             │              │
│  │  Prometheus :9091 · Loki :3100 · Grafana :3000         │              │
│  │  Promtail (scrape logs Jitsi + Nginx + TURN)           │              │
│  └────────────────────────────────────────────────────────┘              │
└─────────────────────────────────────────────────────────────────────────┘
```

---

## 3. Services & composants détaillés

### 3.1 Kafka — Bus de messages

**Image :** `confluentinc/cp-kafka:7.6.0`  
**Mode :** KRaft (sans Zookeeper) — broker + controller en un seul nœud  
**Container :** `civitas-kafka`

#### Listeners

| Listener | Adresse | Usage |
|----------|---------|-------|
| `PLAINTEXT` | `0.0.0.0:9092` | Accès externe (IP hôte `192.168.1.89:9092`) |
| `CONTROLLER` | `0.0.0.0:9093` | Coordination KRaft interne |
| `INTERNAL` | `0.0.0.0:9094` | Communication inter-containers Docker (`civitas-kafka:9094`) |

> **Règle stricte :** tout ce qui tourne dans le réseau Docker `civitas-net`
> (event-bridge, peer, room-spawner, kafka-ui, kafka-exporter, healthcheck du
> broker lui-même) utilise **exclusivement** `civitas-kafka:9094` (`INTERNAL`).
> Le listener `PLAINTEXT` (`192.168.1.89:9092`) est réservé aux clients
> **hors** réseau Docker (poste de dev, outil externe). Ne jamais utiliser
> `localhost:9092` dans un `docker exec` ou un healthcheck : le broker
> annonce `192.168.1.89:9092` pour ce listener, et le client retente sa
> connexion sur cette adresse après le premier contact — ce qui échoue ou
> bloque selon la configuration réseau de l'hôte (hairpin NAT non garanti).

#### Configuration notable

- `KAFKA_AUTO_CREATE_TOPICS_ENABLE: true` — les topics sont créés à la première publication
- `KAFKA_LOG_RETENTION_HOURS: 168` — rétention 7 jours
- `KAFKA_LOG_SEGMENT_BYTES: 1073741824` — segments de 1 Go
- `CLUSTER_ID: RBoUQecvQs2gGtNZLOp3Zw`

#### Kafka UI

**Image :** `provectuslabs/kafka-ui:latest`  
**Container :** `civitas-kafka-ui`  
**Port :** `8090`  
**Auth :** login `civitas` / mot de passe `civitas2024`  
**Connexion interne :** `civitas-kafka:9094`

#### Kafka Exporter (métriques Prometheus)

**Image :** `danielqsj/kafka-exporter:latest`  
**Container :** `civitas-kafka-exporter`  
**Port :** `9308`  
**Connexion interne :** `civitas-kafka:9094`

> Ajouté car le port `9092`/`9094` sert uniquement le protocole Kafka natif —
> il n'a jamais exposé de métriques Prometheus, rendant le job `kafka`
> silencieusement inopérant. Prometheus scrape désormais
> `civitas-kafka-exporter:9308`.

---

### 3.2 Event Bridge — CIVITAS Jitsi Event Bridge v2

**Rôle :** Recevoir les webhooks **Prosody** (serveur XMPP de Jitsi) et les republier sur Kafka avec enrichissement.

**Container :** `civitas-event-bridge`  
**Port :** `8100`  
**Image :** Python 3.12-slim, FastAPI + uvicorn + aiokafka  
**Connexion Kafka :** `civitas-kafka:9094`

#### Routing des événements → Topics Kafka

| Événement Prosody | Topic Kafka |
|-------------------|-------------|
| `muc-room-created` | `jitsi.room.events` |
| `muc-room-destroyed` | `jitsi.room.events` |
| `muc-occupant-joined` | `jitsi.participant.events` |
| `muc-occupant-left` | `jitsi.participant.events` |
| `muc-message` | `jitsi.chat.events` |
| `occupant-affiliation-changed` | `jitsi.participant.events` |
| `occupant-role-changed` | `jitsi.participant.events` |
| Tout autre événement | `jitsi.room.events` (fallback) |

#### État local en mémoire

L'Event Bridge maintient un dictionnaire `_room_state` avec la présence en temps réel de tous les participants par room. À chaque événement de présence (join/left/role-change), il publie aussi un snapshot sur le topic `room.presence`.

#### Payload enrichi publié sur Kafka

```json
{
  "event_type": "muc-occupant-joined",
  "room_id": "ma-salle",
  "timestamp": "2024-01-15T10:30:00",
  "source": "prosody",
  "data": { /* body webhook brut */ },
  "presence": {
    "participant_count": 3,
    "participants": [
      {
        "jid": "user@meet.civitas.local/resource",
        "nick": "Jean Dupont",
        "role": "moderator",
        "affiliation": "owner",
        "joined_at": "2024-01-15T10:25:00"
      }
    ]
  },
  "occupant": {
    "jid": "user@meet.civitas.local/resource",
    "nick": "Jean Dupont",
    "role": "moderator",
    "affiliation": "owner"
  }
}
```

#### Snapshot de présence publié sur `room.presence`

```json
{
  "event_type": "presence.snapshot",
  "room_id": "ma-salle",
  "source": "jitsi-event-bridge",
  "timestamp": "2024-01-15T10:30:00",
  "participant_count": 3,
  "participants": [ /* liste des occupants */ ]
}
```

---

### 3.3 Room Config Service

**Rôle :** Gérer la configuration de l'agent IA par room. C'est la source de vérité pour savoir comment l'agent doit se comporter dans chaque salle.

**Container :** `civitas-room-config`  
**Port :** `8010`  
**Base de données :** PostgreSQL 16 (`civitas-postgres`, base `room_config`, user `civitas`, password `civitas2024`)  
**Auth API :** Bearer token `civitas-room-config-token`  
**Framework :** FastAPI + SQLAlchemy 2.0 + Alembic + aiokafka (consumer d'historique)

#### Modèle de données — Table `room_configs`

| Colonne | Type | Défaut | Description |
|---------|------|--------|-------------|
| `room_id` | String(255) PK | — | Identifiant de la room Jitsi |
| `agent_name` | String(100) | `"CIVITAS"` | Nom d'affichage de l'agent |
| `system_prompt` | Text | (généré) | Prompt système Gemini |
| `behavior_mode` | String(50) | `"on_call"` | `on_call` / `proactive` / `silent` |
| `language` | String(10) | `"fr"` | Langue de réponse |
| `can_speak` | Boolean | `true` | L'agent peut répondre en audio |
| `can_write_chat` | Boolean | `true` | L'agent peut écrire dans le chat |
| `can_use_tools` | Boolean | `false` | Accès aux outils externes |
| `can_use_rag` | Boolean | `false` | Accès à une base de connaissances |
| `can_moderate` | Boolean | `false` | Peut modérer (muter des participants) |
| `invocation_keywords` | JSON (list) | `["civitas"]` | Mots-clés pour interpeller l'agent |
| `tools_allowed` | JSON (list) | `[]` | Outils autorisés |
| `extra_config` | JSON (dict) | `{}` | Configuration additionnelle libre |
| `is_active` | Boolean | `true` | Config active |
| `created_at` | DateTime | now | |
| `updated_at` | DateTime | now+onupdate | |

#### Prompts par défaut

Trois templates de prompts sont définis :

- **DEFAULT_SYSTEM_PROMPT** (`on_call`) : agent silencieux sauf si son nom est mentionné, répond de façon concise
- **MODERATOR_PROMPT** : agent actif, surveille et intervient, peut muter des participants
- **ASSISTANT_PROMPT** : assistant technique avec accès aux outils DevOps

#### Comportement auto-création

Si une room n'a pas de config, le service en crée une automatiquement avec le prompt par défaut dès que quelqu'un appelle `GET /rooms/{room_id}/context`. C'est le comportement utilisé par le Peer au démarrage.

#### Historique de réunion persistant — Table `room_history_entries`

**Rôle :** mémoire durable et complète de la réunion (paroles participants transcrites, paroles de l'agent, messages chat), découplée du cycle de vie du service `peer`. C'est la source de vérité : un crash/redémarrage du peer, ou une simple reconnexion Gemini, ne fait jamais perdre cette mémoire.

| Colonne | Type | Description |
|---------|------|-------------|
| `id` | BigInteger PK | Auto-incrémenté |
| `room_id` | String(255), indexé | Identifiant de la room |
| `speaker_id` | String(255), nullable | `endpoint_id` Jitsi ou `civitas-peer` |
| `speaker_name` | String(255) | Nom affiché |
| `entry_type` | String(32) | `participant` / `agent` / `chat` |
| `text` | Text | Contenu (transcrit ou écrit) |
| `extra` | JSON, nullable | Champ libre (ex: `room_snapshot`) |
| `occurred_at` | DateTime, indexé avec `room_id` | Horodatage de l'interaction |

**Alimentation :** un consumer Kafka embarqué (`app/kafka/consumer.py`, groupe `civitas-room-history`) écoute en continu le topic `room.transcriptions` (déjà publié par `peer`, cf. 3.5) et persiste chaque message. Reconnexion infinie avec backoff, `enable_auto_commit=False` — l'offset n'est commité qu'après écriture DB réussie (sémantique *at-least-once* : un doublon rarissime est possible en cas de crash exact entre écriture et commit, la perte de données non).

**Lecture :** `GET /rooms/{room_id}/history?limit=200` — retourne les entrées brutes **et** un `formatted_context` prêt à injecter tel quel. Utilisé par `peer` pour se réhydrater à chaque join (cf. 3.5).

---

### 3.4 Room Spawner

**Rôle :** Orchestrer le cycle de vie des Peers en réaction aux événements Kafka. Il consomme `jitsi.room.events` et `jitsi.participant.events`, et crée/détruit des instances Peer en conséquence.

**Container :** `civitas-room-spawner`  
**Port :** `8011`  
**Auth API :** Bearer token `civitas-peer-token`  
**Kafka consumer group :** `civitas-room-spawner`  
**Topics consommés :** `jitsi.room.events`, `jitsi.participant.events`

#### Flux automatique (AUTO_JOIN / AUTO_LEAVE)

1. **Prosody** détecte qu'une room MUC a été créée
2. **Event Bridge** reçoit le webhook `muc-room-created` et publie sur `jitsi.room.events`
3. **Room Spawner** consomme l'événement `muc-room-created`
4. Si `AUTO_JOIN=true`, il vérifie avec **Room Config** si le peer est activé pour cette room
5. Si oui, il appelle `POST /peer/join` sur le **Peer Service**
6. Quand la room est détruite (`muc-room-destroyed`), il appelle `POST /peer/leave/{room_id}`

#### Contrôle manuel par modérateur

| Endpoint | Action |
|----------|--------|
| `POST /moderator/inject` | Forcer l'entrée du peer dans une room |
| `POST /moderator/eject` | Expulser le peer d'une room |
| `POST /moderator/standby` | Mettre le peer en mode `silent` (présent mais muet) |
| `POST /moderator/activate` | Réactiver le peer depuis `silent` vers `on_call` |

#### Variables de configuration

| Variable | Défaut | Description |
|----------|--------|-------------|
| `KAFKA_BOOTSTRAP` | `civitas-kafka:9094` | Bootstrap Kafka (listener `INTERNAL` — jamais l'IP hôte) |
| `PEER_SERVICE_URL` | `http://civitas-peer:8002` | URL du Peer Service |
| `ROOM_CONFIG_URL` | `http://civitas-room-config:8010` | URL du Room Config |
| `ROOM_CONFIG_TOKEN` | `civitas-room-config-token` | Token auth Room Config |
| `PEER_SERVICE_TOKEN` | `civitas-peer-token` | Token auth Peer Service |
| `AUTO_JOIN` | `true` | Rejoindre auto à la création |
| `AUTO_LEAVE` | `true` | Quitter auto à la destruction |

---

### 3.5 Peer Service — CIVITAS Peer v3

**Rôle :** Le cœur du système. Chaque instance de Peer représente un agent IA actif dans une room Jitsi. Il gère en parallèle : Chrome headless (Playwright), session audio Gemini Live, et pont audio WebSocket.

**Container :** `civitas-peer`  
**Port :** `8002`  
**Auth API :** Bearer token `civitas-peer-token`

#### Variables de configuration

| Variable | Description |
|----------|-------------|
| `GEMINI_API_KEY` | Clé API Google Gemini (obligatoire) |
| `JITSI_HOST` | `meet.civitas.local` |
| `JITSI_CA_CERT` | `/certs/civitas.local.crt` |
| `ROOM_CONFIG_URL` | `http://civitas-room-config:8010` |
| `ROOM_CONFIG_TOKEN` | `civitas-room-config-token` |
| `KAFKA_BOOTSTRAP` | `civitas-kafka:9094` (listener `INTERNAL` — jamais l'IP hôte) |
| `API_TOKEN` | `civitas-peer-token` |
| `HISTORY_REHYDRATE_LIMIT` | `300` (nb d'entrées rapatriées de l'historique persisté au join) |
| `CONTEXT_MAX_ENTRIES` | `80` (nb d'entrées réinjectées dans Gemini à chaque reconnexion) |
| `ORAL_REQUEST_KEYWORDS` | `oral,voix,parle,vocal,dis à voix,à voix haute,audio` (mots déclenchant une réponse orale sur sollicitation écrite)

#### Modèle Gemini utilisé

`models/gemini-2.5-flash-native-audio-preview-12-2025`

- **Voix :** Aoede
- **Entrée audio :** PCM 16kHz mono int16
- **Sortie audio :** PCM 24kHz mono int16
- **Transcription entrante :** input_audio_transcription activée
- **Transcription sortante :** output_audio_transcription activée

#### Architecture interne du Peer Service (PeerInstance)

Chaque `PeerInstance` orchestre 6 composants :

```
PeerInstance (room_id)
├── ContextStore        — historique des transcriptions en mémoire
├── SpeakerTracker      — identification du locuteur actif
├── EventBus            — bus d'événements interne (pattern pub/sub)
│   ├── Handler: speaker   — met à jour SpeakerTracker
│   ├── Handler: log       — log structuré tous événements
│   ├── Handler: kafka     — publie sur Kafka
│   └── Handler: moderation — réactions auto (main levée, etc.)
├── AudioPipe           — WebSocket local Python (PCM bridge)
├── GeminiSession       — session Gemini Live avec reconnexion auto
└── CivitasBrowser      — Chrome headless Playwright
    ├── RTC_SPY_JS         — intercepte setLocalDescription pour replaceTrack
    ├── AUDIO_BRIDGE_JS    — pont audio JS↔Python via WebSocket
    └── JITSI_EVENTS_JS    — capture tous les événements lib-jitsi-meet
```

#### Cycle de vie d'une PeerInstance

1. **start()** :
   - Charge la config de l'agent (`get_agent_context()` → Room Config Service)
   - Réhydrate la mémoire de réunion : `get_room_history()` → Room Config Service → `ContextStore.seed()` (dégradation gracieuse si indisponible : historique local vide, comme avant)
   - Enregistre les handlers sur l'EventBus
   - Démarre `AudioPipe` (WebSocket local sur port dynamique)
   - Démarre `GeminiSession` (connexion Gemini Live API), avec `context_provider=self._build_catchup_context`
   - Démarre `CivitasBrowser` (Playwright → Jitsi)
   - Attend la connexion AudioPipe (timeout 20s)
   - Lance le watcher de connexion Jitsi (`_watch_connection`, vérifie toutes les 10s)
   - Publie `peer.joined` sur Kafka
   - Envoie un message de bienvenue dans le chat (sauf mode `silent`)

2. **En fonctionnement** :
   - Audio entrant (participants) → AudioPipe → Gemini (`send_audio`)
   - Gemini transcrit → `_on_participant_speech` → ContextStore (local) + Kafka (`room.transcriptions`, persisté durablement côté Room Config)
   - Gemini répond en audio → `_on_gemini_audio` → AudioPipe → Chrome → Jitsi JVB
   - Gemini transcrit sa réponse → `_on_agent_speech` → ContextStore + Kafka
   - Messages chat Jitsi → `_on_chat_message` → ContextStore + Kafka, puis réponse Gemini (texte ou audio)
   - Événements Jitsi → EventBus → handlers (speaker, log, kafka, modération)
   - **À chaque (re)connexion Gemini** (première connexion comme reconnexion après coupure) : `GeminiSession` appelle `context_provider()` — lecture purement locale (`ContextStore.build_context()`, aucune dépendance réseau) — et réinjecte la mémoire de réunion (`end_of_turn=False`, cadrée comme "mémoire interne, ne pas lire à voix haute") avant de reprendre le flux audio normal. L'agent revient donc naturellement dans le sujet en cours même après une coupure, sans jamais avoir besoin de solliciter à nouveau le réseau au moment précis où celui-ci vient de faire défaut.

3. **stop()** :
   - Envoie message d'au revoir dans le chat
   - Arrête Browser → Gemini → AudioPipe
   - Publie `peer.left` sur Kafka

> **Mémoire de réunion — deux niveaux de résilience :**
> 1. *Coupure Gemini / reconnexion* (le cas le plus fréquent) → réinjection instantanée depuis `ContextStore` en RAM, sans aucune I/O réseau.
> 2. *Crash ou redémarrage complet du service peer* → réhydratation depuis Postgres (via Room Config Service) au prochain `start()`, donc l'historique complet survit même à la perte totale du process agent.

#### Règles de réponse de l'agent — `app/peer/response_policy.py`

**Principe :** une sollicitation vocale obtient toujours une réponse vocale (l'agent est un participant comme un autre dans une réunion live). Une sollicitation écrite (chat) obtient par défaut une réponse écrite — pour ne jamais interrompre la réunion avec de l'audio non sollicité — sauf demande explicite d'une réponse orale.

| Condition | Comportement | `ResponseMode` |
|-----------|-------------|-----------------|
| Mode `silent` | L'agent n'intervient jamais | — |
| Parole participant + mot-clé d'invocation | Répond en **audio**, diffusé dans la réunion | `AUDIO` |
| Message chat + mot-clé d'invocation, sans demande orale | Répond par **écrit** dans le chat | `TEXT` |
| Message chat + mot-clé d'invocation + `ORAL_REQUEST_KEYWORDS` ("à voix haute", "vocalement"...) | Répond en **audio** malgré la sollicitation écrite | `AUDIO` |
| Message chat sans mot-clé d'invocation | Ignoré | — |
| Parole/chat + mot-clé + "regarde/screenshot/écran" | Capture frame + vision Gemini, réponse toujours écrite | `TEXT` |
| TALK_WHILE_MUTED Jitsi | Chat automatique d'avertissement | — |
| Raised Hand | Chat automatique de notification | — |
| Seul 10 minutes | Auto-stop | — |

En mode `TEXT`, l'audio généré par Gemini est transcrit (cf. ci-dessous) puis **jamais diffusé** à la réunion (`_on_gemini_audio` l'ignore tant que `response_mode == TEXT`) ; seule sa transcription est postée dans le chat. Le mode revient automatiquement à `AUDIO` juste après.

#### Transcription — garantie de complétude, jamais de fragments

L'API Gemini Live délivre les transcriptions (participant **et** agent) en fragments successifs (deltas), pas en un seul bloc. `GeminiSession` les accumule et ne les restitue qu'une fois complètes :

- Chaque fragment (`input_transcription.text` / `output_transcription.text`) est accumulé dans un buffer dédié.
- Dès que l'API marque le segment `finished=True` (champ natif de `Transcription`), le buffer est vidé et le texte **complet** est transmis en un seul appel (`on_transcription()` / `on_speech()`).
- Filet de sécurité : `turn_complete` ou `interrupted` (coupure de parole) déclenche aussi un flush, pour ne jamais perdre un fragment resté en attente si `finished` n'arrivait pas.
- Une déconnexion abrupte (coupure réseau, avant tout signal `finished`/`turn_complete`) déclenche également ce flush (bloc `finally`) — un fragment déjà reçu n'est jamais silencieusement jeté.

Ainsi : **si l'agent reçoit de l'audio, sa réponse (audio ou texte) vient toujours accompagnée de la transcription complète de ce qu'il a entendu ET de ce qu'il a répondu** — les deux étant persistés dans l'historique de réunion (cf. 3.3).

**Corrélation `turn_id` :** un identifiant (UUID) est généré au premier fragment d'un tour et partagé entre la transcription d'entrée et la réponse de sortie de ce même tour (reset uniquement sur `turn_complete`/`interrupted`, jamais sur un simple vidage local de buffer — sinon la corrélation entrée/sortie casserait dès que l'input est flush avant que l'output ne démarre). Stocké dans le champ `extra.turn_id` de `room_history_entries` — permet de retrouver la paire question/réponse exacte d'un échange dans l'historique persisté.

#### Le pont audio (AudioPipe + AUDIO_BRIDGE_JS)

C'est le composant le plus complexe. Il établit un canal audio bidirectionnel entre Chrome headless et Python :

- **Entrant (participants → Gemini)** :
  - Chrome se connecte aux tracks audio distants via `lib-jitsi-meet` (`TRACK_ADDED`)
  - Web Audio API → AudioWorklet `PCMSender` → convertit Float32 en Int16 → WebSocket Python
  - Python reçoit PCM 16kHz et l'envoie à `GeminiSession.send_audio()`

- **Sortant (Gemini → Jitsi JVB)** :
  - Python reçoit PCM 24kHz de Gemini et l'envoie via WebSocket
  - Chrome reçoit le buffer → AudioContext 24kHz → MediaStreamDestination
  - `RTCPeerConnection.replaceTrack()` injecte le stream dans le flux JVB

Le `RTC_SPY_JS` intercepte `RTCPeerConnection.setLocalDescription` pour garantir que le `replaceTrack` est effectué aux bons moments (4 tentatives : 200ms, 1s, 3s, 6s après chaque négociation SDP).

#### SpeakerTracker — Identification du locuteur

Combine deux signaux :

1. **DOMINANT_SPEAKER_CHANGED** (signal JVB certifié, le plus fiable) — `DominantSpeakerEndpointChangeEvent` du JVB basé sur RFC6464 audio level dans les paquets RTP
2. **TRACK_AUDIO_LEVEL_CHANGED** (niveau par track, 0.0-1.0) — complément local

Logique de résolution (`current_speaker()`) :
- Participants "actifs" = non muté + niveau > 0.04 + timestamp < 2s
- Si dominant speaker est actif → priorité absolue
- Sinon → participant avec niveau le plus élevé
- Ambiguïté si deux niveaux trop proches (delta < 0.05) → `(None, "Participants")`

---

### 3.6 Monitoring Stack

**Composants :**

| Service | Image | Port | Description |
|---------|-------|------|-------------|
| Prometheus | `prom/prometheus:latest` | `9091` | Métriques système |
| Node Exporter | `prom/node-exporter:latest` | — | Métriques hôte Linux |
| Loki | `grafana/loki:2.9.0` | `3100` | Agrégation de logs |
| Promtail | `grafana/promtail:2.9.0` | — | Collecte logs |
| Grafana | `grafana/grafana:latest` | `3000` | Dashboards |

**Auth Grafana :** user `civitas` / password `civitas2024`  
**Rétention Loki :** 168h (7 jours)  
**Rétention Prometheus :** 15 jours

**Sources Prometheus :**
- `localhost:9091` (Prometheus lui-même)
- `192.168.1.89:9100` (JVB metrics)
- `node-exporter:9100` (métriques OS)
- `civitas-kafka-exporter:9308` (Kafka metrics)

**Sources Promtail (logs scrapés) :**
- `/var/log/jitsi/*.log` → label `job: jitsi`
- `/var/log/nginx/*.log` → label `job: nginx`
- `/var/log/turnserver/*.log` → label `job: coturn`
- `/var/log/syslog` → label `job: syslog`

---

## 4. Flux de données complets

### Flux 1 — Création d'une room et injection automatique de l'agent

```
[Participant ouvre Jitsi]
    │
    ▼
[Jitsi Prosody crée le MUC XMPP]
    │ webhook POST /webhook
    ▼
[Event Bridge :8100]
    │ body: { event_name: "muc-room-created", room_name: "salle-42" }
    │ → enrichit avec presence snapshot
    │ → publie sur Kafka "jitsi.room.events"
    ▼
[Kafka topic: jitsi.room.events]
    │
    ▼
[Room Spawner :8011 — consumer group civitas-room-spawner]
    │ event_type == "muc-room-created"
    │ → vérifie Room Config: GET /rooms/salle-42/context (créé si inexistant)
    │ → si peer activé: POST /peer/join { room_id: "salle-42" }
    ▼
[Peer Service :8002]
    │ PeerManager.create("salle-42")
    │ → charge contexte agent depuis Room Config
    │ → démarre AudioPipe (WS local, port dynamique)
    │ → démarre GeminiSession (Gemini Live API)
    │ → démarre CivitasBrowser (Playwright → https://meet.civitas.local/salle-42)
    │   → bypass prejoin
    │   → attend conférence jointe
    │   → injecte RTC_SPY_JS + AUDIO_BRIDGE_JS + JITSI_EVENTS_JS
    │ → attend AudioPipe connecté (timeout 20s)
    │ → publie Kafka "peer.joined"
    │ → envoie chat de bienvenue: "👋 Bonjour ! Je suis CIVITAS..."
    ▼
[Agent CIVITAS actif dans la room]
```

### Flux 2 — Participant parle et l'agent répond

```
[Participant parle: "CIVITAS, quelle heure est-il ?"]
    │
    ▼
[Chrome headless — AUDIO_BRIDGE_JS]
    │ TRACK_AUDIO_LEVEL_CHANGED → WebSocket Python (PCM 16kHz)
    │ (SpeakerTracker mis à jour via AUDIO_LEVEL event)
    ▼
[AudioPipe Python — on_audio_in callback]
    │ → GeminiSession.send_audio(pcm_16k)
    ▼
[Gemini Live API — transcription entrante]
    │ input_transcription.text = "CIVITAS, quelle heure est-il ?"
    │ → PeerInstance._on_participant_speech(text)
    │   → SpeakerTracker.current_speaker() → (ep_id, "Jean Dupont")
    │   → ContextStore.add(...)
    │   → Kafka publish "room.transcriptions"
    │   → vérifie keywords: "civitas" ∈ text → TRUE
    │   → (pas de mot-clé vision)
    │   → GeminiSession.send_text(contexte + question)
    ▼
[Gemini Live API — génération réponse]
    │ output_audio (PCM 24kHz) → PeerInstance._on_gemini_audio(pcm)
    │ output_transcription.text → PeerInstance._on_agent_speech(text)
    ▼
[AudioPipe.send_audio(pcm_24k)]
    │ WebSocket → Chrome headless
    ▼
[AUDIO_BRIDGE_JS — playback 24kHz]
    │ AudioContext(24kHz) → BufferSource → MediaStreamDestination
    │ → replaceTrack sur RTCPeerConnection
    ▼
[Participant entend la réponse de CIVITAS]
```

### Flux 3 — Modérateur éjecte l'agent manuellement

```
[Modérateur appelle POST /moderator/eject { room_id: "salle-42" }]
    │ Authorization: Bearer civitas-peer-token
    ▼
[Room Spawner :8011]
    │ → Room Config PATCH /rooms/salle-42: { extra_config: { peer_enabled: false } }
    │ → _active_rooms.discard("salle-42")
    │ → Peer Client: POST /peer/leave/salle-42
    ▼
[Peer Service :8002]
    │ PeerManager.destroy("salle-42")
    │ → PeerInstance.stop()
    │   → chat: "CIVITAS se déconnecte. À bientôt !"
    │   → CivitasBrowser.stop() (quitte Jitsi + ferme Playwright)
    │   → GeminiSession.stop()
    │   → AudioPipe.stop()
    │   → Kafka publish "peer.left"
    ▼
[Agent retiré de la room]
```

---

## 5. Topologie réseau & ports

**Réseau Docker :** `civitas-net` (external, créé avant le démarrage)  
**IP hôte :** `192.168.1.89`  
**Domaine :** `civitas.local`

| Service | Container | Port hôte | Port interne | Accès |
|---------|-----------|-----------|--------------|-------|
| Jitsi Meet | jitsi/web | 80, 443 | 80, 443 | https://civitas.local |
| Jitsi JVB | jitsi/jvb | 10000/udp | 10000 | WebRTC |
| Kafka | civitas-kafka | 9092 | 9092 | Bootstrap externe |
| Kafka UI | civitas-kafka-ui | 8090 | 8090 | http://kafka-ui.civitas.local |
| Event Bridge | civitas-event-bridge | 8100 | 8100 | http://192.168.1.89:8100 |
| Room Config | civitas-room-config | 8010 | 8010 | http://civitas-room-config:8010 |
| Room Spawner | civitas-room-spawner | 8011 | 8011 | http://192.168.1.89:8011 |
| Peer Service | civitas-peer | 8002 | 8002 | http://civitas-peer:8002 |
| Prometheus | civitas-prometheus | 9091 | 9090 | http://192.168.1.89:9091 |
| Loki | civitas-loki | 3100 | 3100 | http://loki:3100 |
| Grafana | civitas-grafana | 3000 | 3000 | http://grafana.civitas.local |
| PostgreSQL | civitas-postgres | — | 5432 | interne uniquement |

---

## 6. Configuration globale

**Fichier :** `config/civitas.env`

```env
CIVITAS_DOMAIN=civitas.local
CIVITAS_IP=192.168.1.89
JITSI_DOMAIN=meet.civitas.local
KAFKA_DOMAIN=kafka.civitas.local
GRAFANA_DOMAIN=grafana.civitas.local
KAFKA_UI_DOMAIN=kafka-ui.civitas.local
TLS_CERT=/opt/civitas/certs/civitas.local.crt
TLS_KEY=/opt/civitas/certs/civitas.local.key
CA_CERT=/opt/civitas/certs/ca/rootCA.pem
DOCKER_NETWORK=civitas-net
TURN_SECRET=f05b89e355ddc8cc53853dce86b86277556a8e4b79e9450e086f7fa5ce4f2d1f
```

---

## 7. Certificats TLS

**Autorité racine :** `mkcert` (development CA)  
**Outil :** `mkcert civitas@eco-room`  
**Fichiers :**

| Fichier | Description |
|---------|-------------|
| `certs/ca/rootCA.pem` | CA racine à installer dans les navigateurs / curl |
| `certs/ca/rootCA-key.pem` | Clé privée CA (confidentiel) |
| `certs/civitas.local.crt` | Certificat serveur (civitas.local + *.civitas.local) |
| `certs/civitas.local.key` | Clé privée serveur |

**Validité :** 2026-03-23 → 2028-06-23  
**Chemin en production :** `/opt/civitas/certs/`

Le certificat est utilisé par :
- Nginx (HTTPS pour Jitsi Meet, Kafka UI, Grafana)
- `CivitasBrowser` via Playwright (`ca_cert_path` → flag `--ignore-certificate-errors`)

---

## 8. Scripts de démarrage/arrêt

**Démarrage :** `scripts/boot.sh`

Ordre de démarrage (avec attentes) :
1. Attente JVB Jitsi prêt (poll `http://localhost:8080/about/health`, max 180s)
2. Kafka (+ 15s d'attente)
3. Monitoring (Prometheus, Loki, Promtail, Grafana)
4. Room Config (+ 5s d'attente)
5. Room Spawner
6. Event Bridge
7. Peer Service

**Arrêt :** `scripts/stop.sh`

Ordre inverse : Peer → Room Spawner → Event Bridge → Room Config → Monitoring → Kafka

**Chemin de déploiement :** `/opt/civitas/`

---

## 9. Kafka Topics

| Topic | Producteur | Consommateur | Contenu |
|-------|-----------|--------------|---------|
| `jitsi.room.events` | Event Bridge, Peer Service | Room Spawner | Créations/destructions de rooms, événements room |
| `jitsi.participant.events` | Event Bridge, Peer Service | Room Spawner | Entrées/sorties, changements de rôle, mute |
| `jitsi.chat.events` | Event Bridge | — | Messages chat via Prosody |
| `room.presence` | Event Bridge | — | Snapshots de présence en temps réel |
| `room.transcriptions` | Peer Service | — | Transcriptions (participants + agent) |
| `room.agent.actions` | Peer Service | — | Actions de l'agent (vision, etc.) |

---

## 10. Modèle de données Room Config

### Modes de comportement

| Mode | Description |
|------|-------------|
| `on_call` | Agent silencieux, répond uniquement si son nom est mentionné |
| `proactive` | Agent peut prendre l'initiative d'intervenir |
| `silent` | Agent présent dans la room mais n'intervient jamais |

### Permissions granulaires

| Permission | Effet |
|------------|-------|
| `can_speak` | Autorise les réponses audio Gemini |
| `can_write_chat` | Autorise l'écriture dans le chat Jitsi |
| `can_use_tools` | Autorise l'utilisation d'outils externes |
| `can_use_rag` | Autorise l'accès à une base de connaissances |
| `can_moderate` | Autorise les actions de modération |

### extra_config

Dictionnaire libre utilisé pour stocker des configurations supplémentaires. Actuellement utilisé par Room Spawner pour stocker `peer_enabled: bool`.

---

## 11. Modes de comportement de l'agent

### Mode on_call (défaut)

L'agent :
- Écoute tous les participants en permanence
- Ne répond QUE si son nom (`invocation_keywords`) est mentionné
- Répond en audio par défaut
- Répond par chat si la demande est textuelle
- Répond par vision si "regarde/screenshot/écran" est mentionné avec son nom

### Mode proactive

Identique à `on_call` mais l'agent peut prendre l'initiative (non implémenté dans la v3, prévu pour LangGraph).

### Mode silent

L'agent :
- Reste connecté à la room (présent dans la liste des participants)
- N'envoie aucun message chat
- N'envoie aucun audio
- Reste quand même dans la room (utile comme "observateur")

---

## 12. Architecture interne du Peer (détail profond)

### EventBus — Pattern pub/sub interne

```python
bus = EventBus(room_id)
bus.register("*", make_speaker_handler(tracker))   # all events
bus.register("*", make_log_handler(room_id))        # all events
bus.register("*", make_kafka_handler(room_id, kafka))  # all events
bus.register("*", make_moderation_handler(...))     # all events
```

Les handlers sont découplés et composables. Pour ajouter une fonctionnalité LangGraph, il suffit d'implémenter `async def handler(event_type: str, data: dict)` et de l'enregistrer.

### Événements Jitsi capturés

| Événement | Données |
|-----------|---------|
| `USER_JOINED` | participantId, name, role, participants[] |
| `USER_LEFT` | participantId, name, participants[] |
| `USER_ROLE_CHANGED` | participantId, name, role |
| `DISPLAY_NAME_CHANGED` | participantId, name |
| `DOMINANT_SPEAKER_CHANGED` | participantId, name, previousSpeakers[] |
| `TALK_WHILE_MUTED` | participantId, name |
| `NOISY_MIC` | — |
| `TRACK_MUTE_CHANGED` | participantId, name, type, muted |
| `MESSAGE_RECEIVED` | participantId, name, text, timestamp, private:false |
| `PRIVATE_MESSAGE_RECEIVED` | participantId, name, text, timestamp, private:true |
| `REACTION_RECEIVED` | participantId, name, reaction |
| `PARTICIPANT_PROPERTY_CHANGED` | participantId, name, property, oldValue, newValue, raisedHand? |
| `POLL_RECEIVED` | pollId, question, answers, senderId, senderName |
| `POLL_ANSWER_RECEIVED` | pollId, senderId, senderName, answers |
| `SUBJECT_CHANGED` | subject |
| `LOCK_STATE_CHANGED` | locked |
| `KICKED` | participantId, name, reason |
| `PARTICIPANT_KICKED` | kickerId, kickerName, kickedId, kickedName, reason |
| `PARTICIPANTS_SNAPSHOT` | participants[] (initial, au démarrage) |
| `AUDIO_LEVEL` | participantId, level (0.0-1.0) |

### ContextStore — Historique des échanges

Stocke en mémoire (pas en DB) les 50 dernières entrées de la conversation sous forme de `SpeechEntry(speaker_id, speaker_name, text, entry_type, timestamp)`. Utilisé pour construire le contexte envoyé à Gemini.

Types d'entrées :
- `participant` — parole d'un participant (via transcription Gemini)
- `agent` — réponse de l'agent CIVITAS
- `chat` — message chat (préfixé `[chat]`)

### GeminiSession — Reconnexion automatique

La session Gemini Live est enveloppée dans une boucle de reconnexion :
- En cas de déconnexion ou d'erreur, elle attend 2s et se reconnecte
- Un heartbeat envoie du silence PCM toutes les 2s pour maintenir la connexion ouverte
- L'événement `_ready` garantit qu'on n'envoie pas d'audio avant que la session soit établie

### Watcher de connexion Jitsi

Un task asyncio vérifie toutes les 10s (après 30s initiales) que le browser est toujours connecté à Jitsi en évaluant `window.APP?.conference?.isJoined?.()`. Si la connexion est perdue, il appelle `stop()` et se retire du PeerManager.

### Watcher "seul dans la room"

Vérifie toutes les 10s le nombre de participants via `window.APP?.conference?.getParticipants?.().length`. Si l'agent est seul depuis 600s (10 minutes), il se déconnecte automatiquement.

---

*Documentation générée automatiquement par analyse complète du dépôt ECO-ROOM. Tous les fichiers ont été lus sans exception.*
