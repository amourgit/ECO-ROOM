# Plan de correction — Synchronisation rooms CIVITAS ↔ Jitsi

**Statut global :** 🔴 Analyse terminée — en attente de validation avant implémentation
**Dernière mise à jour :** 2026-07-31
**Portée :** `services/room-config`, `services/room-spawner`, `event-bridge`, (futur) interface de gestion des rooms

> Ce document est fait pour être mis à jour au fil des sessions : cocher les
> cases au fur et à mesure, ajouter des constats, ajuster les phases. Ne pas
> le considérer comme figé.

---

## 1. Résumé exécutif

Le diagnostic confirme le constat : **il n'existe aujourd'hui aucune garantie
qu'une "room" côté CIVITAS (`room_configs`) corresponde à une room réelle
côté Jitsi.** Ce n'est pas un détail d'implémentation isolé — c'est une
absence de contrat architectural. `room_id` est une simple chaîne de
caractères libre, répétée dans plusieurs tables/services, sans jamais être
validée contre la réalité de Jitsi. Deux dérives sont possibles dans les
deux sens, et j'ai trouvé des mécanismes concrets dans le code expliquant
chacune d'elles (détail en §2) :

- **CIVITAS peut "inventer" une room qui n'existe pas dans Jitsi** — un
  endpoint existant permet de créer une config avec n'importe quel `room_id`.
- **Jitsi peut créer une vraie room que CIVITAS ne verra jamais** — la chaîne
  webhook → Kafka → room-spawner a deux points de perte silencieuse
  identifiés dans le code.

La philosophie que tu décris (Jitsi = source de vérité pour l'existence de
la room ; CIVITAS = extension pure, jamais une deuxième création) est la
bonne architecture. Le reste de ce document détaille où le code actuel s'en
écarte, et un plan phasé pour y revenir sans casser ce qui fonctionne.

---

## 2. Diagnostic — état actuel, avec preuves précises

### 2.1 — Une room CIVITAS peut exister sans room Jitsi réelle

`POST /rooms/` dans `services/room-config/app/routers/rooms.py` (ligne 87)
accepte un `RoomConfigCreate` (`services/room-config/app/schemas/room_config.py`)
où `room_id` est une simple chaîne fournie par l'appelant — **aucune
vérification que cette room existe réellement dans Jitsi.** N'importe qui
possédant le token peut créer une "room" CIVITAS fantôme.

`room_configs.room_id` (`services/room-config/app/models/room_config.py`,
ligne 10) est une clé primaire `String(255)` nue : aucune colonne ne
distingue "créée parce qu'un vrai événement Jitsi est arrivé" de "créée
manuellement par appel API", aucune trace de la donnée Jitsi source (JID
complet, domaine MUC, timestamp de confirmation).

### 2.2 — Une room Jitsi réelle peut ne jamais être vue par CIVITAS

Deux pertes silencieuses identifiées dans la chaîne
`Prosody → event-bridge → Kafka → room-spawner` :

**a) Webhook Prosody → event-bridge : fire-and-forget, sans retry.**
`event-bridge/main.py` (`POST /webhook`) reçoit le webhook Prosody et publie
sur Kafka. Si `event-bridge` est indisponible à l'instant exact où Prosody
envoie `muc-room-created`, l'événement est perdu — rien ne le retente côté
Prosody (comportement standard des modules webhook Prosody), rien ne le
retente côté CIVITAS puisque l'événement n'a jamais atteint Kafka.

**b) `auto_offset_reset="latest"` dans room-spawner — un nouveau
redémarrage rate tout ce qui a été manqué.**
`services/room-spawner/app/kafka_consumer.py` (ligne 13) : le consumer
group `civitas-room-spawner` utilise `auto_offset_reset="latest"`. Si
room-spawner est indisponible (déploiement, crash, redémarrage) au moment
où un événement `muc-room-created` transite bien par Kafka, il ne le
rattrapera **jamais** à la reconnexion — `latest` signifie "ignore tout ce
qui existe déjà dans le topic, commence à partir de maintenant". Contraste
avec le nouveau consumer d'historique de `room-config`
(`app/kafka/consumer.py`) qui utilise `auto_offset_reset="earliest"`
précisément pour ce genre de garantie.

Combinaison a) + b) : une vraie room Jitsi peut se créer, et CIVITAS n'en
saura jamais rien — jusqu'à ce qu'un autre mécanisme (accès manuel à l'API,
etc.) la touche incidemment.

### 2.3 — Bug adjacent découvert : l'éjection manuelle d'un peer ne "tient" jamais

`services/room-spawner/app/room_config_client.py` :
- `set_peer_enabled()` (ligne 36) écrit dans `extra_config.peer_enabled`.
- `is_peer_enabled()` (ligne 25) lit `permissions.peer_enabled`.

Or `permissions` (construit par `build_agent_context()` côté room-config)
ne contient **jamais** de clé `peer_enabled` — seulement
`can_speak/can_write_chat/can_use_tools/can_use_rag/can_moderate`. Donc
`is_peer_enabled()` retombe systématiquement sur sa valeur par défaut
(`True`), quoi qu'un modérateur ait fait via `POST /moderator/eject`. Ce
n'est pas un problème de synchronisation Jitsi à proprement parler, mais
c'est un symptôme du même mal : deux bouts de code qui parlent de la même
donnée sans contrat partagé explicite. Inclus dans le plan (Phase 5) parce
qu'il touche le même fichier et la même logique de "state du manager".

### 2.4 — Signal d'une intégration commencée puis abandonnée

`event-bridge/main.py` déclare `JICOFO_API = "http://192.168.1.89:8888"`
(ligne 22) — jamais utilisée nulle part dans le fichier. Ça suggère qu'une
intégration directe avec Jicofo (health check et/ou administration) a été
prévue puis jamais branchée. À vérifier en Phase 0 : est-ce que Jicofo
expose quoi que ce soit d'exploitable sur ce port dans le déploiement
actuel (Jicofo expose par défaut un endpoint de santé/stats en HTTP sur les
installations récentes ; je n'ai pas la certitude qu'il expose une réelle
API de création/réservation de room sans vérifier la configuration
effective de ton Jicofo). Cette même IP en dur devra de toute façon être
corrigée (même classe de bug que celle déjà traitée dans les scripts
système).

### 2.5 — Inconnue à lever avant de coder quoi que ce soit

**Je ne sais pas, avec certitude, comment ce déploiement Jitsi crée
réellement une room.** Deux réalités possibles, avec des implications de
conception différentes :

- **Cas A — création implicite (comportement par défaut d'un MUC Prosody) :**
  la room n'existe qu'à partir du moment où quelqu'un (humain ou le peer)
  rejoint effectivement l'adresse MUC. Aucune "création à l'avance" n'est
  possible côté Jitsi lui-même.
- **Cas B — pré-provisioning possible :** un module Prosody/Jicofo
  installé sur ce serveur permet de réserver/créer une room à l'avance via
  une API.

Le §4 propose une architecture qui fonctionne dans les deux cas, mais la
Phase 0 doit trancher lequel s'applique réellement ici — pas question de
deviner et coder à l'aveugle une intégration qui n'existe peut-être pas.

---

## 3. Philosophie cible (reformulée pour validation)

- Jitsi reste **l'unique source de vérité** pour l'existence et l'identité
  d'une room. CIVITAS ne "crée" jamais une room au sens propre.
- Toute donnée CIVITAS relative à une room (`room_configs`,
  `room_history_entries`, futures tables) est une **extension**, toujours
  rattachée à l'identifiant réel de la room Jitsi — jamais une simulation
  parallèle.
- Une donnée CIVITAS ne doit être considérée "confirmée" que lorsqu'elle
  est adossée à une preuve que la room existe réellement côté Jitsi (un
  événement reçu, ou une création déléguée avec succès) — jamais supposée.
- La création "côté CIVITAS" (web ou API du manager) délègue **toujours**
  à Jitsi en premier quand c'est possible (Cas B ci-dessus) ; quand ce
  n'est pas possible (Cas A), elle réserve un état `pending` qui ne devient
  `confirmed` qu'au reçu de l'événement Jitsi réel — jamais l'inverse.
- Jitsi et toute la couche derrière (Prosody/Jicofo/JVB) restent
  **intacts** — CIVITAS s'y adosse, ne le remplace ni ne le duplique.

*(Si cette reformulation ne correspond pas exactement à ce que tu avais en
tête, corrige-la avant qu'on avance — le reste du plan en découle.)*

---

## 4. Architecture cible (schéma de principe)

```
Cas A — création implicite Jitsi (le plus probable par défaut)
────────────────────────────────────────────────────────────────
Manager CIVITAS (web/API)
   │  1. réserve les métadonnées CIVITAS, statut = "pending"
   │     (room_id proposé, config souhaitée — RIEN côté Jitsi pour l'instant)
   ▼
Utilisateur rejoint l'URL Jitsi correspondante
   │  2. Prosody crée réellement la room (comportement MUC standard)
   ▼
Prosody → webhook → event-bridge → Kafka (muc-room-created)
   │  3. room-spawner (ou room-config) reçoit l'événement RÉEL
   ▼
room_configs.status passe "pending" → "confirmed"
   (ou création directe si aucune réservation préalable — cf. §2.1 actuel,
    conservé mais désormais tracé comme "confirmed" dès l'origine)


Cas B — pré-provisioning Jitsi possible (à confirmer Phase 0)
────────────────────────────────────────────────────────────────
Manager CIVITAS (web/API)
   │  1. délègue la création à Jitsi/Prosody/Jicofo D'ABORD
   ▼
Jitsi confirme la création, renvoie l'identifiant réel
   │  2. CIVITAS crée SES données, rattachées à cet identifiant confirmé
   ▼
room_configs.status = "confirmed" dès la création (jamais "pending")
```

Dans les deux cas : **jamais de ligne `room_configs` sans lien vérifiable
vers une room Jitsi réelle, confirmée ou en attente explicite de
confirmation — jamais supposée.**

Changement de schéma envisagé (`room_configs`) :
- `status` : `pending` | `confirmed` (défaut `confirmed` pour compatibilité
  avec le flux actuel réactif, qui reste valide dans le Cas A)
- `jitsi_confirmed_at` : nullable, horodatage de la confirmation réelle
- `source` : `jitsi_event` | `manager_api` | `manager_web` — traçabilité de
  l'origine de la création

---

## 5. Plan de correctifs — phasé, à cocher au fur et à mesure

### Phase 0 — Investigation (bloquante, avant tout code)

- [ ] Vérifier la configuration Prosody réelle du serveur : modules
      chargés (`mod_muc`, présence ou non d'un module de pré-création de
      room), politique `restrict_room_creation`
- [ ] Vérifier ce que sert réellement `http://<host>:8888` côté Jicofo sur
      ce déploiement (santé seule, ou administration/réservation)
- [ ] Confirmer avec toi : Cas A ou Cas B (§2.5) — ou les deux selon le
      contexte d'usage
- [ ] Lister les `room_id` actuellement en base `room_configs` et vérifier
      manuellement, pour chacun, s'il correspond à une room Jitsi ayant
      réellement existé (état des lieux avant correctif — combien de
      "fantômes" existent déjà ?)

### Phase 1 — Verrouiller l'entrée dangereuse existante (risque faible, gain immédiat)

- [ ] `POST /rooms/` (room-config) : ajouter un champ `source` explicite
      dans `RoomConfigCreate`, défaut `manager_api`, pour au moins tracer
      l'origine de chaque ligne existante et future — sans encore bloquer
      la création (rétrocompatible)
- [ ] Ajouter `status`/`jitsi_confirmed_at` au modèle `RoomConfig` (colonnes
      nouvelles avec défauts sûrs — nécessite une vraie migration Alembic
      cette fois, `create_all` ne modifie pas les tables existantes, cf.
      limite déjà rencontrée sur ce projet)
- [ ] Documenter clairement (README) que `POST /rooms/` reste temporaire en
      l'état et sera remplacé Phase 3

### Phase 2 — Fiabiliser la détection des événements Jitsi réels (corrige §2.2)

- [ ] `room-spawner/kafka_consumer.py` : passer `auto_offset_reset` à
      `"earliest"` pour le groupe `civitas-room-spawner`, avec la même
      logique de commit manuel après traitement réussi que le consumer
      d'historique de room-config (déjà en place, à répliquer)
- [ ] `event-bridge` : ajouter un minimum de résilience sur `/webhook`
      (accusé de réception fiable, logs d'échec explicites) — évaluer si
      Prosody permet une forme de retry côté module webhook ; sinon,
      documenter la limite plutôt que la laisser invisible
- [ ] Ajouter un test d'intégration reproduisant le scénario "room-spawner
      redémarre pendant qu'un événement transite" pour vérifier qu'il est
      bien rattrapé après le correctif

### Phase 3 — Nouveau flux de création délégué à Jitsi (cœur de la demande)

- [ ] Implémenter selon la conclusion de la Phase 0 (Cas A ou B, §4)
- [ ] Cas A : endpoint manager "réserver une room" → statut `pending` +
      webhook réel qui confirme → statut `confirmed`
- [ ] Cas B : endpoint manager "créer une room" → délégation Jitsi d'abord
      → confirmation → création CIVITAS avec `status=confirmed` d'emblée
- [ ] Remplacer/déprécier progressivement `POST /rooms/` actuel au profit
      de ce nouveau flux (garder un mode legacy explicite si nécessaire
      pour la transition)
- [ ] Interface web de gestion des rooms : hors périmètre technique de ce
      repo backend à ce stade — à cadrer séparément une fois le flux API
      stabilisé (cf. Questions ouvertes, §6)

### Phase 4 — Visibilité et réconciliation (optionnelle, à discuter)

- [ ] Endpoint de diagnostic : lister les `room_configs` dont le statut
      est `pending` depuis "trop longtemps" (room jamais rejointe)
- [ ] Évaluer l'intérêt d'un job de réconciliation périodique
      (comparer l'état CIVITAS à l'état Jitsi réel si une API de listing
      existe) — seulement si Phase 0 révèle qu'une telle API existe

### Phase 5 — Corriger le bug adjacent `peer_enabled` (§2.3)

- [ ] Faire lire `is_peer_enabled()` depuis `extra_config.peer_enabled`
      (même chemin que l'écriture), ou migrer proprement ce champ dans un
      emplacement dédié et cohérent du modèle `RoomConfig`
- [ ] Ajouter un test couvrant explicitement : éjection manuelle → room
      détruite et recréée → peer ne doit PAS rejoindre automatiquement

---

## 6. Questions ouvertes — à trancher avec toi avant/pendant l'implémentation

1. Cas A ou Cas B (§2.5) sur l'installation Jitsi actuelle — je ne peux pas
   trancher seul sans accès à la configuration Prosody/Jicofo réelle.
2. L'interface web de gestion des rooms mentionnée : un besoin réel à
   court terme, ou l'API du manager suffit pour l'instant ?
3. Pour les `room_configs` déjà en base aujourd'hui sans lien vérifié à une
   room Jitsi réelle (à quantifier en Phase 0) : les marquer `pending`
   rétroactivement, les supprimer, ou les laisser telles quelles avec un
   simple flag "non vérifiée" ?
4. Le job de réconciliation périodique (Phase 4) — vraiment utile pour ton
   usage, ou la garantie apportée par les Phases 1-3 suffit ?

---

## Journal des mises à jour

- **2026-07-31** — Diagnostic initial complet, plan phasé créé. Aucun code
  modifié à ce stade — en attente de validation du diagnostic et des
  réponses au §6 avant de démarrer la Phase 0.
