#!/usr/bin/env bash
# =============================================================================
# CIVITAS — Démarrage et vérification complète du stack Jitsi Meet
# (Prosody, Jicofo, JVB, Web) — PRÉALABLE OBLIGATOIRE à scripts/boot.sh
#
# Pourquoi ce script existe :
#   boot.sh se contente d'attendre (poll) que JVB réponde sur son endpoint de
#   santé — il ne démarre jamais Jitsi lui-même. Si le stack Jitsi est arrêté
#   (conteneurs H.S., serveur redémarré, etc.), boot.sh échoue en expliquant
#   juste "JVB non disponible", sans jamais dire comment le (re)démarrer.
#   Ce script comble ce trou : il découvre comment Jitsi est déployé sur
#   cette machine, le démarre, puis vérifie chaque composant un par un dans
#   l'ordre réel de dépendance (Prosody → Jicofo → JVB → Web).
#
# Usage :
#   sudo bash scripts/jitsi_boot.sh
#
# Variables d'environnement optionnelles :
#   JITSI_COMPOSE_DIR    Chemin du docker-compose.yml Jitsi, si non trouvé
#                        automatiquement (cf. scripts/lib/jitsi_common.sh)
#   JVB_HEALTH_URL       URL de health-check JVB
#                        (défaut : http://localhost:8080/about/health)
#   JVB_HEALTH_TIMEOUT   Délai max d'attente JVB en secondes (défaut : 180)
#   CIVITAS_IP           IP du serveur, si l'auto-détection ne convient pas
# =============================================================================
set -uo pipefail  # PAS de -e : chaque échec doit être géré explicitement,
                   # avec un message actionnable, pas juste stopper le script.

SCRIPT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
# shellcheck source=lib/jitsi_common.sh
source "$SCRIPT_DIR/lib/jitsi_common.sh"

JVB_HEALTH_URL="${JVB_HEALTH_URL:-http://localhost:8080/about/health}"
JVB_HEALTH_TIMEOUT="${JVB_HEALTH_TIMEOUT:-180}"

echo ""
info "============================================================"
info " CIVITAS — Démarrage du stack Jitsi Meet"
info "============================================================"

SERVER_IP=$(detect_server_ip)
[[ -n "$SERVER_IP" ]] && info "IP serveur détectée : $SERVER_IP" \
                       || warn "IP serveur non détectée (non bloquant pour ce script)"

# --------------------------------------------------------------------------
# 1. Découverte du mode de déploiement
# --------------------------------------------------------------------------
info "Détection du mode de déploiement Jitsi..."

MODE_INFO=$(detect_jitsi_mode) || die "$(cat <<EOF
Impossible de localiser un déploiement Jitsi sur cette machine.

  → Déploiement Docker (docker-jitsi-meet) :
      export JITSI_COMPOSE_DIR=/chemin/vers/docker-jitsi-meet
      puis relancer ce script.

  → Déploiement natif (paquets Debian jitsi-meet) :
      vérifier que prosody est installé : dpkg -l | grep prosody
      Si absent, Jitsi n'est pas encore installé (hors périmètre de ce
      script — cf. guide officiel : https://jitsi.github.io/handbook/)

  → Chemins vérifiés automatiquement :
$(jitsi_candidate_dirs | grep -v '^$' | sed 's/^/      - /')
EOF
)"

JITSI_MODE="${MODE_INFO%%:*}"
JITSI_DIR="${MODE_INFO#*:}"

case "$JITSI_MODE" in
    docker)  log "Déploiement Docker détecté : $JITSI_DIR" ;;
    systemd) log "Déploiement natif détecté (prosody/jicofo/jitsi-videobridge2 via systemd)" ;;
esac

# --------------------------------------------------------------------------
# 2. Démarrage
# --------------------------------------------------------------------------
echo ""
info "Démarrage des composants Jitsi..."

case "$JITSI_MODE" in
    docker)
        info "docker compose up -d (dans $JITSI_DIR)..."
        if ! ( cd "$JITSI_DIR" && docker compose up -d ); then
            die "Échec du démarrage des conteneurs Jitsi.
  → Diagnostiquer : cd $JITSI_DIR && docker compose logs --tail=100
  → Vérifier que le réseau externe requis existe (souvent 'meet.jitsi' ou 'civitas-net') :
      docker network ls"
        fi
        log "docker compose up -d exécuté"
        ;;
    systemd)
        for svc in prosody jicofo jitsi-videobridge2 nginx; do
            if systemctl is-active --quiet "$svc" 2>/dev/null; then
                log "$svc déjà actif"
            else
                info "Démarrage de $svc..."
                if systemctl start "$svc" 2>/dev/null; then
                    log "$svc démarré"
                else
                    die "Échec du démarrage de $svc.
  → Diagnostiquer : journalctl -u $svc -n 100 --no-pager"
                fi
            fi
        done
        ;;
esac

# --------------------------------------------------------------------------
# 3. Vérifications, une par une, dans l'ordre réel de dépendance :
#    Prosody (XMPP, backbone) -> Jicofo (focus, dépend de Prosody)
#    -> JVB (dépend de Prosody+Jicofo) -> Web (frontend)
# --------------------------------------------------------------------------
echo ""
info "Vérification des composants (ordre de dépendance)..."
echo ""

FAILED=0

port_listening() {
    local port="$1"
    if command -v ss &>/dev/null; then
        ss -ltn 2>/dev/null | grep -q ":${port} "
    else
        (exec 3<>"/dev/tcp/127.0.0.1/${port}") 2>/dev/null && exec 3>&-
    fi
}

container_running() {
    docker ps --filter "name=$1" --filter "status=running" --format '{{.Names}}' 2>/dev/null | grep -q .
}

# --- Prosody : conteneur/service actif ---
case "$JITSI_MODE" in
docker)
    if container_running "prosody"; then
        log "Prosody : conteneur actif"
    else
        err "Prosody : aucun conteneur actif trouvé (filtré sur le nom 'prosody')"
        FAILED=1
    fi
    ;;
systemd)
    if systemctl is-active --quiet prosody; then
        log "Prosody : service actif"
    else
        err "Prosody : service inactif — journalctl -u prosody -n 100 --no-pager"
        FAILED=1
    fi
    ;;
esac

# --- Jicofo : process/conteneur actif ---
case "$JITSI_MODE" in
    docker)
        if container_running "jicofo"; then
            log "Jicofo : conteneur actif"
        else
            err "Jicofo : aucun conteneur actif trouvé (filtré sur le nom 'jicofo')"
            FAILED=1
        fi
        ;;
    systemd)
        if systemctl is-active --quiet jicofo; then
            log "Jicofo : service actif"
        else
            err "Jicofo : service inactif — journalctl -u jicofo -n 100 --no-pager"
            FAILED=1
        fi
        ;;
esac

# --- JVB : health endpoint HTTP, avec attente active ---
info "Attente JVB prêt (max ${JVB_HEALTH_TIMEOUT}s sur $JVB_HEALTH_URL)..."
elapsed=0
jvb_status="000"
while [ "$elapsed" -lt "$JVB_HEALTH_TIMEOUT" ]; do
    jvb_status=$(curl -s -o /dev/null -w "%{http_code}" "$JVB_HEALTH_URL" 2>/dev/null || echo "000")
    [ "$jvb_status" = "200" ] && break
    sleep 5
    elapsed=$((elapsed + 5))
done

if [ "$jvb_status" = "200" ]; then
    log "JVB prêt (HTTP 200 après ${elapsed}s)"
else
    err "JVB non disponible après ${JVB_HEALTH_TIMEOUT}s (dernier code HTTP : $jvb_status)"
    case "$JITSI_MODE" in
        docker)  err "  → Diagnostiquer : docker logs jvb --tail=100" ;;
        systemd) err "  → Diagnostiquer : journalctl -u jitsi-videobridge2 -n 100 --no-pager" ;;
    esac
    FAILED=1
fi

# --- Web (frontend nginx) : 443 en priorité, 80 en repli ---
if port_listening 443; then
    log "Web : port 443 (HTTPS) à l'écoute"
elif port_listening 80; then
    warn "Web : port 443 injoignable — port 80 (HTTP) à l'écoute en repli"
else
    err "Web : ni le port 443 ni le port 80 ne répondent"
    FAILED=1
fi

# --------------------------------------------------------------------------
# Résumé
# --------------------------------------------------------------------------
echo ""
echo "============================================================"
if [ "$FAILED" -eq 0 ]; then
    log "Stack Jitsi opérationnel — Prosody, Jicofo, JVB, Web vérifiés ✓"
    echo "============================================================"
    exit 0
else
    err "Au moins une vérification a échoué — voir les messages ci-dessus"
    echo "============================================================"
    exit 1
fi
