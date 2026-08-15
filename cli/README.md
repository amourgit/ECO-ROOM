# `civitas` — CLI de pilotage CIVITAS

Outil en ligne de commande pour piloter rooms, peers et modération —
couvre exactement le cycle de vie documenté dans
[`DOCUMENTATION_API.md` §0](../DOCUMENTATION_API.md#0-cycle-de-vie-complet-dun-peer-dans-une-room).

**Zéro dépendance externe** (stdlib Python uniquement — `urllib`,
`argparse`, `json`) : fonctionne avec n'importe quel Python ≥ 3.9, sans
rien installer.

## Installation

Aucune — c'est un script exécutable autonome.

```bash
chmod +x cli/civitas
./cli/civitas --help

# Ou, pour l'utiliser depuis n'importe où :
sudo ln -s /opt/civitas/cli/civitas /usr/local/bin/civitas
civitas --help
```

## Configuration

Trois façons de configurer hôtes/tokens, par ordre de priorité
décroissante :

1. **Options en ligne de commande** — `--host`, `--room-config-url`,
   `--token`, `--webhook-secret`, etc. (reconnues avant OU après la
   sous-commande : `civitas --host X room get id` et
   `civitas room get id --host X` fonctionnent tous les deux)
2. **Variables d'environnement** — `CIVITAS_HOST`,
   `CIVITAS_ROOM_CONFIG_TOKEN`, `CIVITAS_PEER_TOKEN`,
   `CIVITAS_WEBHOOK_SECRET`, etc.
3. **Fichier de config** — `~/.civitas.env` ou `/opt/civitas/cli/.env`
   (format `KEY=VALUE`, une entrée par ligne) :
   ```
   HOST=192.168.1.89
   WEBHOOK_SECRET=le-vrai-secret-genere-par-openssl
   ```
4. **Défauts intégrés** — `localhost`, ports et tokens standards issus
   des `.env.example` du dépôt.

Voir la configuration effective à tout moment :
```bash
civitas config
```

## Exemples

```bash
# Santé de toute la plateforme
civitas health

# Réserver une room (flux recommandé — cf. DOCUMENTATION_API.md §0/§2)
civitas room reserve reunion-budget-2026 \
  --agent-name CIVITAS-BUDGET \
  --prompt "Tu es CIVITAS-BUDGET, assistant de la réunion budgétaire." \
  --can-moderate --keywords civitas,budget

# Faire rejoindre le peer manuellement (tests — en production, automatique
# dès qu'un humain ouvre la room réelle)
civitas peer inject reunion-budget-2026

# Vérifier
civitas peer active
civitas room get reunion-budget-2026

# Interagir
civitas peer send-text reunion-budget-2026 "Annonce le début de la réunion."
civitas peer send-chat reunion-budget-2026 "📋 Ordre du jour dans le chat."

# Modérer (toujours vérifier le statut réel avant)
civitas peer status reunion-budget-2026
civitas peer mute reunion-budget-2026 a1b2c3d4
civitas peer kick reunion-budget-2026 a1b2c3d4 --reason "Hors sujet répété"

# Éjecter / réactiver
civitas peer eject reunion-budget-2026
civitas peer activate reunion-budget-2026

# Sortie JSON brute pour scripting (jq, etc.)
civitas room list --raw | jq '.[] | select(.status == "pending")'
```

## Toutes les commandes

```
civitas config                                     Config résolue (URLs, tokens masqués)
civitas health                                      État de tous les services

civitas room reserve ROOM_ID [options...]           Réserver (recommandé)
civitas room create ROOM_ID [options...]            Créer directement (legacy)
civitas room get ROOM_ID
civitas room list [--skip N] [--limit N]
civitas room update ROOM_ID [options...]
civitas room delete ROOM_ID
civitas room context ROOM_ID                        Contexte agent (confirme pending->confirmed)
civitas room history ROOM_ID [--limit N]

civitas peer inject ROOM_ID
civitas peer eject ROOM_ID
civitas peer standby ROOM_ID
civitas peer activate ROOM_ID
civitas peer active                                 Rooms où un peer est actif
civitas peer instances                               Instances peer (vue directe)
civitas peer status ROOM_ID                          État modérateur réel
civitas peer kick ROOM_ID PARTICIPANT_ID [--reason]
civitas peer mute ROOM_ID PARTICIPANT_ID
civitas peer send-text ROOM_ID TEXT
civitas peer send-chat ROOM_ID TEXT

civitas webhook room-created ROOM_ID                 Simulation (dev/test)
civitas webhook room-destroyed ROOM_ID
civitas webhook participant-joined ROOM_ID --jid ... [--nick] [--role] [--affiliation]
civitas webhook participant-left ROOM_ID --jid ...
civitas webhook rooms                                État vu par event-bridge
civitas webhook room ROOM_ID

civitas kafka topics                                 (nécessite docker local)
civitas kafka consume TOPIC [--from-beginning] [--max-messages N]
```

Options communes à `room reserve` / `room create` / `room update` :
`--agent-name`, `--prompt`, `--behavior-mode {on_call,proactive,silent}`,
`--language`, `--can-speak/--no-can-speak`,
`--can-write-chat/--no-can-write-chat`,
`--can-use-tools/--no-can-use-tools`, `--can-use-rag/--no-can-use-rag`,
`--can-moderate/--no-can-moderate`, `--peer-enabled/--no-peer-enabled`,
`--active/--no-active`, `--keywords a,b,c`, `--tools a,b,c`,
`--extra-config '{"json": "libre"}'`.

`--help` est disponible à chaque niveau : `civitas --help`,
`civitas room --help`, `civitas room reserve --help`, etc.

## Notes

- `civitas peer kick`/`mute` pilotent la **vraie** room Jitsi (mêmes API
  `JitsiConference` que l'interface Jitsi elle-même) — pas une
  simulation. Elles n'ont d'effet que si le peer a le rôle `moderator`
  dans la room au moment de l'appel (`civitas peer status` le confirme
  avant d'agir). Cf. `PLAN_SYNCHRONISATION_ROOMS_JITSI.md` §8.9.
- `civitas webhook *` sert à simuler des événements Prosody pour tester
  sans navigateur réel — nécessite `--webhook-secret`/`CIVITAS_WEBHOOK_SECRET`
  (doit correspondre à `muc_webhook_secret` côté Prosody).
- `civitas kafka *` exécute `docker exec civitas-kafka ...` — nécessite
  que la CLI tourne sur une machine avec accès Docker au conteneur Kafka
  (typiquement directement sur le serveur CIVITAS).
