#!/bin/bash
set -e

log() {
    echo "[$(date)] $1"
}

SCRIPT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
PROJECT_ROOT="$(cd "$SCRIPT_DIR/.." && pwd)"

# Liste des microservices à builder
declare -A SERVICES
SERVICES["event-bridge"]="$PROJECT_ROOT/event-bridge/docker-compose.yml"
SERVICES["peer"]="$PROJECT_ROOT/services/peer/docker-compose.yml"
SERVICES["room-config"]="$PROJECT_ROOT/services/room-config/docker-compose.yml"
SERVICES["room-spawner"]="$PROJECT_ROOT/services/room-spawner/docker-compose.yml"

build_service() {
    local name=$1
    local file=$2
    log "Build du microservice $name..."
    docker compose -f "$file" build
}

show_usage() {
    echo "Usage: $0 [service_name]"
    echo ""
    echo "Build tous les microservices Civitas ou un service spécifique."
    echo ""
    echo "Services disponibles:"
    for service in "${!SERVICES[@]}"; do
        echo "  - $service"
    done
    echo ""
    echo "Exemples:"
    echo "  $0              # Build tous les services"
    echo "  $0 event-bridge # Build uniquement event-bridge"
}

# Vérifie les arguments
if [ "$1" = "-h" ] || [ "$1" = "--help" ]; then
    show_usage
    exit 0
fi

if [ -n "$1" ]; then
    # Build ciblé
    SERVICE_NAME="$1"
    if [ -z "${SERVICES[$SERVICE_NAME]}" ]; then
        log "ERREUR: service '$SERVICE_NAME' inconnu"
        echo ""
        show_usage
        exit 1
    fi
    build_service "$SERVICE_NAME" "${SERVICES[$SERVICE_NAME]}"
    log "Build $SERVICE_NAME terminé ✓"
else
    # Build complet
    log "Build complet de tous les microservices Civitas..."
    for service in "${!SERVICES[@]}"; do
        build_service "$service" "${SERVICES[$service]}"
    done
    log "Build complet terminé ✓"
fi
