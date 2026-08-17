# Isolation par room & Orchestration — CIVITAS Agent Orchestrator

> Répond à l'exigence centrale posée pour cette refonte : **« les processus dans chaque room
> sont complètement séparés — si un CIVITAS Agent plante dans une room, ça ne doit pas affecter
> les autres rooms. »** Ce document détaille le mécanisme concret qui garantit cette propriété,
> et l'évolution de `room-spawner` en **CIVITAS Agent Orchestrator** qui la met en œuvre.

---

## 1. Le problème exact à résoudre (rappel doc 00 §5.1)

Aujourd'hui : 1 container `civitas-peer` → 1 process Python → 1 `PeerManager` → N
`PeerInstance` en tâches `asyncio` dans le **même** event loop. Un crash, une fuite mémoire, un
deadlock ou un bug de librairie affecte **toutes** les rooms simultanément.

Exigence cible, formulée comme un invariant vérifiable :

> **Un process CIVITAS Agent ne connaît, ne peut lire, ne peut écrire et ne peut faire planter
> que l'état d'une seule room — la sienne — de façon structurelle (pas seulement
> conventionnelle).**

---

## 2. La garantie structurelle : un process = un `ROOM_ID`, jamais réassignable

Chaque process CIVITAS Agent (doc 01 §8) reçoit `ROOM_ID` en **variable d'environnement au
démarrage du process**, jamais en paramètre de requête HTTP mutable :

```python
# app/config.py
class Settings(BaseSettings):
    ROOM_ID: str                 # obligatoire, pas de valeur par défaut — le process
                                  # refuse de démarrer sans identité de room fixée
    ...
```

Conséquences directement vérifiables dans le code (doc 01 §8.1) :

- Le `ConferenceAgentState.conference.room_id` est initialisé une seule fois à `Settings.ROOM_ID`
  et jamais réécrit ailleurs dans le code.
- Le checkpoint LangGraph utilise `thread_id = Settings.ROOM_ID` — un seul thread possible par
  process (doc 01 §7 niveau 3).
- Les routes HTTP de contrôle (`/admin/kick`, `/admin/mute`…) n'acceptent **plus** de `room_id`
  en paramètre (contrairement à `peer-service` aujourd'hui) — il ne peut structurellement pas y
  avoir de confusion inter-room au niveau de l'API elle-même (doc 01 §8.1).
- Le navigateur headless de ce process ne rejoint **qu'une seule** URL Jitsi
  (`https://meet.civitas.local/{ROOM_ID}`), fixée au démarrage.

C'est la différence essentielle avec `PeerManager` : là où l'isolation reposait sur la
*discipline du code* (bien indexer un dictionnaire par `room_id`, ne jamais mélanger deux
`PeerInstance`), elle repose ici sur une **impossibilité physique** — il n'existe tout
simplement aucune autre room que celle fournie au process pour que du code, même buggé, puisse
s'y référer.

---

## 3. La garantie d'exécution : un process OS = un container Docker, par room

La garantie de state ci-dessus protège contre les **erreurs logiques**. Il faut en plus une
garantie contre les **pannes d'exécution** (OOM, crash du garbage collector, crash de Chromium,
exception non rattrapée qui tue l'event loop) : c'est le rôle de l'isolation **container par
room**.

### 3.1 Option retenue par défaut : container Docker éphémère par room

- Un container `civitas-agent-<slug(room_id)>` est démarré dynamiquement par l'Orchestrateur
  (§4) pour chaque room qui doit avoir un agent actif, sur le réseau `civitas-net` existant
  (résolution DNS par nom de container, comme `civitas-peer` aujourd'hui).
- `slug(room_id)` : minuscule, `[a-z0-9-]`, tronqué + suffixe de hash court en cas de collision
  (les noms de room saisis par les humains peuvent contenir des caractères hors charte des noms
  de container Docker).
- Chaque container a ses **propres limites de ressources** (`mem_limit`, `shm_size` — reprend la
  valeur `shm_size: 2gb` de `services/peer/docker-compose.yml`, mais **par room** désormais, pas
  partagée) — une room dont le Chromium headless dérive en consommation mémoire ne peut plus
  faire tomber les autres via un plafond `shm`/mémoire partagé.
- `--rm` : le container est détruit proprement à la fin de vie de la room (`muc-room-destroyed`
  ou éjection modérateur) — pas d'accumulation de containers morts.
- Le crash d'un container (exit code ≠ 0, OOM-killed) est détecté par l'Orchestrateur via
  l'API Docker Events (§4.4) **indépendamment** des autres containers — c'est une garantie du
  noyau Linux (cgroups, namespaces), pas du code applicatif.

### 3.2 Alternative documentée (non retenue par défaut) : sous-process au sein d'un même container hôte

`multiprocessing`/`subprocess.Popen` lançant `python -m app.main` par room, dans un même
container "hôte des agents". Plus rapide à démarrer, mais isolation plus faible : partage du
même filesystem, du même OOM-killer de cgroup si les sous-process ne sont pas eux-mêmes replacés
dans des cgroups dédiés, et du même binaire Chromium en cache (ce qui est plutôt un avantage,
mais au prix d'un risque de fork-bomb mémoire partagé). **Non retenu par défaut** car le dépôt
est déjà entièrement construit autour de Docker Compose (`civitas-net`, un service = un
container) — l'option container-par-room est la continuité naturelle du modèle de déploiement
existant, pas une rupture. Documentée ici comme repli possible si la latence de démarrage d'un
container (1 à 3 secondes typiquement) s'avère trop pénalisante en usage réel.

### 3.3 Alternative future (hors périmètre de ce projet) : Pod Kubernetes par room

Même principe, avec `Deployment`/`Job` Kubernetes à la place de `docker run`. Le contrat
"spawn / route / health / teardown" de l'Orchestrateur (§4) est conçu pour être
**interchangeable** derrière une interface (`app/docker_runtime.py` → `AgentRuntimeProvider`,
§4.3) : passer à Kubernetes plus tard ne change que l'implémentation de ce provider, jamais le
reste de l'Orchestrateur ni des CIVITAS Agents. Non développé dans cette phase — le README du
projet cible explicitement un déploiement mono-serveur (`192.168.1.89`, Docker Compose).

---

## 4. CIVITAS Agent Orchestrator — évolution de `room-spawner`

Nouveau service : `services/civitas-orchestrator/` (remplace `services/room-spawner/`). Conserve
l'intégralité du rôle métier de `room-spawner` ("qui doit avoir un agent actif, où") — seule sa
mécanique de bout de chaîne change (spawn + route au lieu d'un appel HTTP à un service partagé).

### 4.1 Ce qui est repris à l'identique

- Seul consommateur Kafka de `jitsi.room.events` / `jitsi.participant.events`, même pattern de
  consumer group + offset committé après traitement réussi (`enable_auto_commit=False`,
  `auto_offset_reset="earliest"`, backoff exponentiel de reconnexion) — doc 00 §3, code déjà bon.
- Vérification `room-config` (`peer_enabled` → renommé `agent_enabled` en cible, cf. doc 04) avant
  tout spawn.
- Endpoints modérateur manuels : `inject`/`eject`/`standby`/`activate`/`kick`/`mute`/`status`,
  mêmes contrats d'entrée/sortie qu'aujourd'hui (compatibilité CLI, doc 04).
- Idempotence déjà en place (`_active_rooms` comme garde-fou contre un double spawn) — devient
  la table de routage (§4.2), avec la même logique de garde.

### 4.2 Ce qui change : registre de routage au lieu d'un simple `set[str]`

```python
# app/registry.py (civitas-orchestrator)
class AgentHandle(TypedDict):
    room_id: str
    container_name: str           # "civitas-agent-<slug>"
    base_url: str                 # "http://civitas-agent-<slug>:8300"
    started_at: str
    status: str                   # "starting" | "healthy" | "unhealthy" | "stopping"

class AgentRegistry:
    """
    En mémoire (comme _active_rooms aujourd'hui). Une entrée perdue en cas de crash de
    l'Orchestrateur N'EST PAS une perte de données : les agents déjà lancés continuent de
    tourner (containers indépendants), et le prochain démarrage de l'Orchestrateur peut
    reconstruire le registre en interrogeant Docker directement (`docker ps` filtré sur le
    label civitas.agent=true) avant de reprendre la consommation Kafka — cf. §4.5.
    """
```

L'Orchestrateur lui-même reste **un seul process** (comme `room-spawner` aujourd'hui) — ce n'est
**pas** un problème d'isolation au même titre que l'ex-`peer`, car :
1. Il ne porte aucun état de raisonnement (pas de `ConferenceAgentState`, pas de session Gemini,
   pas de navigateur headless) — juste une table `room_id → container/URL`.
2. Un crash de l'Orchestrateur **n'arrête aucun agent déjà lancé** (containers indépendants,
   `--rm` déclenché uniquement par un `docker stop` explicite de l'Orchestrateur, jamais par la
   mort de l'Orchestrateur lui-même).
3. Au redémarrage, le registre est reconstruit (§4.5) et la consommation Kafka reprend au dernier
   offset committé (rattrapage at-least-once déjà en place).

### 4.3 Interface de spawn — remplaçable (Docker aujourd'hui, k8s demain)

```python
# app/docker_runtime.py
class AgentRuntimeProvider(Protocol):
    async def spawn(self, room_id: str, env: dict[str, str]) -> AgentHandle: ...
    async def teardown(self, handle: AgentHandle) -> None: ...
    async def is_healthy(self, handle: AgentHandle) -> bool: ...
    async def list_running(self) -> list[AgentHandle]: ...     # reconstruction du registre, §4.5

class DockerAgentRuntimeProvider:
    """
    Implémentation par défaut — via le SDK Python `docker` (docker.from_env()).
    spawn() : docker run --rm -d --network civitas-net --name civitas-agent-<slug>
              -e ROOM_ID=<room_id> -e ... --shm-size=2g --memory=<limite>
              civitas-agent-runtime:latest
    teardown() : appel à /shutdown sur l'agent (arrêt propre : au revoir chat, fermeture
                 navigateur, checkpoint final) avec timeout, puis `docker stop` en repli si le
                 timeout expire.
    is_healthy() : GET {base_url}/health (doc 01 §8.1) — complété par l'écoute des Docker
                   Events (§4.4) pour une détection immédiate des morts brutales (OOM, crash).
    """
```

### 4.4 Détection de crash — immédiate, par room, sans polling agressif

L'Orchestrateur s'abonne au flux d'événements Docker (`docker events --filter
label=civitas.agent=true`) plutôt que de ne faire que du polling HTTP périodique : un
`OOMKilled` ou un `die` sur `civitas-agent-<slug>` est reçu en quasi temps réel, déclenche :

1. Marquage de l'entrée `AgentRegistry` correspondante en `unhealthy`.
2. Politique de redémarrage **avec backoff, appliquée à cette room uniquement**, sur le modèle
   déjà présent dans `kafka_consumer.py` (backoff exponentiel, plafonné) — pas de tempête de
   redémarrage si une room est réellement cassée (config invalide, boucle d'erreur Gemini…).
3. Aucune autre entrée du registre n'est touchée — la boucle de traitement des Docker Events est
   strictement scopée par `container_name`/label, donc par `room_id`.

### 4.5 Reconstruction du registre au démarrage de l'Orchestrateur

```
au démarrage de civitas-orchestrator :
  1. docker ps --filter "label=civitas.agent=true" --filter "status=running"
  2. pour chaque container trouvé → reconstruire une AgentHandle (room_id lu depuis le label
     civitas.room_id, posé au spawn) → réinsérer dans AgentRegistry avec status="healthy"
     (à confirmer par un /health immédiat)
  3. reprendre la consommation Kafka au dernier offset committé
```

Ce mécanisme garantit qu'un redémarrage de l'Orchestrateur (déploiement, mise à jour) ne perd
**aucun** agent déjà actif — cohérent avec le principe "l'Orchestrateur ne porte pas d'état
critique, les agents si, et les agents survivent à l'Orchestrateur".

### 4.6 Forward des événements Control Plane vers l'agent concerné

```python
# app/forwarder.py
async def on_kafka_event(event: dict):
    room_id = event.get("room_id")
    handle = registry.get(room_id)
    if not handle:
        return  # aucun agent actif pour cette room — rien à faire (comportement déjà présent)
    await agent_client.post(f"{handle['base_url']}/control/event", json=event)
```

Simple, explicite, testable unitairement — un événement Kafka pour la room A n'est **jamais**
transmis physiquement au process de la room B (pas de topic partagé lu par l'agent lui-même,
contrairement à un design où chaque agent aurait son propre consumer group sur le topic global,
qui aurait nécessité un filtrage applicatif — ici le filtrage est fait une seule fois, en amont,
par l'Orchestrateur, avant même que l'information n'atteigne le process de l'agent).

---

## 5. Schéma complet

```
                         Kafka (jitsi.room.events, jitsi.participant.events)
                                          │
                                          │  UN SEUL consumer group
                                          ▼
                         ┌───────────────────────────────────┐
                         │   CIVITAS Agent Orchestrator       │
                         │   (process unique, sans état       │
                         │    de raisonnement — juste un      │
                         │    registre room_id → container)   │
                         └───────────┬─────────────┬──────────┘
                                     │             │
                     spawn/teardown  │             │  forward HTTP (control/event)
                     (Docker SDK)    │             │  scopé strictement par room_id
                                     ▼             ▼
     ┌───────────────────────────────────────────────────────────────────────┐
     │  civitas-net (réseau Docker)                                          │
     │                                                                       │
     │   ┌─────────────────────┐   ┌─────────────────────┐   ┌─────────────┐│
     │   │ civitas-agent-salle-a│   │ civitas-agent-salle-b│   │     ...     ││
     │   │ (container isolé)    │   │ (container isolé)    │   │             ││
     │   │ ROOM_ID=salle-a       │   │ ROOM_ID=salle-b       │   │             ││
     │   │ shm_size dédié        │   │ shm_size dédié        │   │             ││
     │   │ mémoire dédiée        │   │ mémoire dédiée        │   │             ││
     │   │ 1 seul thread graphe  │   │ 1 seul thread graphe  │   │             ││
     │   │ = 1 seul room_id      │   │ = 1 seul room_id      │   │             ││
     │   └─────────────────────┘   └─────────────────────┘   └─────────────┘│
     │        ▲ un crash ici ne peut PAS se propager vers les autres        │
     └───────────────────────────────────────────────────────────────────────┘
```

---

## 6. Vérification de l'exigence, point par point

| Exigence formulée | Mécanisme qui la garantit |
|---|---|
| "chacun assume complètement tout ce qui concerne son processus dans une room" | `ROOM_ID` fixé au process, jamais réassigné (§2) |
| "les contexts, états, mémoire… tout doit être bien défini" | `ConferenceAgentState` scopé par construction (doc 01 §5), mémoire à 3 niveaux tous scopés `room_id`/`thread_id` (doc 01 §7) |
| "si un CIVITAS Agent plante dans une room, ça ne doit pas affecter les autres" | isolation container Docker par room, cgroups indépendants, détection de crash scopée (§3, §4.4) |
| "instances de CIVITAS Agent complètement isolées" | garantie structurelle (state) **+** garantie d'exécution (process/container OS) — les deux niveaux sont nécessaires et sont couverts |

---

## 7. Ce qui reste volontairement partagé (et pourquoi ce n'est pas un problème d'isolation)

Pour éviter toute ambiguïté : certains composants restent des instances **uniques**, partagées
par toutes les rooms — ce n'est pas un oubli, c'est un choix cohérent avec la nature de ces
composants (doc 00 §5.1 le justifie déjà pour `event-bridge`/`room-spawner`) :

- **Kafka, Postgres, Redis, Qdrant, MinIO** (domaine 4, "CIVITAS Platform") — ce sont des
  *données au repos* ou des *bus de messages*, pas du *raisonnement en cours d'exécution*. Leur
  disponibilité est un sujet de robustesse infra (réplication, sauvegardes) — **distinct** du
  sujet traité ici (isolation du raisonnement/crash-domain par room). Toute panne y dégrade
  gracieusement (patterns déjà en place : reconnexion avec backoff, dégradation silencieuse à
  liste vide en cas d'indisponibilité de `room-config`, doc 00 §5.3) sans jamais faire planter
  un agent, et sans que la panne d'une room puisse en provoquer une autre.
- **event-bridge et l'Orchestrateur** — routage et supervision, pas de session IA. Un redémarrage
  y est un incident bref sans perte pour les agents déjà actifs (§4.5).
- **Jitsi lui-même** (Prosody/Jicofo/JVB) — acté, hors périmètre, déjà partagé par construction
  (c'est un serveur de conférence multi-room par nature, pas un composant CIVITAS).

---

## 8. Suite du document

Plan de migration phasé, fichier par fichier, avec ordre de bascule et stratégie de rollback :
[`04-plan-migration.md`](./04-plan-migration.md).
