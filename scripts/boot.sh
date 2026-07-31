#!/bin/bash
set -e

log() {
    echo "[$(date)] $1"
}

log "Démarrage Civitas..."

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

compose_up /opt/civitas/kafka/docker-compose.yml "Kafka"
sleep 15
compose_up /opt/civitas/monitoring/docker-compose.yml "Monitoring"
compose_up /opt/civitas/services/room-config/docker-compose.yml "Room Config"
sleep 5
compose_up /opt/civitas/services/room-spawner/docker-compose.yml "Room Spawner"
compose_up /opt/civitas/event-bridge/docker-compose.yml "Event Bridge"
compose_up /opt/civitas/services/peer/docker-compose.yml "Peer"

log "Civitas opérationnel ✓"

