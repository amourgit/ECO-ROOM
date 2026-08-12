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
#   XMPP_SERVER          Nom XMPP de Prosody, pour la vérification TCP réelle
#                        du port XMPP en mode Docker (défaut : xmpp.meet.jitsi)
#   XMPP_PORT            Port XMPP de Prosody à vérifier (défaut : 5222)
#   PROSODY_LISTEN_TIMEOUT  Délai max d'attente de l'écoute Prosody, en
#                        secondes (défaut : 60)
#   JICOFO_HEALTH_URL    URL de health-check Jicofo (requiert
#                        JICOFO_ENABLE_HEALTH_CHECKS=1 dans jitsi/.env)
#                        (défaut : http://localhost:8888/about/health)
#   JICOFO_HEALTH_TIMEOUT  Délai max d'attente santé Jicofo, en secondes
#                        (défaut : 60)
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
        # Conteneurs rootless/read-only (stable-11146+) : storage/ et tmp/
        # doivent exister et être inscriptibles par l'uid 1000 AVANT le tout
        # premier démarrage, sinon Prosody (entre autres) refuse de démarrer.
        # cf. scripts/lib/jitsi_common.sh::ensure_jitsi_docker_config_dirs
        ensure_jitsi_docker_config_dirs "$JITSI_DIR"

        # Auto-résync : si .env a changé depuis le dernier démarrage réussi
        # (gen-passwords.sh relancé, ${CONFIG} réutilisé...), purge les
        # comptes Prosody obsolètes AVANT de démarrer plutôt que de laisser
        # Jicofo/JVB échouer en boucle avec SASL not-authorized — cf. §7.5
        # de PLAN_SYNCHRONISATION_ROOMS_JITSI.md et
        # scripts/lib/jitsi_common.sh::sync_prosody_accounts_with_env
        sync_prosody_accounts_with_env "$JITSI_DIR"

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

# --- Prosody : conteneur actif, ET écoute TCP/XMPP réellement constatée ---
# (un conteneur "actif" ne prouve rien de l'état interne de Prosody —
# cf. scripts/lib/jitsi_common.sh::wait_for_prosody_listening)
PROSODY_OK=0
PROSODY_LISTEN_TIMEOUT="${PROSODY_LISTEN_TIMEOUT:-60}"
case "$JITSI_MODE" in
docker)
    if container_running "prosody"; then
        log "Prosody : conteneur actif"
        info "Attente de l'écoute XMPP (max ${PROSODY_LISTEN_TIMEOUT}s, ss -ltn dans le conteneur prosody)..."
        if wait_for_prosody_listening "$JITSI_DIR" "$PROSODY_LISTEN_TIMEOUT"; then
            log "Prosody : écoute confirmée sur le port ${XMPP_PORT:-5222} (ss -ltn)"
            if check_prosody_reachable_from_jicofo "$JITSI_DIR"; then
                log "Prosody : joignable depuis Jicofo (TCP ouvert de bout en bout)"
                PROSODY_OK=1
            else
                err "Prosody écoute localement, mais INJOIGNABLE depuis Jicofo (réseau Docker/pare-feu ?)"
                FAILED=1
            fi
        else
            err "Prosody : conteneur actif mais AUCUNE écoute sur le port ${XMPP_PORT:-5222} après ${PROSODY_LISTEN_TIMEOUT}s"
            err "  → Cause la plus fréquente : \${CONFIG}/storage/prosody non inscriptible par l'uid 1000"
            err "    du conteneur (Prosody plante silencieusement à l'init, sans faire sortir le conteneur —"
            err "    s6-overlay le relance en boucle). Ce script a préparé ces répertoires en (2), donc si"
            err "    l'erreur persiste, vérifier qu'aucun processus externe n'a recréé/remonté \${CONFIG}."
            prosody_listen_diagnose "$JITSI_DIR"
            FAILED=1
        fi
    else
        err "Prosody : aucun conteneur actif trouvé (filtré sur le nom 'prosody')"
        FAILED=1
    fi
    ;;
systemd)
    if systemctl is-active --quiet prosody; then
        log "Prosody : service actif"
        PROSODY_OK=1
    else
        err "Prosody : service inactif — journalctl -u prosody -n 100 --no-pager"
        FAILED=1
    fi
    ;;
esac

# --- Jicofo : conteneur actif, ET santé REST réelle (auth XMPP incluse) ---
# Un port TCP ouvert sur Prosody NE PROUVE PAS que Jicofo s'est authentifié
# avec succès (SASL peut échouer après coup — vécu en pratique : TCP ouvert
# ET SASLError "not-authorized" en boucle simultanément, cf. §7.5 de
# PLAN_SYNCHRONISATION_ROOMS_JITSI.md). Le health-check REST de Jicofo,
# lui, tente réellement de rejoindre une conférence — donc de s'authentifier
# à Prosody — pour répondre 200 : c'est la seule preuve fiable ici. Requiert
# JICOFO_ENABLE_HEALTH_CHECKS=1 dans jitsi/.env (déjà dans .env.example).
JICOFO_OK=0
JICOFO_HEALTH_URL="${JICOFO_HEALTH_URL:-http://localhost:8888/about/health}"
JICOFO_HEALTH_TIMEOUT="${JICOFO_HEALTH_TIMEOUT:-60}"
case "$JITSI_MODE" in
    docker)
        if ! container_running "jicofo"; then
            err "Jicofo : aucun conteneur actif trouvé (filtré sur le nom 'jicofo')"
            FAILED=1
        elif [ "$PROSODY_OK" -ne 1 ]; then
            warn "Jicofo : vérification de santé sautée (Prosody non confirmé à l'écoute)"
            FAILED=1
        else
            log "Jicofo : conteneur actif"
            info "Attente santé Jicofo (max ${JICOFO_HEALTH_TIMEOUT}s sur $JICOFO_HEALTH_URL)..."
            elapsed=0
            jicofo_status="000"
            while [ "$elapsed" -lt "$JICOFO_HEALTH_TIMEOUT" ]; do
                jicofo_status=$(curl -s -o /dev/null -w "%{http_code}" "$JICOFO_HEALTH_URL" 2>/dev/null || echo "000")
                [ "$jicofo_status" = "200" ] && break
                sleep 3
                elapsed=$((elapsed + 3))
            done
            if [ "$jicofo_status" = "200" ]; then
                log "Jicofo : opérationnel et authentifié auprès de Prosody (HTTP 200 après ${elapsed}s)"
                JICOFO_OK=1
            else
                err "Jicofo : conteneur actif mais santé REST KO après ${JICOFO_HEALTH_TIMEOUT}s (dernier code : $jicofo_status)"
                err "  → Cause fréquente : SASLError 'not-authorized' — comptes Prosody désynchronisés du .env actuel"
                err "  → Vérifier : cd $JITSI_DIR && docker compose logs jicofo --tail=50"
                err "  → Si 'not-authorized' visible : sudo bash scripts/jitsi_reset_prosody.sh"
                FAILED=1
            fi
        fi
        ;;
    systemd)
        if systemctl is-active --quiet jicofo; then
            log "Jicofo : service actif"
            JICOFO_OK=1
        else
            err "Jicofo : service inactif — journalctl -u jicofo -n 100 --no-pager"
            FAILED=1
        fi
        ;;
esac

# --- JVB : health endpoint HTTP, avec attente active ---
# Note : le /about/health de JVB répond 200 dès que son serveur REST est
# levé, MÊME SI sa propre connexion XMPP vers la brewery MUC échoue encore
# en SASL (vécu en pratique) — ce n'est donc pas une preuve d'authentification
# JVB->Prosody à lui seul. En cas de doute, vérifier aussi les logs JVB.
# Inutile d'attendre JVB_HEALTH_TIMEOUT (jusqu'à 3 min) s'il est déjà acquis
# que Prosody n'écoute pas : JVB ne pourra de toute façon jamais s'y
# connecter en XMPP tant que ce n'est pas corrigé (cf. bloc Prosody ci-dessus).
if [ "$PROSODY_OK" -ne 1 ]; then
    warn "JVB : vérification sautée (Prosody non confirmé à l'écoute — JVB ne peut pas s'y connecter)"
    FAILED=1
else
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
            docker)  err "  → Diagnostiquer : cd $JITSI_DIR && docker compose logs jvb --tail=100" ;;
            systemd) err "  → Diagnostiquer : journalctl -u jitsi-videobridge2 -n 100 --no-pager" ;;
        esac
        FAILED=1
    fi
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
