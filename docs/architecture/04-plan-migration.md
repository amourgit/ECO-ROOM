# Plan de migration — phasé, fichier par fichier

> Convertit les 3 documents précédents en un plan d'exécution concret : ordre des phases,
> fichiers touchés, critères de bascule, stratégie de rollback. Chaque phase est livrable et
> testable indépendamment — aucune phase ne suppose que la suivante existe déjà.

---

## Vue d'ensemble des phases

| Phase | Objectif | Statut à l'issue de cette session |
|---|---|---|
| **0** | Documentation + squelette de code | ✅ Livré |
| **1** | `civitas-agent` — parité fonctionnelle avec `peer`, une seule room, lancée manuellement | 🔶 En cours — squelette posé, **tests unitaires écrits et verts** (49 tests, cf. §Tests unitaires ci-dessous), intégration réelle (Jitsi/Gemini/Kafka/Postgres) restant à faire |
| **2** | `civitas-orchestrator` — spawn/route/teardown automatique, bascule progressive | 🔶 En cours — squelette posé, **migration Alembic A appliquée et validée contre un vrai Postgres**, endpoints modérateur corrigés et testés (23 tests), spawn/teardown Docker réel restant à valider (cf. §Phase 2 ci-dessous) |
| **3** | Catalogue d'outils P0 (doc 02) implémenté et testé | 🔶 Largement fait dès la Phase 0 — tous les outils P0 sont déjà enregistrés dans `tools/registry.py` avec une implémentation réelle contre `browser/driver.py` ; reste à valider contre un vrai Jitsi (Phase 1) |
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
  d'édition n'a pas accès au serveur de déploiement réel (dont l'IP est auto-détectée au
  provisioning, jamais fixée en dur — cf. doc 03 §3.1bis), à Gemini, ni à un Jitsi déployé).
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

### Tests unitaires — écrits et exécutés avec succès dans cette session

`services/civitas-agent/tests/` (49 tests), `services/civitas-orchestrator/tests/` (23 tests)
et `services/room-config/tests/` (10 tests) — **82 tests au total, tous verts** — cf. les
sections "Tests" des `README.md` respectifs pour le détail. Deux niveaux de rigueur bien
distincts, à ne pas confondre :

- **`civitas-agent`/`civitas-orchestrator`** : logique pure avec des dépendances **simulées**
  (navigateur, moteur de parole, Kafka, Docker mockés). Ils prouvent que le graphe LangGraph
  s'assemble et s'exécute réellement (routage d'entrée conditionnel, arête `route`,
  déclenchement d'outil via le registre, isolation d'état entre deux graphes indépendants, et
  désormais le **rechargement de configuration en direct sans reconstruction du graphe**), que
  le gating de permissions (`tools/registry.py`, doc 01 §9) refuse correctement (jamais un faux
  succès silencieux), que `slugify_room_id` ne fait jamais collisionner deux rooms distinctes,
  et que les endpoints `/moderator/*` reproduisent fidèlement (ou améliorent délibérément, cf.
  §Phase 2 ci-dessus) le comportement de l'original `room-spawner`.
- **`room-config`** : contre une **vraie base Postgres 16** (installée dans l'environnement de
  développement via `apt` spécifiquement pour cette validation), pas une simulation — la
  migration `0002_add_agent_enabled` a été exécutée pour de vrai contre un schéma
  pré-migration reconstruit fidèlement, avec un backfill vérifié ligne par ligne sur des
  données hétérogènes, plus la réversibilité complète (downgrade/re-upgrade). C'est le niveau
  de validation le plus élevé atteignable sans le serveur de déploiement réel lui-même.

Ce travail a aussi mis au jour et corrigé, en cours de route, quatre défauts réels — pas
seulement écrit du code présumé correct (cf. §Phase 2 ci-dessus pour le détail complet de
chacun) :
1. `is_agent_enabled()` lisait le mauvais niveau d'imbrication JSON (`civitas-orchestrator`).
2. `/moderator/standby` détruisait le container au lieu de simplement rendre l'agent silencieux
   (`civitas-orchestrator`).
3. `/moderator/activate` spawnait un nouveau container au lieu de réactiver l'agent déjà actif
   (`civitas-orchestrator`).
4. `DockerAgentRuntimeProvider` se connectait à Docker dès l'import du module, rendant
   `civitas-orchestrator` impossible à tester (et fragile au démarrage) sans démon Docker déjà
   disponible.

Ce que ces tests NE remplacent PAS — et qui reste le véritable critère de sortie des Phases 1
et 2 :

- Rejeu des scénarios déjà documentés dans `DOCUMENTATION_API.md` §0 et §9 (cycle de vie complet
  d'un agent dans une room), adaptés à `civitas-agent`, **contre un vrai cluster Jitsi**.
- Une session Gemini Live (ou OpenAI Realtime, doc 05) réelle, avec un vrai flux audio Jitsi.
- Un vrai broker Kafka et un vrai `AsyncPostgresSaver` Postgres pour le checkpoint LangGraph (le
  smoke test du graphe utilise `MemorySaver`, en mémoire — noter que `room-config`, lui,
  utilise déjà un vrai Postgres, cf. ci-dessus ; seul le checkpoint LangGraph du CIVITAS Agent
  lui-même reste non testé contre un vrai Postgres).
- Un vrai daemon Docker pour valider `DockerAgentRuntimeProvider.spawn/teardown` en conditions
  réelles (la logique de connexion paresseuse est corrigée et le reste du provider est écrit,
  mais l'appel réel à l'API Docker n'a pu être exercé).

Ces points nécessitent le serveur de déploiement réel dont l'IP est auto-détectée au
provisioning par `scripts/lib/jitsi_common.sh::detect_server_ip()` (cf. doc 03 §3.1bis — jamais
une IP fixée en dur) — ils ne peuvent pas être validés depuis un environnement de développement
sans accès à Jitsi/Gemini/Kafka/Docker réels, et restent donc le travail restant avant bascule
vers la Phase 3.

### Critère de bascule vers Phase 2

`civitas-agent` tourne de façon stable (test manuel prolongé, ≥ 1h, une room réelle) avec
parité observée sur les 5 actions déjà en production (`send_chat`, `send_text`, `kick`, `mute`,
`capture_frame`) + audio bidirectionnel Gemini Live fonctionnel.

---

## Phase 2 — `civitas-orchestrator` : spawn/route/teardown automatique

### Fichiers finalisés (scaffoldés en Phase 0, complétés et corrigés dans cette session)

1. `app/kafka_consumer.py` — port direct de `services/room-spawner/app/kafka_consumer.py`
   (même topics, même sémantique at-least-once). Inchangé depuis Phase 0.
2. `app/registry.py` — implémenté en Phase 0 (structure `AgentHandle`/`AgentRegistry`), testé
   (`tests/test_registry.py`).
3. `app/docker_runtime.py` — `DockerAgentRuntimeProvider` avec le SDK `docker` Python, labels
   `civitas.agent=true` + `civitas.room_id=<room_id>` pour la reconstruction du registre
   (doc 03 §4.5). **Corrigé dans cette session** : la connexion au démon Docker
   (`docker.from_env()`) se faisait à tort dans `__init__`, empêchant `app.main` d'être ne
   serait-ce qu'importé sans un démon Docker déjà actif, et aurait fait planter l'Orchestrateur
   au démarrage sur une indisponibilité Docker transitoire, avant même de pouvoir servir
   `/health`. Rendue paresseuse (propriété `_client`, connexion différée au premier usage réel)
   — trouvé en tentant précisément de tester ce module dans un environnement sans démon Docker.
4. `app/forwarder.py` — implémenté en Phase 0, inchangé.
5. `app/agent_client.py` — client HTTP vers `/admin/*` d'un agent précis (remplace
   `services/room-spawner/app/peer_client.py`). Complété dans cette session avec
   `reload_config()` (cf. §Rechargement en direct ci-dessous).
6. `app/room_config_client.py` — **bug réel corrigé** : `is_agent_enabled()` lisait
   `agent_enabled`/`peer_enabled` à la racine de la réponse `/rooms/{room_id}/context`, alors
   que ces deux champs sont imbriqués sous `permissions` (`AgentContextResponse`, cf.
   `services/room-config/app/schemas/room_config.py`) — exactement comme l'original
   `is_peer_enabled()` de `room-spawner` le lisait déjà correctement. Sans cette correction,
   `is_agent_enabled()` serait systématiquement retombé sur son défaut `True`, quel que soit
   l'état réel persisté — le même bug que celui déjà documenté et corrigé côté `peer_enabled`
   avant cette session (commentaire "Corrige le bug §2.3/§7.5 du plan" dans
   `room_config_service.py::build_agent_context`). Corrigé + testé
   (`tests/test_room_config_client.py`, 6 tests).
7. `app/main.py` — routes `/moderator/*` **vérifiées ligne par ligne contre l'original**
   (`services/room-spawner/app/spawner.py`) plutôt que déduites de son nom, ce qui a révélé
   deux vraies divergences de comportement corrigées dans cette session (cf.
   §Corrections de parité ci-dessous). Testé (`tests/test_moderator_routes.py`, 9 tests).

### Corrections de parité — deux bugs de comportement trouvés en revérifiant l'original

La Phase 0 avait scaffoldé `/moderator/standby` et `/moderator/activate` en devinant leur
comportement à partir de leur nom plutôt qu'en relisant `services/room-spawner/app/spawner.py`
ligne par ligne. Cette relecture, faite dans cette session avant de considérer la Phase 2
"finalisée", a révélé que **standby ne coupe jamais l'agent** — `set_peer_standby`
(l'original) ne fait qu'un `PATCH behavior_mode=silent` sur `room-config`, l'agent reste
connecté à la room et continue d'écouter, il se contente de ne plus intervenir. Un agent "en
standby" est un figurant silencieux, pas un agent éjecté.

| Endpoint | Comportement scaffoldé en Phase 0 (incorrect) | Comportement réel de l'original, désormais reproduit |
|---|---|---|
| `/moderator/standby` | Appelait `agent_client.shutdown()` — détruisait le container | `PATCH behavior_mode=silent` sur room-config, container jamais touché |
| `/moderator/activate` | Aliasait sur `/moderator/inject` — spawnait un nouveau container | `PATCH behavior_mode=on_call`, aucun spawn (suppose un agent déjà actif, éventuellement en standby) |

Les deux sont désormais corrigés dans `app/main.py`, avec des tests de régression dédiés
(`test_standby_never_tears_down_the_container`,
`test_activate_never_spawns_a_new_container`) qui échoueraient si cette erreur était
réintroduite.

### Rechargement en direct — amélioration délibérée au-delà du comportement original

En vérifiant l'original, une limitation préexistante est apparue : `PeerInstance.start()`
(`services/peer/app/peer/instance.py`) charge `self.context` (dont `behavior_mode`) **une
seule fois**, jamais rafraîchi. `set_peer_standby`/`activate_peer` ne font qu'un `PATCH` côté
base — ils ne notifient jamais le peer déjà connecté. Un `/moderator/standby` sur une room
active ne prenait donc réellement effet qu'au **prochain redémarrage** du peer, jamais en
direct — une limitation déjà présente dans le système actuel, pas quelque chose introduit par
cette refonte.

L'architecture LangGraph rend une vraie correction naturelle et peu risquée, donc **faite
délibérément dans cette session**, documentée explicitement plutôt que silencieuse :

1. `services/civitas-agent/app/graph/nodes/routing.py` relit désormais `deps.room_config`
   (`behavior_mode`, `invocation_keywords`, `oral_request_keywords`) à **chaque** invocation du
   nœud `route`, plutôt que de les capturer une seule fois à la construction du graphe.
2. Nouvelle route `POST /admin/reload_config` (`services/civitas-agent/app/main.py`) : relit
   la config depuis room-config et met à jour `runtime.room_config` **en place**
   (`dict.clear()` + `dict.update()`, jamais de réassignation) — `GraphDeps.room_config`
   référence le même objet, donc voit le changement immédiatement, sans reconstruire le graphe.
3. `civitas-orchestrator` appelle cette route juste après avoir persisté le nouveau
   `behavior_mode`, dans `/moderator/standby` et `/moderator/activate`.

Validé par un test dédié qui invoque le **même graphe compilé** deux fois, avec une mutation
en place de `room_config` entre les deux appels, et vérifie que la décision change bien sans
reconstruction (`services/civitas-agent/tests/test_live_reload.py`) — la route HTTP elle-même
n'est pas testable dans cet environnement (dépendances lourdes indisponibles, cf. §Tests
unitaires), mais le mécanisme dont elle dépend est prouvé fonctionner.

### Migration du schéma `room_configs` — colonne `peer_enabled` → `agent_enabled`

**Migration A appliquée et validée dans cette session**, pas seulement planifiée. Cohérent
avec la disparition du concept "peer" : une migration Alembic additive et réversible, en 3
étapes espacées dans le temps (jamais un `ALTER COLUMN RENAME` brutal qui casserait
`room-spawner`/`peer` encore en service pendant la bascule) :

```
Migration A (FAITE, cf. ci-dessous) : ADD COLUMN agent_enabled BOOLEAN NOT NULL DEFAULT TRUE
                               → backfill agent_enabled = peer_enabled pour les lignes existantes
                               → civitas-orchestrator lit/écrit agent_enabled
                               → services/room-spawner (encore actif en parallèle, cf. §Bascule
                                 progressive) continue de lire/écrire peer_enabled
                               → une synchronisation applicative (dans room-config, PAS en DB —
                                 jamais de trigger SQL, pour rester lisible et traçable dans les
                                 logs) recopie chaque écriture de l'un vers l'autre tant que les
                                 deux orchestrateurs coexistent
Migration B (Phase 6)        : suppression de la synchronisation applicative +
                               DROP COLUMN peer_enabled, une fois room-spawner désactivé —
                               PAS écrite par anticipation, seulement au moment de la Phase 6
```

Fichiers touchés : `services/room-config/app/models/room_config.py` (colonne),
`app/schemas/room_config.py` (`RoomConfigCreate`/`Update`/`Response`),
`app/services/room_config_service.py` (`_sync_agent_peer_enabled`, appelée dans
`create_room_config`/`reserve_room_config`/`update_room_config`, et
`build_agent_context` qui expose désormais `agent_enabled` à côté de `peer_enabled` sous
`permissions`), `migrations/versions/0002_add_agent_enabled.py`.

**Validation** : la migration a été exécutée contre une vraie base Postgres (16.15, installée
dans l'environnement de développement via `apt`), pas seulement relue. Méthode : schéma
pré-migration reconstruit à l'identique de la révision 0001 (SQL brut, pas
`Base.metadata.create_all()` avec les modèles actuels, pour ne pas fausser le test), 4 lignes
avec des valeurs `peer_enabled` hétérogènes insérées, migration appliquée, backfill vérifié
ligne par ligne (`agent_enabled` reproduit exactement `peer_enabled`, pas une valeur par
défaut uniforme), puis downgrade/re-upgrade vérifiés pour la réversibilité complète —
formalisé dans `services/room-config/tests/test_migration_0002.py`. La synchronisation
applicative bidirectionnelle (create/update/reserve, dans les deux sens, y compris le cas où
aucun des deux flags n'est fourni) est testée dans
`services/room-config/tests/test_agent_enabled_sync.py` (9 tests), également contre une vraie
base Postgres dédiée (`tests/conftest.py`).

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

**Non encore implémenté** (contrairement à la migration `agent_enabled` ci-dessus, qui l'est) :
ce mécanisme de flag reste au stade de la description — `_handle_kafka_event`
(`app/main.py`) ne le consulte pas encore. À faire avant tout déploiement en parallèle réel
avec `room-spawner`.

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
