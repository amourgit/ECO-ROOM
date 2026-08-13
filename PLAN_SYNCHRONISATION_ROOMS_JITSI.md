# Plan de correction — Synchronisation rooms CIVITAS ↔ Jitsi

**Statut global :** 🟡 En cours — corrections de cohérence appliquées, containerisation Jitsi livrée (non déployée), Phases 1-5 du §5 toujours en attente de ton feu vert détaillé
**Dernière mise à jour :** 2026-08-07
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

### 2.4 — ✅ Traité : signal d'une intégration commencée puis abandonnée

`event-bridge/main.py` déclarait `JICOFO_API = "http://192.168.1.89:8888"` —
jamais utilisée nulle part dans le fichier. En creusant le
`docker-compose.yml` officiel de `jitsi/docker-jitsi-meet` (cf. §7), la
raison apparaît clairement : Jicofo publie son port 8888 en
`127.0.0.1:8888:8888` — **bindé sur le loopback de l'hôte uniquement**,
jamais joignable via l'IP LAN du serveur. Cette variable n'aurait donc
jamais pu fonctionner telle quelle, même utilisée. Supprimée (cf. journal).
Elle deviendra effectivement joignable une fois Jitsi containerisé (§7) —
un conteneur attaché au réseau `meet.jitsi` peut atteindre `jicofo:8888`
en interne, indépendamment de son binding sur l'hôte — mais rien n'indique
que Jicofo expose une réelle API de création/réservation de room au-delà
de la santé/stats (`/about/health`, `/stats`) : à vérifier concrètement une
fois le conteneur en place, avant de bâtir quoi que ce soit dessus.

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

## 7. Containerisation Jitsi — livré, non déployé

Confirmé par toi : Jitsi tourne aujourd'hui en installation native (hors
Docker) sur le serveur. C'est cohérent avec la conception de
`jitsi_boot.sh`/`jitsi_stop.sh` (§8 du README), qui supportait déjà les
deux modes (Docker et systemd) précisément pour cette raison.

### 7.1 — Ce qui a été livré

- **`jitsi/docker-compose.yml`** — *vendored* depuis le projet officiel
  [`jitsi/docker-jitsi-meet`](https://github.com/jitsi/docker-jitsi-meet)
  (web, prosody, jicofo, jvb), **quasiment tel quel**. Une seule
  modification volontaire, marquée explicitement dans le fichier
  ("AJOUT CIVITAS") : un alias réseau `meet.civitas.local` sur le service
  `web`, attaché à `civitas-net` (réseau externe, créé par CIVITAS —
  jamais par ce fichier), pour que `peer` puisse le résoudre nativement via
  le DNS Docker le jour de la bascule. Rien d'autre n'est modifié —
  Jitsi reste la base intacte, CIVITAS s'y raccroche de l'extérieur.
- **`jitsi/.env.example`** — adapté du modèle officiel : domaine et ports
  déjà en place (`meet.civitas.local`, 80/443/10000), stockage hors repo
  (`/opt/civitas/jitsi/data`), image `stable` fixée ici plutôt que dans le
  compose vendored (pour ne garder qu'une seule modification dans ce
  dernier), mots de passe jamais committés.
- **`jitsi/gen-passwords.sh`** — vendored tel quel depuis l'officiel.
- **`jitsi_boot.sh`/`jitsi_stop.sh` (§8 README)** : découverte automatique
  déjà en place (`scripts/lib/jitsi_common.sh` vérifiait déjà
  `/opt/civitas/jitsi` parmi ses chemins candidats). **Complété le
  2026-08-12** (cf. §7.4) : préparation automatique des répertoires
  `${CONFIG}/storage` et `${CONFIG}/tmp` avant le premier démarrage, et
  vérification TCP réelle du port XMPP Prosody (5222) plutôt qu'un simple
  "conteneur actif" — voir §7.4 pour le pourquoi.

### 7.2 — Deux points nécessitant une action manuelle de ta part (je n'ai pas la source)

**a) Certificats TLS** — vérifié dans le code source du conteneur `web`
officiel : s'il trouve `cert.crt`/`cert.key` dans `${CONFIG}/web/keys/`, il
les utilise ; sinon il en génère un self-signed que les clients
n'approuveraient pas. Pour réutiliser le certificat mkcert déjà déployé et
approuvé sur les postes clients (`install_civitas_ca.sh`) :
```bash
mkdir -p /opt/civitas/jitsi/data/web/keys
cp /opt/civitas/certs/civitas.local.crt /opt/civitas/jitsi/data/web/keys/cert.crt
cp /opt/civitas/certs/civitas.local.key /opt/civitas/jitsi/data/web/keys/cert.key
```

**b) Plugin Prosody du webhook vers event-bridge** — `event-bridge`
reçoit aujourd'hui de vrais webhooks Prosody (`POST /webhook`), donc un
module Prosody personnalisé est déjà actif sur l'installation native
actuelle. **Je n'ai pas accès à son code source** (il n'est pas versionné
dans ce repo) — je ne peux donc pas le porter à ta place, et je ne veux
pas en fabriquer un nouveau à l'aveugle en devinant sa logique. Le
conteneur `prosody` officiel prévoit exactement cet usage via un point
d'extension monté en volume :
```bash
# Localiser le module actif sur l'installation native (chemin typique,
# à confirmer chez toi) :
ls /etc/prosody/prosody-plugins-custom/ 2>/dev/null || find / -iname "*webhook*" -path "*prosody*" 2>/dev/null

# Une fois trouvé, le copier vers l'emplacement monté par le conteneur :
mkdir -p /opt/civitas/jitsi/data/prosody/prosody-plugins-custom
cp <module trouvé> /opt/civitas/jitsi/data/prosody/prosody-plugins-custom/
```
Le module devra pointer vers `http://event-bridge:8100/webhook` (DNS
Docker, une fois `event-bridge` attaché à `meet.jitsi` — cf. 7.3) au lieu
de son URL actuelle.

### 7.3 — Procédure de bascule (à exécuter quand tu es prêt — rien d'automatique)

Je n'ai **pas** modifié `event-bridge/docker-compose.yml` ni
`services/peer/docker-compose.yml` pour les attacher à `meet.jitsi` : ce
réseau n'existe pas tant que `jitsi/docker-compose.yml` n'a jamais tourné,
et un `docker compose up` référençant un réseau externe inexistant échoue
immédiatement — ça aurait cassé ton déploiement natif actuel dès le
prochain `boot.sh`. La bascule reste donc une opération volontaire, phasée :

- [ ] `cd jitsi && cp .env.example .env && ./gen-passwords.sh`
- [ ] Copier les certificats (7.2a) et le plugin Prosody (7.2b)
- [ ] Démarrer via `sudo bash scripts/jitsi_boot.sh` plutôt qu'un
      `docker compose up -d` manuel : depuis le 2026-08-12 (cf. §7.4) le
      script prépare seul `${CONFIG}/storage` et `${CONFIG}/tmp` avec les
      permissions attendues par les conteneurs rootless, **avant** le tout
      premier démarrage — sans quoi Prosody peut refuser de démarrer. Le
      script vérifie ensuite chaque composant, y compris une connexion TCP
      réelle sur le port XMPP (5222), avant de conclure au succès. Tester
      en parallèle de l'installation native (ports différents le temps du
      test, ou fenêtre de maintenance).
- [ ] Ajouter `meet.jitsi: external: true` au réseau de
      `event-bridge/docker-compose.yml` et `services/peer/docker-compose.yml`
      (webhook Prosody -> event-bridge, et navigation Playwright -> `web`
      via l'alias `meet.civitas.local`)
- [ ] Une fois validé : arrêter et désinstaller les paquets natifs
      (`prosody`, `jicofo`, `jitsi-videobridge2`, `nginx` — géré par
      `jitsi_stop.sh` en mode systemd)
- [ ] Retirer `extra_hosts` de `services/peer/docker-compose.yml` (devenu
      inutile, résolution via l'alias Docker désormais)

### 7.4 — Diagnostic XMPP Prosody/Jicofo/JVB et correctifs (2026-08-12)

Un test réel de `docker compose up -d` sur `jitsi/` (première tentative de
bascule) a produit un rapport de diagnostic détaillé sur la communication
XMPP entre Prosody, Jicofo et JVB. Vérification, point par point, contre le
dépôt et la doc officielle (`jitsi.github.io/handbook`) :

**Confirmé exact** — noms de domaines XMPP (`xmpp.meet.jitsi`,
`auth.meet.jitsi`, `muc.meet.jitsi`, `internal-muc.meet.jitsi`), résolution
DNS Docker, cohérence des secrets `JICOFO_AUTH_PASSWORD`/`JVB_AUTH_PASSWORD`
entre Prosody et ses clients, génération de `/run/{jvb,jicofo}/config/*` à
partir des templates : tout est conforme à `jitsi/docker-compose.yml`
(vendored) et à `jitsi/.env.example`. `/config` vide dans les trois
conteneurs est normal (lecture seule, rendu vers `/run/<service>/config` au
démarrage) — ce n'est pas un bug.

**Non prouvé par le rapport, et cause la plus probable** — le rapport
s'arrêtait sur "le port TCP 5222 n'a pas pu être testé (`nc` absent des
images)". Aucun `mkdir`/`chmod` des répertoires `${CONFIG}/storage/*` et
`${CONFIG}/tmp/*` n'existait nulle part dans ce dépôt (ni dans
`jitsi_boot.sh`, ni dans la checklist 7.3). Or, depuis la release
`stable-11146` de `docker-jitsi-meet`, les conteneurs tournent en rootless
(uid/gid 1000) avec filesystem en lecture seule ; **seuls** `storage/` et
`tmp/` sont inscriptibles, et **doivent être créés et rendus inscriptibles
avant** le premier démarrage — sinon Docker les crée lui-même en
`root:root`, et le service concerné (Prosody en tout premier lieu, à cause
de `${CONFIG}/storage/prosody`) refuse de démarrer avec une erreur
explicite. C'est exactement le scénario qui expliquerait "tout est
configuré correctement, mais la connexion XMPP n'est jamais prouvée" :
Prosody ne serait tout simplement jamais réellement à l'écoute sur 5222.
Référence :
https://jitsi.github.io/handbook/docs/devops-guide/devops-guide-docker#rootless-and-read-only-containers

**Bug distinct, confirmé et corrigé** — le reverse-proxy nginx CIVITAS
(`nginx/conf.d/meet.civitas.local.conf`) termine le TLS et reverse-proxy en
clair vers `web:8000`, mais `DISABLE_HTTPS` n'était jamais positionné : par
défaut, le conteneur `web` redirige lui-même tout son trafic HTTP interne
vers son propre HTTPS (certificat auto-signé), ce qui casse la chaîne
nginx → web. Comportement documenté pour tout déploiement derrière un
reverse-proxy TLS :
https://jitsi.github.io/handbook/docs/devops-guide/devops-guide-docker#disable-https

**Mise à jour du 2026-08-12 (suite) — confirmation terrain :** un `ss -ltn`
exécuté directement dans le conteneur `prosody` a confirmé l'hypothèse
ci-dessus : aucun listener sur 5222. `scripts/lib/jitsi_common.sh` a été
complété en conséquence — `check_prosody_xmpp_port` (test TCP one-shot
immédiatement après `docker compose up -d`) est remplacée par
`ensure_jitsi_docker_config_dirs` (prépare `storage/`/`tmp/` en
`chmod 777`, idempotent), `wait_for_prosody_listening` (poll `ss -ltn`
*dans* le conteneur Prosody, avec timeout — un test one-shot immédiat
produisait de faux négatifs le temps que Prosody termine son init) et
`check_prosody_reachable_from_jicofo` (preuve de bout en bout via
`/dev/tcp`, `nc` étant absent des images). `jitsi_boot.sh` n'attend plus
JVB (jusqu'à 3 min) si Prosody n'est pas déjà confirmé à l'écoute, et
imprime `ss -ltn` + les 30 dernières lignes de logs Prosody en cas
d'échec pour aller droit à la cause.

Aucun secret ni template Jitsi n'a été modifié — conformément au
diagnostic initial, ce n'était pas là que se trouvait le problème.

### 7.5 — SASLError "not-authorized" après le premier `docker compose up -d` réel (2026-08-12)

Le premier démarrage réel avec les correctifs de 7.4 a **confirmé leur
efficacité** : `scripts/jitsi_boot.sh` a créé/chmod les répertoires
`storage/`+`tmp/`, `docker compose up -d` a réussi, Prosody a été confirmé
à l'écoute sur 5222 (`ss -ltn`), joignable depuis Jicofo. Mais les logs
réels ont révélé un problème **suivant**, jusque-là masqué par l'échec plus
en amont :

```
Jicofo : SASLError using SCRAM-SHA-1: not-authorized (en boucle)
JVB    : SASLError using SCRAM-SHA-1: not-authorized (en boucle, sur son
         MucClient vers xmpp.meet.jitsi)
```

Le port est ouvert, la configuration (domaines, secrets déclarés dans
`.env`) est cohérente — mais l'authentification XMPP échoue quand même.
**Cause connue et documentée par la communauté Jitsi**, pas spécifique à
CIVITAS : Prosody enregistre les comptes internes (`jicofo`, `jvb`, ...)
**une seule fois**, dans son stockage persistant
(`${CONFIG}/storage/prosody`). Si ce stockage contient déjà des comptes
créés avec d'anciens mots de passe (`./gen-passwords.sh` relancé après un
premier essai, ou `${CONFIG}` réutilisé d'une tentative Docker antérieure —
précisément le cas ici, cf. le tout premier rapport de ce diagnostic qui
inspectait déjà des conteneurs `jitsi-prosody-1` réels), Prosody **ne met
jamais à jour** le mot de passe stocké : Jicofo/JVB présentent le nouveau
mot de passe de `.env`, Prosody attend l'ancien → SASL `not-authorized` en
boucle, même avec un TCP grand ouvert. Référence communauté :
https://www.cynkra.com/blog/2020-11-02-jitsi-load-balanced/ ("Do not run
gen-passwords.sh multiple times... you need to delete all config folders
before running docker-compose up again").

**Remédiation immédiate (à exécuter sur le serveur) :**
```bash
sudo bash scripts/jitsi_reset_prosody.sh
```
Purge uniquement `${CONFIG}/storage/prosody` (comptes/roster/certs
auto-générés — jamais les certificats web ni la configuration), redémarre
Prosody seul ; Jicofo/JVB, déjà en boucle de reconnexion active, se
réauthentifient automatiquement avec les mots de passe **actuels** de
`.env` sans qu'il soit nécessaire de les redémarrer.

**Correctifs de fond apportés (pour que cette classe d'échec soit
détectée automatiquement à l'avenir, au lieu d'un faux "succès") :**
- `jitsi/.env.example` : `JICOFO_ENABLE_HEALTH_CHECKS=1` — sans cette
  variable (désactivée par défaut), Jicofo n'expose aucun moyen de
  prouver qu'il est réellement authentifié.
- `scripts/lib/jitsi_common.sh` : `reset_prosody_account_storage()`,
  utilisée par le nouveau script ci-dessous.
- `scripts/jitsi_reset_prosody.sh` (nouveau) : réinitialisation ciblée,
  avec confirmation (`--yes` pour l'automatiser), qui ne touche que le
  stockage des comptes Prosody.
- `scripts/jitsi_boot.sh` : le check Jicofo interroge désormais
  `http://localhost:8888/about/health` (poll, jusqu'à ce que Jicofo
  rejoigne réellement une conférence test — donc s'authentifie) au lieu
  de se contenter d'un "conteneur actif". **Constat important, documenté
  en commentaire dans le script** : le `/about/health` de JVB, lui,
  répondait déjà 200 alors que son propre SASL échouait encore en
  arrière-plan — ce n'est donc pas une preuve d'authentification à lui
  seul, contrairement à celui de Jicofo (qui tente de rejoindre une
  conférence pour répondre). D'où le choix de fiabiliser spécifiquement
  le check Jicofo plutôt que celui de JVB.

**Mise à jour du 2026-08-12 (re-test) — le problème est réapparu à
l'identique** (logs `jitsi/logs.txt`/`jitsi/console.txt` versés au dépôt) :
Jicofo/JVB toujours en SASL `not-authorized`, et côté navigateur la requête
XMPP de création de conférence vers `focus.meet.jitsi` échoue en
`service-unavailable` — preuve directe, côté utilisateur, que Jicofo
n'existe tout simplement pas en tant que composant XMPP aux yeux de
Prosody (il n'a jamais réussi à s'y authentifier). C'est la cause exacte
de "impossible de rejoindre une réunion créée soi-même" : le navigateur se
connecte bien à Prosody (compte anonyme), mais personne ne répond côté
Jicofo pour créer la conférence.

Plutôt que de compter sur l'exécution manuelle de `jitsi_reset_prosody.sh`
à chaque fois que `.env` change, une **auto-résynchronisation** a été
ajoutée : `sync_prosody_accounts_with_env()` calcule une empreinte
(SHA-256) de `JICOFO_AUTH_PASSWORD`+`JVB_AUTH_PASSWORD`, la compare à
celle enregistrée lors du dernier démarrage réussi (fichier caché dans
`${CONFIG}/storage/prosody`, donc persistant avec les comptes), et purge
automatiquement le stockage Prosody **avant** `docker compose up -d` si
elles diffèrent — sans purger à chaud si Prosody tournait déjà. Appelée
systématiquement par `jitsi_boot.sh`. Testée unitairement (création,
non-purge si identique, purge si différent, empreinte mise à jour).
Seul cas encore manuel : la toute première exécution sur un stockage déjà
ancien (aucune empreinte de référence) — d'où la nécessité de lancer
`jitsi_reset_prosody.sh` une dernière fois pour "amorcer" le mécanisme.

### 7.6 — `jitsi_reset_prosody.sh` exécuté : SASL résolu, mais faux négatif dans la vérification (2026-08-13)

Exécution de `sudo bash scripts/jitsi_reset_prosody.sh` sur le serveur.
Les logs Prosody réels (`docker compose logs prosody`) confirment un
**succès complet** : les 4 comptes internes ont été recréés
(`focus@auth.meet.jitsi`, `jvb@auth.meet.jitsi`, `jibri@auth.meet.jitsi`,
`jigasi@auth.meet.jitsi`), et surtout — preuve directe que le problème du
§7.5 est résolu — le log montre explicitement :
```
Authenticated as jvb@auth.meet.jitsi [prosody:operator]
Authenticated as focus@auth.meet.jitsi [prosody:operator]
```
Jicofo et JVB se sont réauthentifiés avec succès.

Le script a pourtant affiché `[✗] Prosody ne s'est pas remis à écouter` —
un **faux négatif dans la vérification elle-même**, pas dans Prosody. Cause
identifiée : `wait_for_prosody_listening()` s'appuyait sur `ss -ltn`
exécuté via `docker compose exec -T prosody` (non-interactif). Ce mode
d'exécution semble résoudre `$PATH` différemment du shell interactif dans
lequel `ss` avait été testé manuellement plus tôt (`ss` vit sous
`/usr/sbin` sur Debian, pas systématiquement dans le `$PATH` par défaut
hors shell de login) — le binaire n'était probablement simplement pas
trouvé, produisant une sortie vide plutôt qu'une erreur visible.

**Correctif** : `wait_for_prosody_listening()` et `prosody_listen_diagnose()`
n'utilisent plus `ss` pour la décision succès/échec — remplacé par un test
de connexion TCP en loopack (`127.0.0.1:5222`) via `/dev/tcp` (builtin
bash, sans dépendance à un binaire externe ni à son `$PATH`), la même
méthode déjà utilisée avec succès pour `check_prosody_reachable_from_jicofo`.
Validé par un test unitaire (port ouvert détecté / port fermé rejeté,
sans faux positif ni faux négatif). `ss -ltn` reste affiché en best-effort
dans `prosody_listen_diagnose()` à titre purement informatif, plus jamais
comme critère de décision.

**Conclusion à ce stade : la chaîne d'authentification XMPP
Prosody↔Jicofo↔JVB fonctionne.** Reste à confirmer côté navigateur qu'une
réunion peut réellement être créée et rejointe de bout en bout (cf. §3 du
guide de démarrage).

---

## Journal des mises à jour

- **2026-07-31** — Diagnostic initial complet, plan phasé créé. Aucun code
  modifié à ce stade — en attente de validation du diagnostic et des
  réponses au §6 avant de démarrer la Phase 0.
- **2026-08-07** — Diagnostic et philosophie validés par toi. Deux chantiers
  distincts lancés en parallèle du plan Phases 1-5 (toujours en attente) :
  - Cohérence des variables d'environnement : suppression de toutes les IP
    en dur restantes trouvées (`JICOFO_API` event-bridge, listener Kafka
    externe, `extra_hosts` peer, cible Prometheus jitsi-videobridge,
    `config/civitas.env` tracké) au profit d'une résolution dynamique
    unique via `config/civitas.env`, exportée par `boot.sh` avant tout
    `docker compose`. `event-bridge` aligné sur le pattern
    pydantic-settings + `.env` déjà en place partout ailleurs.
  - Containerisation Jitsi (§7) : `jitsi/docker-compose.yml` vendored
    depuis l'officiel + adaptation CIVITAS, livré mais **non déployé** —
    bascule volontaire, procédure documentée en 7.3, deux étapes
    nécessitant une action manuelle (certificats, plugin Prosody existant
    que je n'ai pas pu porter faute d'accès à son code source).
- **2026-08-12** — Premier test réel de démarrage du stack Docker : rapport
  de diagnostic XMPP Prosody/Jicofo/JVB vérifié point par point contre le
  dépôt et la doc officielle Jitsi. Deux correctifs apportés (préparation
  des répertoires `${CONFIG}/storage`+`tmp` requise par les conteneurs
  rootless, `DISABLE_HTTPS=1` pour la chaîne nginx → web) plus une
  vérification TCP réelle du port XMPP ajoutée à `jitsi_boot.sh`. Détail
  complet en §7.4.
- **2026-08-12 (suite)** — Premier `docker compose up -d` réel avec les
  correctifs de 7.4 : succès (Prosody à l'écoute, confirmé). A révélé un
  problème suivant, jusque-là masqué : SASLError "not-authorized" sur
  Jicofo et JVB — comptes XMPP Prosody désynchronisés du `.env` actuel
  (cause connue, documentée par la communauté Jitsi). Script de
  remédiation ciblée ajouté (`jitsi_reset_prosody.sh`), et le check Jicofo
  de `jitsi_boot.sh` vérifie désormais une vraie preuve d'authentification
  (health-check REST) plutôt qu'un "conteneur actif". Détail complet en
  §7.5.
