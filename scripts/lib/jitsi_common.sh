#!/usr/bin/env bash
# =============================================================================
# CIVITAS — Bibliothèque partagée : découverte du déploiement Jitsi Meet
#
# Ce repo (ECO-ROOM) ne gère que les services CIVITAS (Kafka, room-config,
# peer, etc.) — le stack Jitsi Meet lui-même (Prosody, Jicofo, JVB, Web) est
# déployé séparément, soit via docker-jitsi-meet (Docker), soit en paquets
# natifs Debian (systemd). Ce fichier centralise la logique de découverte
# pour que jitsi_boot.sh et jitsi_stop.sh restent cohérents et DRY.
#
# À sourcer, jamais à exécuter directement :
#   source "$(dirname "$0")/lib/jitsi_common.sh"
# =============================================================================

RED='\033[0;31m'; GREEN='\033[0;32m'; YELLOW='\033[1;33m'
BLUE='\033[0;34m'; NC='\033[0m'

log()  { echo -e "${GREEN}[✓]${NC} $*"; }
info() { echo -e "${BLUE}[→]${NC} $*"; }
warn() { echo -e "${YELLOW}[!]${NC} $*"; }
err()  { echo -e "${RED}[✗]${NC} $*" >&2; }
die()  { err "$*"; exit 1; }

# --- Détection dynamique de l'IP du serveur (jamais une IP en dur) ----------
# Ordre de priorité :
#   1. Variable d'environnement CIVITAS_IP (override explicite)
#   2. Déjà généré par 01_system_base.sh (/opt/civitas/config/civitas.env)
#   3. Auto-détection via la route par défaut (IP source vers Internet)
detect_server_ip() {
    if [[ -n "${CIVITAS_IP:-}" ]]; then
        echo "$CIVITAS_IP"
        return 0
    fi
    if [[ -f /opt/civitas/config/civitas.env ]]; then
        local ip
        ip=$(grep -E '^CIVITAS_IP=' /opt/civitas/config/civitas.env 2>/dev/null | cut -d= -f2)
        if [[ -n "$ip" ]]; then
            echo "$ip"
            return 0
        fi
    fi
    ip -4 route get 1.1.1.1 2>/dev/null | awk '{for(i=1;i<=NF;i++) if ($i=="src") print $(i+1)}'
}

# Interface réseau principale (celle utilisée pour sortir vers Internet)
detect_server_iface() {
    ip -4 route get 1.1.1.1 2>/dev/null | awk '{for(i=1;i<=NF;i++) if ($i=="dev") print $(i+1)}'
}

# Sous-réseau CIDR de l'interface principale (ex: 192.168.1.89/24) — utilisé
# pour les règles UFW "accès interne uniquement", jamais un /24 supposé en dur.
detect_server_cidr() {
    if [[ -n "${CIVITAS_SUBNET:-}" ]]; then
        echo "$CIVITAS_SUBNET"
        return 0
    fi
    local iface
    iface=$(detect_server_iface)
    [[ -z "$iface" ]] && return 1
    ip -o -4 addr show dev "$iface" scope global 2>/dev/null | awk '{print $4}' | head -1
}

# --- Découverte du déploiement Jitsi (Docker ou natif) ----------------------

# Chemins conventionnels où chercher un déploiement docker-jitsi-meet, par
# ordre de priorité, si JITSI_COMPOSE_DIR n'est pas explicitement fourni.
jitsi_candidate_dirs() {
    printf '%s\n' \
        "${JITSI_COMPOSE_DIR:-}" \
        "/opt/jitsi-docker-compose" \
        "/opt/docker-jitsi-meet" \
        "/opt/jitsi-meet" \
        "/opt/civitas/jitsi" \
        "/srv/jitsi" \
        "${HOME:-/root}/docker-jitsi-meet"
}

# Retourne le chemin du docker-compose.yml Jitsi trouvé, ou échoue (code 1)
find_jitsi_compose() {
    local d
    while IFS= read -r d; do
        [[ -z "$d" ]] && continue
        if [[ -f "$d/docker-compose.yml" ]]; then
            echo "$d"
            return 0
        fi
    done < <(jitsi_candidate_dirs)
    return 1
}

# Détecte le mode de déploiement : "docker", "systemd", ou échoue (rien trouvé)
detect_jitsi_mode() {
    local dir
    if dir=$(find_jitsi_compose); then
        echo "docker:$dir"
        return 0
    fi
    if systemctl list-unit-files 2>/dev/null | grep -qE '^prosody\.service'; then
        echo "systemd:"
        return 0
    fi
    return 1
}
