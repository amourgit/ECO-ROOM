#!/bin/bash
set -e

log() {
    echo "[$(date)] $1"
}

err() {
    echo "[$(date)] [ERREUR] $1" >&2
}

# Attend qu'un service réponde HTTP 200 sur son endpoint /health — jamais
# un simple `sleep N` (durée arbitraire, ne prouve rien) : preuve réelle
# que le service a démarré, avec un délai maximal explicite. Même principe
# que scripts/jitsi_boot.sh pour Prosody/Jicofo/JVB — un `docker compose up
# -d` réussi ne prouve que le conteneur a démarré, jamais que le service
# applicatif dedans répond (ex: crash au démarrage si la DB n'est pas
# encore prête, migration en échec...).
wait_for_health() {
    local url=$1 name=$2 timeout=${3:-60}
    local elapsed=0
    log "Attente de $name ($url, max ${timeout}s)..."
    while [ "$elapsed" -lt "$timeout" ]; do
        if curl -sf -o /dev/null "$url" 2>/dev/null; then
            log "$name prêt ✓ (après ${elapsed}s)"
            return 0
        fi
        sleep 2
        elapsed=$((elapsed + 2))
    done
    err "$name non disponible après ${timeout}s ($url)"
    return 1
}

log "Démarrage Civitas..."

# Charge les variables globales (CIVITAS_IP, CIVITAS_SUBNET, CIVITAS_DOMAIN...)
# générées par 01_system_base.sh, et les exporte pour que ${CIVITAS_IP} soit
# résolu par Docker Compose dans les fichiers qui l'utilisent
# (kafka/docker-compose.yml, services/peer/docker-compose.yml...) — jamais
# d'IP codée en dur dans le code, toujours une résolution dynamique depuis
# ce fichier unique.
CIVITAS_ENV_FILE="/opt/civitas/config/civitas.env"
if [[ -f "$CIVITAS_ENV_FILE" ]]; then
    set -a
    # shellcheck source=/dev/null
    source "$CIVITAS_ENV_FILE"
    set +a
    log "Variables globales chargées (CIVITAS_IP=${CIVITAS_IP:-?})"
else
    log "ERREUR: $CIVITAS_ENV_FILE introuvable — exécuter 01_system_base.sh d'abord"
    exit 1
fi

# Démarre (ou vérifie s'il tourne déjà) le stack Jitsi complet — Prosody,
# Jicofo, JVB, Web — puis vérifie chaque composant un par un. Avant, ce
# script se contentait d'attendre passivement que JVB réponde, sans jamais
# démarrer Jitsi lui-même ; si les conteneurs étaient H.S., le boot échouait
# sans indiquer comment les redémarrer. Voir scripts/jitsi_boot.sh.
SCRIPT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
log "Démarrage/vérification du stack Jitsi..."
if ! bash "$SCRIPT_DIR/jitsi_boot.sh"; then
    log "ERREUR: le stack Jitsi n'est pas opérationnel (voir messages ci-dessus)"
    exit 1
fi

compose_up() {
    local file=$1
    local name=$2
    log "Démarrage $name..."
    docker compose -f $file up -d
}

# Prometheus ne supporte pas nativement l'interpolation de variables d'env
# dans sa config YAML — on génère donc le fichier réel depuis son template
# à chaque boot, via envsubst (cf. monitoring/prometheus/prometheus.yml.template).
PROM_DIR="/opt/civitas/monitoring/prometheus"
if [[ -f "$PROM_DIR/prometheus.yml.template" ]]; then
    log "Génération de prometheus.yml depuis le template..."
    envsubst < "$PROM_DIR/prometheus.yml.template" > "$PROM_DIR/prometheus.yml"
else
    log "ERREUR: $PROM_DIR/prometheus.yml.template introuvable"
    exit 1
fi

compose_up /opt/civitas/kafka/docker-compose.yml "Kafka"
compose_up /opt/civitas/monitoring/docker-compose.yml "Monitoring"

compose_up /opt/civitas/services/room-config/docker-compose.yml "Room Config"
# room-config exécute désormais create_all() + alembic upgrade head à son
# démarrage (cf. PLAN_SYNCHRONISATION_ROOMS_JITSI.md §8.6) — peut prendre
# plus que quelques secondes selon l'état de la base ; on attend une vraie
# preuve plutôt qu'un délai fixe.
if ! wait_for_health "http://localhost:8010/health" "Room Config" 60; then
    err "Room Config indisponible — voir : docker logs civitas-room-config --tail=100"
    exit 1
fi

# event-bridge AVANT room-spawner : c'est lui qui produit les événements
# jitsi.room.events/jitsi.participant.events que room-spawner consomme.
# Ordre inversé par rapport à avant — sans effet fatal via Kafka (le
# consumer attend simplement les messages), mais plus logique et plus
# rapide à diagnostiquer en cas de souci.
compose_up /opt/civitas/event-bridge/docker-compose.yml "Event Bridge"
if ! wait_for_health "http://localhost:8100/health" "Event Bridge" 30; then
    err "Event Bridge indisponible — voir : docker logs civitas-event-bridge --tail=100"
    exit 1
fi

compose_up /opt/civitas/services/room-spawner/docker-compose.yml "Room Spawner"
if ! wait_for_health "http://localhost:8011/health" "Room Spawner" 30; then
    err "Room Spawner indisponible — voir : docker logs civitas-room-spawner --tail=100"
    exit 1
fi

compose_up /opt/civitas/services/peer/docker-compose.yml "Peer"
if ! wait_for_health "http://localhost:8002/health" "Peer" 30; then
    err "Peer indisponible — voir : docker logs civitas-peer --tail=100"
    exit 1
fi

log "Civitas opérationnel ✓ — Room Config, Event Bridge, Room Spawner, Peer tous vérifiés"

