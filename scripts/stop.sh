#!/bin/bash
LOG="/opt/civitas/logs/boot.log"
echo "[$(date)] Arrêt Civitas..." | tee -a $LOG

docker compose -f /opt/civitas/services/peer/docker-compose.yml down
docker compose -f /opt/civitas/services/room-spawner/docker-compose.yml down
docker compose -f /opt/civitas/event-bridge/docker-compose.yml down
docker compose -f /opt/civitas/services/room-config/docker-compose.yml down
docker compose -f /opt/civitas/monitoring/docker-compose.yml down
docker compose -f /opt/civitas/kafka/docker-compose.yml down

echo "[$(date)] Arrêt complet ✓" | tee -a $LOG
