# Guide complet — Démarrer le stack Jitsi Meet (CIVITAS)

Ce guide part de zéro et couvre tout ce qu'il faut faire, dans l'ordre,
pour que le stack Docker Jitsi Meet (Prosody + Jicofo + JVB + Web + nginx)
démarre et que les réunions fonctionnent réellement — pas seulement que
les conteneurs soient "actifs".

Tout ce qui est décrit ici est déjà présent dans le dépôt `ECO-ROOM`, à
`/opt/civitas`. Ce guide ne fait qu'expliquer comment l'utiliser, dans le
bon ordre, sans rien oublier.

---

## 0. Ce qui bloquait jusqu'ici, en une phrase

Prosody, le serveur XMPP au centre de la stack, n'accepte de mettre à jour
le mot de passe d'un compte interne (`jicofo`, `jvb`) **qu'une seule fois**
— à sa toute première création. Si les mots de passe changent ensuite dans
`.env` (parce que `gen-passwords.sh` est relancé, ou parce que le dossier
de configuration `${CONFIG}` est réutilisé d'un essai précédent) sans
repartir d'un stockage Prosody vide, Jicofo et JVB continuent de présenter
le **nouveau** mot de passe alors que Prosody attend l'**ancien** :
authentification refusée en boucle (`SASLError ... not-authorized`), même
si tout le reste de la configuration est parfaitement cohérent. Résultat
côté utilisateur : le navigateur se connecte bien à Prosody, mais personne
ne répond côté Jicofo pour créer la conférence — impossible de rejoindre
une réunion, même créée soi-même.

Ce guide (§2 et §5) explique comment ne **jamais** retomber dedans. Le
dépôt corrige aussi maintenant ce problème tout seul à chaque démarrage
(`scripts/jitsi_boot.sh`) — mais mieux vaut comprendre pourquoi, pour ne
pas reproduire la cause (relancer `gen-passwords.sh` sans y penser, par
exemple).

---

## 1. Prérequis (normalement déjà en place)

- Docker + Docker Compose v2 installés (`docker compose version`)
- Le réseau Docker `civitas-net` déjà créé par `01_system_base.sh` lors de
  l'installation initiale du serveur :
  ```bash
  docker network ls | grep civitas-net
  ```
  S'il n'existe pas : `sudo bash 01_system_base.sh` (une seule fois, sur un
  serveur neuf).
- Le dépôt cloné à `/opt/civitas` (c'est le cas si tu lis ce guide depuis
  là).
- Le certificat TLS `civitas.local` déjà généré (mkcert) — c'est ce que
  `01_system_base.sh` met en place et que le navigateur du poste client a
  déjà accepté via `install_civitas_ca.sh`.

Si l'un de ces trois points n'est pas fait, tout le reste de ce guide ne
peut pas fonctionner — commence par là.

---

## 2. Première mise en service, étape par étape

### 2.1 — Se placer dans le bon répertoire

```bash
cd /opt/civitas/jitsi
```

Tout ce qui suit (sauf mention contraire) se fait depuis ce répertoire.

### 2.2 — Copier le fichier d'environnement

```bash
cp .env.example .env
```

**Ne jamais committer `.env`** (il est dans `.gitignore` — c'est normal et
volontaire, il contient des secrets).

Ouvre `.env` et vérifie/complète chaque variable. Voici exactement ce que
signifie chacune, et ce qu'il faut en faire :

| Variable | Que faire | Pourquoi |
|---|---|---|
| `CONFIG` | Laisser `/opt/civitas/jitsi/data` (déjà rempli) | C'est le répertoire où Docker va stocker toute la configuration générée et les données persistantes (comptes XMPP, certificats web...). Ne pas le mettre dans le repo Git. |
| `HTTP_PORT` / `HTTPS_PORT` | Laisser `80` / `443` | Sans effet réel ici : c'est le conteneur `nginx` (CIVITAS) qui publie ces ports sur l'hôte, pas `web` directement. Gardés pour référence/cohérence avec la doc officielle. |
| `JVB_PORT` | Laisser `10000` | Port UDP du flux média WebRTC — déjà ouvert dans le pare-feu par `01_system_base.sh`. |
| `TZ` | Laisser la valeur déjà présente (`Africa/Libreville`) ou ajuster si le serveur est ailleurs | Affecte les horodatages dans les logs de tous les conteneurs. |
| `PUBLIC_URL` | Laisser `https://meet.civitas.local` | C'est l'URL que Jitsi Meet utilise en interne (liens de partage, etc.) — doit correspondre au domaine déjà configuré (dnsmasq + certificat mkcert). |
| `DISABLE_HTTPS` | **Laisser `1` — ne jamais retirer** | Le conteneur `nginx` CIVITAS termine déjà le TLS et reverse-proxy en clair vers `web:8000`. Sans cette variable, `web` redirige lui-même son trafic vers son propre HTTPS interne (certificat auto-signé) et casse tout. |
| `JICOFO_ENABLE_HEALTH_CHECKS` | **Laisser `1` — ne jamais retirer** | Sans ça, `scripts/jitsi_boot.sh` ne peut pas prouver que Jicofo est réellement authentifié auprès de Prosody (un simple port TCP ouvert ne le prouve pas — vécu en pratique). |
| `JVB_ADVERTISE_IPS` | Laisser commenté (`#...`) | Utile uniquement si les clients n'arrivent pas à établir la connexion média malgré tout le reste au vert (scénario NAT/cloud) — pas le cas sur un LAN simple. Si besoin un jour : y mettre la même IP que `CIVITAS_IP` (jamais une IP en dur). |
| `JICOFO_AUTH_PASSWORD`, `JVB_AUTH_PASSWORD`, `JIGASI_XMPP_PASSWORD`, `JIGASI_TRANSCRIBER_PASSWORD`, `JIBRI_RECORDER_PASSWORD`, `JIBRI_XMPP_PASSWORD` | **Ne rien taper ici** — laisser vide | Générés automatiquement à l'étape 2.3. Ne jamais les remplir à la main. |
| `RESTART_POLICY` | Laisser `unless-stopped` | Redémarre les conteneurs automatiquement après un crash ou un reboot du serveur, sauf arrêt volontaire. |
| `JITSI_IMAGE_VERSION` | Laisser `stable` | L'image par défaut du fichier vendored est `unstable` (branche de développement) — jamais adaptée à un usage réel. Ne jamais retirer cette ligne. |

En résumé : **le seul champ qui demande une action de ta part ici, c'est
de vérifier que rien n'a été oublié** — tout est déjà pré-rempli avec les
bonnes valeurs par défaut CIVITAS dans `.env.example`. Ne touche à rien
d'autre sans raison précise.

### 2.3 — Générer les mots de passe (une seule fois)

```bash
./gen-passwords.sh
```

Ce script remplit automatiquement dans `.env` :
`JICOFO_AUTH_PASSWORD`, `JVB_AUTH_PASSWORD`, `JIGASI_XMPP_PASSWORD`,
`JIGASI_TRANSCRIBER_PASSWORD`, `JIBRI_RECORDER_PASSWORD`,
`JIBRI_XMPP_PASSWORD`, avec des valeurs aléatoires (`openssl rand -hex 16`).

> ⚠️ **Règle d'or n°1 : ne relance JAMAIS ce script après le premier
> démarrage réussi**, sauf si tu veux vraiment forcer une réinitialisation
> complète (auquel cas, voir §6 "Réinitialisation complète"). C'est
> exactement la cause du problème décrit en §0. Depuis peu, si tu le fais
> quand même, `jitsi_boot.sh` (§2.7) le détecte et se corrige tout seul —
> mais mieux vaut ne pas compter dessus et prendre le bon réflexe.

### 2.4 — Certificat TLS pour le conteneur `web`

```bash
mkdir -p /opt/civitas/jitsi/data/web/keys
cp /opt/civitas/certs/civitas.local.crt /opt/civitas/jitsi/data/web/keys/cert.crt
cp /opt/civitas/certs/civitas.local.key /opt/civitas/jitsi/data/web/keys/cert.key
```

Sans ça, le conteneur `web` génère un certificat auto-signé que les postes
clients n'ont pas approuvé — le navigateur affichera un avertissement de
sécurité (moins critique que `DISABLE_HTTPS`, puisque c'est `nginx`, pas
`web`, qui présente son certificat au navigateur en premier — mais autant
faire les choses proprement).

### 2.5 — (Optionnel à ce stade) Plugin Prosody du webhook vers event-bridge

Si `event-bridge` doit recevoir les événements de salle (création,
présence...) en provenance de Prosody, un module Prosody personnalisé doit
être copié :

```bash
mkdir -p /opt/civitas/jitsi/data/prosody/prosody-plugins-custom
# Copier ici le module webhook trouvé sur l'installation native existante,
# en le faisant pointer vers http://event-bridge:8100/webhook
```

**Ce n'est pas nécessaire pour qu'une réunion vidéo fonctionne** — uniquement
pour que les événements de salle remontent à `event-bridge`. Tu peux
avancer sans, et revenir à cette étape plus tard.

### 2.6 — Vérifier le réseau `civitas-net`

```bash
docker network ls | grep civitas-net
```

Doit déjà exister (§1). Si ce n'est pas le cas, ne continue pas — reviens
au §1.

### 2.7 — Démarrer le stack

**Ne jamais faire `docker compose up -d` à la main directement.** Utilise
toujours :

```bash
sudo bash /opt/civitas/scripts/jitsi_boot.sh
```

Ce script, dans l'ordre :
1. Détecte automatiquement le mode de déploiement (Docker ici).
2. Prépare les répertoires `${CONFIG}/storage` et `${CONFIG}/tmp` avec les
   permissions attendues par les conteneurs (qui tournent en utilisateur
   non-root) — sans ça, Prosody peut refuser de démarrer purement et
   simplement.
3. **Vérifie automatiquement que les mots de passe de `.env` correspondent
   à ceux déjà enregistrés dans Prosody**, et purge/resynchronise tout
   seul si ce n'est pas le cas (le correctif du problème décrit en §0).
4. Lance `docker compose up -d`.
5. Vérifie, dans l'ordre de dépendance réel, que chaque composant
   fonctionne **vraiment** (pas juste "conteneur démarré") :
   - Prosody : écoute confirmée sur le port XMPP (5222), avec attente active
   - Jicofo : health-check REST, qui exige une authentification XMPP
     réussie auprès de Prosody pour répondre — pas seulement un port ouvert
   - JVB : health-check HTTP
   - Web : port HTTPS à l'écoute

### 2.8 — Lire le résultat

Un démarrage réussi ressemble à ceci :

```
[✓] Prosody : conteneur actif
[✓] Prosody : écoute confirmée sur le port XMPP 5222 (ss -ltn)
[✓] Prosody : joignable depuis Jicofo (TCP ouvert de bout en bout)
[✓] Jicofo : conteneur actif
[✓] Jicofo : opérationnel et authentifié auprès de Prosody (HTTP 200)
[✓] JVB prêt (HTTP 200 après Ns)
[✓] Web : port 443 (HTTPS) à l'écoute

[✓] Stack Jitsi opérationnel — Prosody, Jicofo, JVB, Web vérifiés ✓
```

Si un `[✗]` apparaît quelque part, **le script te dit précisément quoi
regarder** (commande exacte à lancer) — va directement au §4 de ce guide.

---

## 3. Vérifier que ça marche *vraiment* (test réel)

Le script ci-dessus prouve que l'infrastructure est saine. La seule vraie
preuve que **les réunions fonctionnent**, c'est d'en créer une :

1. Ouvrir `https://meet.civitas.local/<nom-de-salle-au-hasard>` dans le
   navigateur.
2. Cliquer sur "Rejoindre" / passer l'écran de pré-jonction.
3. **Ça marche si** : la vidéo locale s'affiche et la salle se charge sans
   message d'erreur ni blocage sur l'écran de pré-jonction.
4. **Ça ne marche pas si** : rien ne se passe après avoir cliqué sur
   rejoindre, ou une erreur apparaît. Dans ce cas, ouvre la console du
   navigateur (F12 → Console) et cherche une ligne contenant
   `service-unavailable` ou `focus.meet.jitsi` — c'est le même symptôme
   que celui diagnostiqué en §0. Repasse par `jitsi_boot.sh` (§2.7) : s'il
   annonce tout au vert et que le problème persiste côté navigateur,
   consulte le §4.

---

## 4. En cas d'échec — que regarder, dans l'ordre

### `jitsi_boot.sh` échoue sur Prosody (pas d'écoute sur 5222)

Cause quasi certaine : permissions sur `${CONFIG}/storage/prosody`. Le
script affiche déjà `ss -ltn` + les logs Prosody. Vérifier :

```bash
ls -la /opt/civitas/jitsi/data/storage/prosody
# Doit être inscriptible par tout le monde (chmod 777) — c'est ce que
# jitsi_boot.sh fait automatiquement à chaque démarrage.
```

### `jitsi_boot.sh` échoue sur Jicofo (santé REST KO)

Cause quasi certaine : `SASLError not-authorized` (§0). Vérifier :

```bash
cd /opt/civitas/jitsi && docker compose logs jicofo --tail=50 | grep -i sasl
```

Si tu vois `not-authorized` : lance la réinitialisation ciblée (sûre, ne
touche à rien d'autre que les comptes XMPP internes) :

```bash
sudo bash /opt/civitas/scripts/jitsi_reset_prosody.sh
```

Puis relance `jitsi_boot.sh` pour confirmer.

### Le navigateur affiche `service-unavailable` / `focus.meet.jitsi`

C'est la conséquence directe du point précédent, vue côté client — refaire
le point ci-dessus.

### Erreur 502 / page blanche sur `https://meet.civitas.local`

```bash
cd /opt/civitas/jitsi && docker compose logs civitas-nginx --tail=50
docker compose logs web --tail=50
```

Vérifier que `DISABLE_HTTPS=1` est bien présent dans `.env` (§2.2) — sans
ça, `web` redirige en interne vers son propre HTTPS que `nginx` ne sait
pas suivre.

### Rien ne se passe du tout, aucun conteneur ne démarre

```bash
docker network ls | grep civitas-net    # doit exister
cd /opt/civitas/jitsi && docker compose config    # doit afficher la config sans erreur
```

---

## 5. Règles d'or à ne jamais enfreindre

1. **Ne jamais relancer `gen-passwords.sh`** après le premier démarrage
   réussi, sauf en sachant que ça implique une réinitialisation Prosody
   (§6). `jitsi_boot.sh` s'en remet désormais tout seul, mais autant ne
   pas y être obligé à chaque fois.
2. **Ne jamais lancer `docker compose up -d` à la main** — toujours passer
   par `sudo bash scripts/jitsi_boot.sh`, qui prépare les répertoires et
   resynchronise les comptes avant de démarrer quoi que ce soit.
3. **Ne jamais éditer les fichiers dans `${CONFIG}` (`/opt/civitas/jitsi/data`)
   à la main**, sauf les deux exceptions explicites du §2.4/§2.5
   (certificats, plugin) — tout le reste y est généré automatiquement et
   sera écrasé/ignoré.
4. **Ne jamais committer `.env`** — il est dans `.gitignore`, c'est
   volontaire.
5. **Toujours vérifier via `jitsi_boot.sh`**, jamais seulement via
   `docker ps` — un conteneur "actif" ne prouve rien de son état interne
   réel (vécu en pratique avec Prosody et Jicofo tous les deux).

---

## 6. Arrêter le stack / redémarrer / réinitialisation complète

### Arrêt normal

```bash
sudo bash /opt/civitas/scripts/jitsi_stop.sh
```

### Redémarrage normal (rien n'a changé dans `.env`)

```bash
sudo bash /opt/civitas/scripts/jitsi_boot.sh
```

### Réinitialisation ciblée (comptes XMPP uniquement — cas du §0/§4)

```bash
sudo bash /opt/civitas/scripts/jitsi_reset_prosody.sh
```

Ne touche qu'à `${CONFIG}/storage/prosody` (comptes, roster, certificats
XMPP auto-générés) — jamais aux certificats web ni à la configuration.

### Réinitialisation complète (table rase — perd tout, y compris les
comptes/salles éventuellement configurés)

À utiliser seulement si tu veux repartir d'un état totalement neuf (après
de multiples essais manuels, par exemple) :

```bash
sudo bash /opt/civitas/scripts/jitsi_stop.sh
sudo rm -rf /opt/civitas/jitsi/data
cd /opt/civitas/jitsi
rm -f .env
cp .env.example .env
./gen-passwords.sh
# Refaire §2.4 (certificat) et §2.5 (plugin) si besoin
sudo bash /opt/civitas/scripts/jitsi_boot.sh
```

---

## 7. Référence rapide

```bash
cd /opt/civitas/jitsi

# Première installation
cp .env.example .env            # puis vérifier le tableau du §2.2
./gen-passwords.sh               # UNE SEULE FOIS
mkdir -p data/web/keys
cp /opt/civitas/certs/civitas.local.crt data/web/keys/cert.crt
cp /opt/civitas/certs/civitas.local.key data/web/keys/cert.key

# Démarrage / arrêt (toujours par ces scripts, jamais docker compose à la main)
sudo bash /opt/civitas/scripts/jitsi_boot.sh
sudo bash /opt/civitas/scripts/jitsi_stop.sh

# En cas de SASLError not-authorized (Jicofo/JVB)
sudo bash /opt/civitas/scripts/jitsi_reset_prosody.sh

# Logs utiles
docker compose logs prosody --tail=50
docker compose logs jicofo  --tail=50
docker compose logs jvb     --tail=50
docker compose logs web     --tail=50
docker compose logs civitas-nginx --tail=50
```
