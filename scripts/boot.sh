#!/bin/bash
set -e

log() {
    echo "[$(date)] $1"
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
sleep 15
compose_up /opt/civitas/monitoring/docker-compose.yml "Monitoring"
compose_up /opt/civitas/services/room-config/docker-compose.yml "Room Config"
sleep 5
compose_up /opt/civitas/services/room-spawner/docker-compose.yml "Room Spawner"
compose_up /opt/civitas/event-bridge/docker-compose.yml "Event Bridge"
compose_up /opt/civitas/services/peer/docker-compose.yml "Peer"

log "Civitas opérationnel ✓"

