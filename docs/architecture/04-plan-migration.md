# Plan de migration — phasé, fichier par fichier

> Convertit les 3 documents précédents en un plan d'exécution concret : ordre des phases,
> fichiers touchés, critères de bascule, stratégie de rollback. Chaque phase est livrable et
> testable indépendamment — aucune phase ne suppose que la suivante existe déjà.

---

## Vue d'ensemble des phases

| Phase | Objectif | Statut à l'issue de cette session |
|---|---|---|
| **0** | Documentation + squelette de code | ✅ Livré dans cette session (ce commit) |
| **1** | `civitas-agent` — parité fonctionnelle avec `peer`, une seule room, lancée manuellement | À faire — squelette posé, logique métier à finaliser/tester |
| **2** | `civitas-orchestrator` — spawn/route/teardown automatique, bascule progressive | À faire |
| **3** | Catalogue d'outils P0 (doc 02) implémenté et testé | À faire |
| **4** | Domaine 4 — `platform_tools`, `rag_tools`, Qdrant/MinIO | À faire |
| **5** | Catalogue P1 (breakout rooms, sondages, E2EE, streaming) | À faire |
| **6** | Bascule finale + suppression de `services/peer` et `services/room-spawner` | À faire, conditionnée aux phases précédentes |

---

## Phase 0 — Documentation + squelette (cette session)

### Livrés

- `docs/architecture/00-etat-des-lieux.md`
- `docs/architecture/01-architecture-cible-civitas-agent.md`
- `docs/architecture/02-catalogue-outils-agent.md`
- `docs/architecture/03-isolation-et-orchestration.md`
- `docs/architecture/04-plan-migration.md` (ce document)
- `services/civitas-agent/` — squelette de code (structure de doc 01 §8, modules portés,
  registre d'outils fonctionnel, graphe LangGraph assemblé avec des nœuds réels mais dont la
  logique de raisonnement fine reste à enrichir en Phase 1)
- `services/civitas-orchestrator/` — squelette de code (registre, provider Docker, forwarder,
  consumer Kafka porté de `room-spawner`)
- `services/peer/DEPRECATED.md` — avis de dépréciation, sans suppression du code (cf. §Phase 6)
- Mise à jour de la table des matières du `README.md` racine pointant vers cette documentation

### Ce qui n'est PAS fait en Phase 0 (assumé explicitement)

- Le squelette `services/civitas-agent` n'a pas encore été **exécuté** contre un vrai cluster
  Jitsi (pas de `docker build` + `docker run` réel effectué dans cette session — l'environnement
  d'édition n'a pas accès au serveur `192.168.1.89`, à Gemini, ni à un Jitsi déployé).
- Les outils marqués 🔧 P1 dans le catalogue (doc 02) ne sont pas implémentés — seulement
  déclarés dans le registre avec un statut explicite (`NotImplementedError` documenté, jamais un
  faux succès silencieux).
- Le pipeline RAG (Qdrant/MinIO) n'existe pas encore — seule l'interface `rag_tools` est posée.

---

## Phase 1 — `civitas-agent` : parité fonctionnelle, une seule room

### Objectif de sortie de phase

Un opérateur peut lancer `docker run -e ROOM_ID=test-room ... civitas-agent-runtime` et obtenir
un comportement **au moins équivalent** à `civitas-peer` aujourd'hui pour une room unique :
rejoindre la room, écouter, transcrire, répondre en audio/texte selon `response_policy`,
kick/mute/chat/vision, réhydratation mémoire, reconnexion Gemini.

### Fichiers à finaliser (déjà scaffoldés en Phase 0, cf. arborescence doc 01 §8)

1. `app/browser/driver.py` — reporter les 3 scripts JS (`RTC_SPY_JS`, `AUDIO_BRIDGE_JS`,
   `JITSI_EVENTS_JS`) **sans modification fonctionnelle** depuis `services/peer/app/browser/browser.py`
   (copier-coller contrôlé, pas de réécriture — c'est du JS déjà validé en production).
2. `app/speech/gemini_live.py` — porter `services/peer/app/gemini/session.py` à l'identique
   (reconnexion, heartbeat, accumulation par tour, `context_provider`).
3. `app/perception/audio_pipe.py`, `app/perception/speaker_tracker.py` — port direct.
4. `app/context/store.py` — port direct.
5. `app/graph/nodes/*.py` — remplacer les stubs par la logique réelle, en réutilisant
   `response_policy.decide_chat_response_mode` (port direct) dans `routing.py`, et en
   reproduisant fidèlement la séquence `_on_participant_speech`/`_on_chat_message`/
   `_handle_vision` de l'ancien `PeerInstance` à l'intérieur de `reasoning.py`/`acting.py`.
6. `app/kafka/producer.py` — port direct.
7. `app/room/config_client.py` — port direct, endpoints `room-config` inchangés.

### Tests de non-régression (à écrire en Phase 1, gabarits déjà présents dans le squelette)

- Rejeu des scénarios déjà documentés dans `DOCUMENTATION_API.md` §0 et §9 (cycle de vie complet
  d'un peer dans une room), adaptés à `civitas-agent`.
- Test unitaire `tools/registry.py` : un outil hors `tools_allowed` est refusé avec
  `{"allowed": false, ...}`, jamais une exception non gérée.
- Test unitaire du graphe : un événement `USER_JOINED` traverse
  `ingest_control_event → update_state` et produit un `ConferenceAgentState.participants` à
  jour, sans appeler `reason`/`act` (pas de raison de répondre à une simple entrée).

### Critère de bascule vers Phase 2

`civitas-agent` tourne de façon stable (test manuel prolongé, ≥ 1h, une room réelle) avec
parité observée sur les 5 actions déjà en production (`send_chat`, `send_text`, `kick`, `mute`,
`capture_frame`) + audio bidirectionnel Gemini Live fonctionnel.

---

## Phase 2 — `civitas-orchestrator` : spawn/route/teardown automatique

### Fichiers à finaliser (scaffoldés en Phase 0)

1. `app/kafka_consumer.py` — port direct de `services/room-spawner/app/kafka_consumer.py`
   (même topics, même sémantique at-least-once).
2. `app/registry.py` — implémenté en Phase 0 (structure `AgentHandle`/`AgentRegistry`).
3. `app/docker_runtime.py` — implémenter `DockerAgentRuntimeProvider` avec le SDK `docker`
   Python (`pip install docker`), labels `civitas.agent=true` + `civitas.room_id=<room_id>`
   pour permettre la reconstruction du registre (doc 03 §4.5).
4. `app/forwarder.py` — implémenté en Phase 0 (structure simple, cf. doc 03 §4.6).
5. `app/agent_client.py` — client HTTP vers `/admin/*` d'un agent précis (remplace
   `services/room-spawner/app/peer_client.py`, même contrat de sortie pour compatibilité CLI).
6. `app/main.py` — reprendre les routes `/moderator/*` de `room-spawner` à l'identique
   (contrat HTTP conservé pour ne pas casser `cli/civitas` immédiatement), en les faisant
   pointer vers `agent_client` + `registry` au lieu de `peer_client` + appel à un service unique.

### Migration du schéma `room_configs` — colonne `peer_enabled` → `agent_enabled`

Cohérent avec la disparition du concept "peer" : une migration Alembic dédiée, **additive et
réversible**, en 3 étapes espacées dans le temps (jamais un `ALTER COLUMN RENAME` brutal qui
casserait `room-spawner`/`peer` encore en service pendant la bascule) :

```
Migration A (début Phase 2) : ADD COLUMN agent_enabled BOOLEAN DEFAULT TRUE
                               → backfill agent_enabled = peer_enabled pour les lignes existantes
                               → civitas-orchestrator lit/écrit agent_enabled
                               → services/room-spawner (encore actif en parallèle, cf. §Bascule
                                 progressive) continue de lire/écrire peer_enabled
                               → un trigger applicatif (dans room-config, pas en DB) recopie
                                 chaque écriture de l'un vers l'autre tant que les deux
                                 orchestrateurs coexistent
Migration B (Phase 6)        : suppression de la synchronisation applicative +
                               DROP COLUMN peer_enabled, une fois room-spawner désactivé
```

`RoomConfigUpdate`/`RoomConfigResponse` (schémas Pydantic, `services/room-config/app/schemas/`)
exposent les deux champs en Migration A, un seul en Migration B — changement non cassant pour
les clients existants pendant toute la période de transition.

### Bascule progressive — les deux orchestrateurs coexistent un temps

`room-spawner` (ancien) et `civitas-orchestrator` (nouveau) peuvent tourner **en parallèle**
pendant la validation, à condition de ne jamais gérer la même room simultanément — mécanisme :
un flag par room dans `extra_config` (`orchestrator: "legacy" | "civitas-agent"`), lu par les
deux consumers Kafka pour décider s'ils doivent agir sur l'événement ou l'ignorer. Permet un
test A/B room par room, sans big-bang, et un retour arrière immédiat par simple changement de
flag si un problème est constaté sur `civitas-agent` en conditions réelles.

### Critère de bascule vers Phase 3

Au moins 3 rooms réelles gérées exclusivement par `civitas-orchestrator`/`civitas-agent`
pendant ≥ 48h sans incident, y compris un test explicite de l'exigence d'isolation : provoquer
un crash volontaire (ex: `docker kill` du container d'une room) et vérifier que les autres
rooms actives ne sont pas affectées (test de "chaos engineering" ciblé, à documenter dans
`services/civitas-orchestrator/tests/test_isolation.py`).

---

## Phase 3 — Catalogue d'outils P0 (doc 02)

Implémentation, dans l'ordre de dépendance le plus naturel :

1. `presence_tools` (raise/lower hand, set_display_name, mute/unmute applicatif) — le plus
   simple, pas de dépendance externe nouvelle.
2. `moderation_tools` — extension (grant_moderator, AV moderation, lobby) au-delà de
   kick/mute déjà portés en Phase 1.
3. `room_tools` — subject, lock/unlock, end_meeting.
4. `chat_tools` — send_private_chat, send_reaction (create/answer_poll restent en Phase 5, P1
   assumé, cf. doc 02 §11).
5. `media_tools` — start/stop recording (dépend de Jibri déjà configuré ou non côté infra —
   vérifier en amont, hors périmètre CIVITAS).
6. `vision_tools` — rendre `describe_screen`/`read_shared_content` appelables directement par le
   nœud `reason`, pas seulement par mot-clé (bascule du hardcode vers un vrai choix de l'agent).

Chaque outil livré avec : le test unitaire de permission (refus propre si `can_moderate`/
`tools_allowed` ne l'autorise pas) + un test d'intégration manuel documenté (checklist
reproduisant `DOCUMENTATION_API.md`, section à créer `docs/architecture/tests-manuels-outils.md`
si le volume le justifie — décision à prendre en Phase 3 selon le nombre d'outils réellement
livrés).

---

## Phase 4 — Domaine 4 : `platform_tools`, `rag_tools`, Qdrant/MinIO

1. Définir les APIs CIVITAS Platform réellement nécessaires (`get_user`, `get_meeting`,
   `create_task`, `create_minutes`, `create_vote`) — **dépend de systèmes métier externes au
   dépôt ECO-ROOM actuel**, non encore identifiés dans le code existant. Cette phase nécessite
   une clarification produit (quelles APIs existent déjà côté CIVITAS Platform, lesquelles sont
   à créer) avant toute implémentation — volontairement non anticipée à tort dans ce document.
2. Ajouter les services `Qdrant` et `MinIO` au déploiement (`docker-compose.yml` dédiés, sur le
   modèle de `kafka/docker-compose.yml`/`monitoring/docker-compose.yml` déjà présents).
3. Pipeline d'ingestion documentaire (doc 01 §7) : MinIO → extraction → embedding → Qdrant —
   nouveau composant, potentiellement un service dédié `services/knowledge-ingest/` plutôt
   qu'une logique interne au CIVITAS Agent (pour ne pas alourdir chaque process agent d'un
   pipeline d'indexation qui n'a pas besoin d'être répété par room).
4. `rag_tools.query_knowledge_base` — implémentation finale, soumise à `can_use_rag`.

---

## Phase 5 — Catalogue P1 (doc 02) et fonctionnalités avancées

- Sondages (`create_poll`/`answer_poll`) — après inspection du bundle JS déployé (doc 02 §11).
- Breakout rooms (`manage_breakout_rooms`) — après inspection du composant XMPP dédié
  (`mod_muc_breakout_rooms.lua`, déjà vendé dans `nginx/jitsi-meet-host-backup/prosody-plugins/`).
- E2EE (`toggle_e2ee` + gestion de `setMediaEncryptionKey`) — sujet sensible nécessitant une
  revue dédiée (partage de clé avec un agent automatisé = surface de risque à documenter avant
  activation, pas un simple toggle).
- Streaming live (`start_recording(mode="stream")`) — dépend de la configuration Jibri +
  fourniture sécurisée de la clé de stream (jamais en clair dans les logs/Kafka).
- SIP/dial-out — dépend d'une passerelle SIP configurée, hors périmètre CIVITAS.

---

## Phase 6 — Bascule finale et suppression de l'ancien code

**Condition de déclenchement** : Phase 2 validée en production sur 100% des rooms depuis une
durée jugée suffisante par l'équipe opérationnelle (pas de date fixée arbitrairement ici —
c'est une décision opérationnelle, pas architecturale).

### Actions

1. Couper `services/room-spawner` et `services/peer` (`docker compose down`, retrait de
   `scripts/boot.sh`/`scripts/stop.sh`).
2. Migration Alembic B (§Phase 2) : `DROP COLUMN peer_enabled`.
3. Suppression physique de `services/peer/` et `services/room-spawner/` du dépôt (dans un commit
   dédié, séparé, facilement identifiable et **revertable** via Git si un besoin de comparaison
   avec l'ancien code se présentait malgré tout).
4. Mise à jour de `README.md` racine : retrait des sections legacy (§3.4, §3.5, §11, §12
   actuelles), le contenu de ce dossier `docs/architecture/` devient la documentation de
   référence unique.
5. `cli/civitas` : retrait des alias de compatibilité `peer *` une fois `agent *` (§CLI
   ci-dessous) validé en usage réel.
6. `scripts/boot.sh`/`scripts/stop.sh` : remplacer les étapes "Room Spawner"/"Peer Service" par
   "CIVITAS Agent Orchestrator" (les agents eux-mêmes ne sont **jamais** démarrés par ces
   scripts globaux — ils sont spawnés à la demande par l'orchestrateur, cf. doc 03 §4 — c'est un
   changement de nature du script de boot, pas juste un renommage).

---

## Évolution du CLI (`cli/civitas`)

Nouvelle sous-commande `civitas agent` en complément de `civitas peer` (conservée en alias
dépréciée jusqu'à Phase 6) :

```
civitas agent status <room_id>        # équivalent de `peer status`, via l'orchestrateur
civitas agent list                    # liste des agents actifs (remplace `peer active` + `peer instances`)
civitas agent kick <room_id> <id>     # inchangé dans son contrat
civitas agent mute <room_id> <id>     # inchangé
civitas agent send-chat <room_id> ... # inchangé
civitas agent send-text <room_id> ... # inchangé
civitas agent inject/eject/standby/activate <room_id>   # inchangé (mêmes endpoints /moderator/*)
```

Le contrat HTTP exposé par `civitas-orchestrator` (`/moderator/*`) est conçu pour rester
**identique** à celui de `room-spawner` aujourd'hui (doc 03 §4.1) précisément pour que cette
évolution du CLI soit un simple ajout de sous-commande, jamais une réécriture de `cli/civitas`.

---

## Récapitulatif des fichiers créés en Phase 0 (cette session)

```
docs/architecture/
├── 00-etat-des-lieux.md
├── 01-architecture-cible-civitas-agent.md
├── 02-catalogue-outils-agent.md
├── 03-isolation-et-orchestration.md
└── 04-plan-migration.md                       (ce document)

services/civitas-agent/                         (squelette — cf. commit associé)
services/civitas-orchestrator/                  (squelette — cf. commit associé)
services/peer/DEPRECATED.md                     (avis de dépréciation)
README.md                                       (mis à jour — pointeurs vers docs/architecture/)
```
