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

# Sous-réseau CIDR de l'interface principale (ex: <IP_SERVEUR>/24) — utilisé
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

# --- Préparation du répertoire CONFIG (mode Docker uniquement) --------------
#
# Depuis la release stable-11146 de jitsi/docker-jitsi-meet, les conteneurs
# tournent en rootless (uid/gid 1000) avec un filesystem en lecture seule.
# ${CONFIG}/storage/* et ${CONFIG}/tmp/* sont les SEULS répertoires sur
# lesquels les conteneurs écrivent (comptes/certs Prosody, TLS web, etc.) ;
# doc officielle :
#   https://jitsi.github.io/handbook/docs/devops-guide/devops-guide-docker#rootless-and-read-only-containers
# S'ils n'existent pas, Docker les crée lui-même en root:root au montage —
# non inscriptibles par uid 1000 — et le conteneur concerné refuse de
# démarrer avec une erreur explicite nommant le répertoire fautif. Prosody
# est le cas le plus critique : sans accès en écriture à
# ${CONFIG}/storage/prosody, il ne démarre jamais, et JVB/Jicofo ne peuvent
# alors jamais réellement établir de connexion XMPP vers xmpp.meet.jitsi:5222
# — même si tout le reste (DNS, secrets, configuration générée) est correct.
#
# Lit CONFIG dans le .env du déploiement ($1/.env) ; échoue explicitement
# si le .env n'existe pas encore (pas de valeur par défaut inventée).
ensure_jitsi_docker_config_dirs() {
    local jitsi_dir="$1" env_file config_dir
    env_file="$jitsi_dir/.env"

    [[ -f "$env_file" ]] || die "$(cat <<EOF
$env_file introuvable — impossible de préparer les répertoires CONFIG.
  → cd $jitsi_dir && cp .env.example .env && ./gen-passwords.sh
EOF
)"

    config_dir=$(grep -E '^CONFIG=' "$env_file" | tail -1 | cut -d= -f2-)
    [[ -n "$config_dir" ]] || die "CONFIG= absent ou vide dans $env_file — impossible de préparer les répertoires."
    config_dir="${config_dir/#\~/$HOME}"

    info "Préparation de \$CONFIG ($config_dir) pour les conteneurs rootless..."

    # Lus par les conteneurs au démarrage (pas d'écriture requise, mais le
    # répertoire doit exister pour que le bind-mount se fasse proprement).
    mkdir -p \
        "$config_dir/web" \
        "$config_dir/prosody/config" \
        "$config_dir/prosody/prosody-plugins-custom" \
        "$config_dir/jicofo" \
        "$config_dir/jvb" \
        || die "Échec de création des répertoires de configuration sous $config_dir"

    # Écrits par les conteneurs à l'exécution (état persistant / fichiers
    # temporaires) — DOIVENT être inscriptibles par l'uid 1000 du conteneur.
    mkdir -p \
        "$config_dir/storage/prosody" \
        "$config_dir/storage/web" \
        "$config_dir/storage/transcripts" \
        "$config_dir/tmp/web-crontabs" \
        "$config_dir/tmp/web-load-test" \
        || die "Échec de création des répertoires persistants sous $config_dir/{storage,tmp}"

    chmod 777 \
        "$config_dir/storage/prosody" \
        "$config_dir/storage/web" \
        "$config_dir/storage/transcripts" \
        "$config_dir/tmp/web-crontabs" \
        "$config_dir/tmp/web-load-test" \
        || die "Échec du chmod sur $config_dir/{storage,tmp} (inscriptible par uid 1000 requis)"

    log "Répertoires CONFIG prêts (storage/ et tmp/ inscriptibles par uid 1000)"
}

# --- Vérification réelle de la connexion XMPP JVB/Jicofo -> Prosody ---------
#
# Les images Jitsi ne fournissent pas `nc`. On utilise à la place le
# pseudo-périphérique /dev/tcp de bash (toujours présent dans ces images)
# pour prouver, ou non, qu'une connexion TCP s'établit réellement sur
# xmpp.meet.jitsi:5222 depuis le conteneur "jicofo" — la question laissée
# ouverte par un simple test de résolution DNS ou de process actif.
# Retourne 0 si le port répond, 1 sinon (jamais bloquant : à l'appelant de
# décider si c'est fatal).
check_prosody_xmpp_port() {
    local jitsi_dir="$1"
    local xmpp_server="${XMPP_SERVER:-xmpp.meet.jitsi}"
    local xmpp_port="${XMPP_PORT:-5222}"

    ( cd "$jitsi_dir" && docker compose exec -T jicofo \
        bash -c "(exec 3<>/dev/tcp/${xmpp_server}/${xmpp_port}) 2>/dev/null" \
    ) 2>/dev/null
}
