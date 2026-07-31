#!/usr/bin/env bash
# =============================================================================
# CIVITAS — Arrêt du stack Jitsi Meet (Web, JVB, Jicofo, Prosody)
# Symétrique de jitsi_boot.sh — ordre inverse du démarrage.
#
# Usage : sudo bash scripts/jitsi_stop.sh
#
# Variables d'environnement optionnelles : cf. scripts/lib/jitsi_common.sh
#   (JITSI_COMPOSE_DIR, CIVITAS_IP)
# =============================================================================
set -uo pipefail

SCRIPT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
# shellcheck source=lib/jitsi_common.sh
source "$SCRIPT_DIR/lib/jitsi_common.sh"

echo ""
info "============================================================"
info " CIVITAS — Arrêt du stack Jitsi Meet"
info "============================================================"

MODE_INFO=$(detect_jitsi_mode) || {
    warn "Aucun déploiement Jitsi détecté — rien à arrêter."
    exit 0
}
JITSI_MODE="${MODE_INFO%%:*}"
JITSI_DIR="${MODE_INFO#*:}"

case "$JITSI_MODE" in
    docker)
        info "docker compose down (dans $JITSI_DIR)..."
        if ( cd "$JITSI_DIR" && docker compose down ); then
            log "Conteneurs Jitsi arrêtés"
        else
            err "Échec de l'arrêt des conteneurs Jitsi — voir : cd $JITSI_DIR && docker compose logs --tail=100"
            exit 1
        fi
        ;;
    systemd)
        # Ordre inverse du démarrage : Web -> JVB -> Jicofo -> Prosody
        for svc in nginx jitsi-videobridge2 jicofo prosody; do
            if systemctl is-active --quiet "$svc" 2>/dev/null; then
                info "Arrêt de $svc..."
                systemctl stop "$svc" && log "$svc arrêté" || warn "Échec de l'arrêt de $svc"
            else
                log "$svc déjà arrêté"
            fi
        done
        ;;
esac

log "Arrêt du stack Jitsi terminé"
