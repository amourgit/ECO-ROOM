#!/bin/bash
LOG="/opt/civitas/logs/boot.log"
echo "[$(date)] Arrêt Civitas..." | tee -a $LOG

docker compose -f /opt/civitas/services/peer/docker-compose.yml down
docker compose -f /opt/civitas/services/room-spawner/docker-compose.yml down
docker compose -f /opt/civitas/event-bridge/docker-compose.yml down
docker compose -f /opt/civitas/services/room-config/docker-compose.yml down
docker compose -f /opt/civitas/monitoring/docker-compose.yml down
docker compose -f /opt/civitas/kafka/docker-compose.yml down

# Arrêt du stack Jitsi (Web, JVB, Jicofo, Prosody) — symétrique du démarrage
# effectué par boot.sh via jitsi_boot.sh. Absent jusqu'ici : Jitsi n'était
# jamais arrêté par ce script.
SCRIPT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
echo "[$(date)] Arrêt du stack Jitsi..." | tee -a $LOG
bash "$SCRIPT_DIR/jitsi_stop.sh" 2>&1 | tee -a $LOG

echo "[$(date)] Arrêt complet ✓" | tee -a $LOG
