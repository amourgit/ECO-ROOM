#!/bin/bash
set -e

log() {
    echo "[$(date)] $1"
}

log "Démarrage Civitas..."

# Laisser le temps à Jitsi de s'initialiser
sleep 20

# Attendre que le JVB soit opérationnel
log "Attente JVB..."
MAX=180
COUNT=0
while [ $COUNT -lt $MAX ]; do
    STATUS=$(curl -s -o /dev/null -w "%{http_code}" http://localhost:8080/about/health 2>/dev/null)
    if [ "$STATUS" = "200" ]; then
        log "JVB prêt ✓"
        break
    fi
    sleep 5
    COUNT=$((COUNT + 5))
done

if [ $COUNT -ge $MAX ]; then
    log "ERREUR: JVB non disponible après ${MAX}s"
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

