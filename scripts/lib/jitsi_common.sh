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

# --- Auto-résynchronisation des comptes Prosody avec .env (avant démarrage) -
#
# Racine du problème observé en usage réel (§7.5 du plan) : Prosody
# n'enregistre les comptes XMPP internes (jicofo, jvb) qu'UNE FOIS dans son
# stockage persistant. Si JICOFO_AUTH_PASSWORD/JVB_AUTH_PASSWORD changent
# ensuite dans .env (gen-passwords.sh relancé, ${CONFIG} réutilisé d'un
# essai précédent...) sans purge manuelle, les comptes stockés restent sur
# l'ANCIEN mot de passe -> SASL not-authorized en boucle, invisible tant
# qu'on ne regarde pas les logs Jicofo/JVB en détail.
#
# Cette fonction élimine le besoin de s'en souvenir : à CHAQUE démarrage,
# avant que Prosody ne tourne, elle compare une empreinte des mots de passe
# actuels de .env à celle enregistrée lors du dernier démarrage réussi
# (fichier caché dans ${CONFIG}/storage/prosody, qui persiste avec les
# comptes). Si elles diffèrent, elle purge automatiquement le stockage
# Prosody AVANT le démarrage — Prosody recrée alors les comptes avec les
# valeurs actuelles, sans aucune intervention manuelle.
#
# Sans empreinte enregistrée (premier démarrage avec cette fonction, sur un
# stockage déjà ancien) : ne touche à rien par prudence — c'est le seul cas
# qui nécessite encore un `jitsi_reset_prosody.sh` manuel, une fois.
# Ensuite, l'empreinte est systématiquement à jour et le problème ne peut
# plus se reproduire silencieusement.
sync_prosody_accounts_with_env() {
    local jitsi_dir="$1" env_file config_dir prosody_storage fp_file current_fp stored_fp
    env_file="$jitsi_dir/.env"
    [[ -f "$env_file" ]] || return 0  # ensure_jitsi_docker_config_dirs aura déjà échoué avant, rien à faire ici

    config_dir=$(grep -E '^CONFIG=' "$env_file" | tail -1 | cut -d= -f2-)
    [[ -n "$config_dir" ]] || return 0
    config_dir="${config_dir/#\~/$HOME}"
    prosody_storage="$config_dir/storage/prosody"
    fp_file="$prosody_storage/.civitas_auth_fingerprint"

    current_fp=$(grep -E '^(JICOFO_AUTH_PASSWORD|JVB_AUTH_PASSWORD)=' "$env_file" | sort | sha256sum | cut -d' ' -f1)
    [[ -n "$current_fp" ]] || return 0  # mots de passe pas encore générés (gen-passwords.sh pas encore lancé)

    if [[ -f "$fp_file" ]]; then
        stored_fp=$(cat "$fp_file" 2>/dev/null || true)
        if [[ -n "$stored_fp" && "$stored_fp" != "$current_fp" ]]; then
            warn "Mots de passe XMPP (.env) différents de ceux déjà enregistrés dans Prosody"
            warn "  → Purge automatique de $prosody_storage pour resynchroniser (cf. §7.5 du plan)"
            # docker compose stop est un no-op sûr si prosody n'est pas (encore)
            # démarré (cas normal, cette fonction s'exécute avant le premier
            # "up") — mais protège aussi le cas d'une resynchronisation
            # déclenchée alors que le conteneur tournait déjà : on ne purge
            # jamais son stockage à chaud.
            ( cd "$jitsi_dir" && docker compose stop prosody ) 2>/dev/null
            rm -rf --one-file-system -- "${prosody_storage:?}"/* "${prosody_storage:?}"/.[!.]* 2>/dev/null
        fi
    fi

    mkdir -p "$prosody_storage" && chmod 777 "$prosody_storage"
    echo "$current_fp" > "$fp_file" 2>/dev/null || true
}

# --- Vérification réelle de l'écoute Prosody sur le port XMPP ---------------
#
# Deux niveaux de preuve, dans l'ordre :
#   1. Prosody lui-même écoute-t-il sur 5222 ? -> connexion TCP en loopback
#      (127.0.0.1) DEPUIS le conteneur prosody, via /dev/tcp (pseudo-device
#      bash). Une preuve directe : un conteneur "actif" côté Docker ne dit
#      rien de l'état interne du process Prosody lui-même (s6-overlay peut
#      le laisser en crash-loop sans jamais faire sortir le conteneur, cf.
#      §7.4 de PLAN_SYNCHRONISATION_ROOMS_JITSI.md).
#      NOTE (§7.6) : ce check utilisait initialement `ss -ltn` (confirmé
#      disponible en shell interactif), mais s'est révélé produire de FAUX
#      NÉGATIFS en pratique via `docker compose exec -T` non-interactif —
#      probablement une résolution de $PATH différente pour ce contexte
#      d'exec côté uid non-root (ss vit sous /usr/sbin, pas toujours dans
#      le PATH par défaut hors shell de login). /dev/tcp est un builtin
#      bash, sans dépendance à un binaire externe ni à son PATH — méthode
#      déjà utilisée avec succès pour le point (2) ci-dessous.
#   2. Si (1) est vrai, la connexion aboutit-elle bien depuis Jicofo (le
#      vrai client XMPP), et pas seulement en loopback sur Prosody ?
#      `nc` étant absent des images, on utilise /dev/tcp également.
#
# wait_for_prosody_listening fait du polling (Prosody peut mettre quelques
# secondes à terminer son init — génération de certificats, stockage —
# après "docker compose up -d") : un test one-shot immédiat après le
# démarrage produirait de faux négatifs même sur un déploiement sain.
wait_for_prosody_listening() {
    local jitsi_dir="$1" timeout="${2:-60}"
    local xmpp_port="${XMPP_PORT:-5222}"
    local elapsed=0
    while [ "$elapsed" -lt "$timeout" ]; do
        if ( cd "$jitsi_dir" && docker compose exec -T prosody \
                bash -c "(exec 3<>/dev/tcp/127.0.0.1/${xmpp_port}) 2>/dev/null" \
           ) 2>/dev/null; then
            return 0
        fi
        sleep 2
        elapsed=$((elapsed + 2))
    done
    return 1
}

# Preuve de bout en bout : Jicofo (client XMPP réel) parvient-il à ouvrir
# une connexion TCP vers Prosody, pas seulement Prosody qui écoute en local.
check_prosody_reachable_from_jicofo() {
    local jitsi_dir="$1"
    local xmpp_server="${XMPP_SERVER:-xmpp.meet.jitsi}"
    local xmpp_port="${XMPP_PORT:-5222}"

    ( cd "$jitsi_dir" && docker compose exec -T jicofo \
        bash -c "(exec 3<>/dev/tcp/${xmpp_server}/${xmpp_port}) 2>/dev/null" \
    ) 2>/dev/null
}

# Diagnostic imprimé uniquement en cas d'échec : état TCP réel + `ss` en
# best-effort (informatif seulement, jamais utilisé pour décider du
# succès/échec — cf. note §7.6 ci-dessus) + fin des logs, pour aller droit
# à la cause (le plus souvent une permission refusée sur
# ${CONFIG}/storage/prosody lors de l'init).
prosody_listen_diagnose() {
    local jitsi_dir="$1"
    ( cd "$jitsi_dir" && {
        echo "  -- test TCP loopback 127.0.0.1:${XMPP_PORT:-5222} (dans le conteneur prosody) --"
        docker compose exec -T prosody bash -c \
            "(exec 3<>/dev/tcp/127.0.0.1/${XMPP_PORT:-5222}) 2>/dev/null && echo '  -> ouvert' || echo '  -> fermé/injoignable'"
        echo "  -- ss -ltn, si disponible (informatif uniquement) --"
        docker compose exec -T prosody ss -ltn 2>&1 | sed 's/^/  /'
        echo "  -- docker compose logs prosody --tail=30 --"
        docker compose logs prosody --tail=30 2>&1 | sed 's/^/  /'
    } ) >&2
}

# --- Réinitialisation ciblée des comptes XMPP internes de Prosody -----------
#
# Cause connue et documentée (communauté Jitsi) du SASLError "not-authorized"
# sur Jicofo/JVB alors que .env est par ailleurs cohérent : Prosody NE MET
# JAMAIS À JOUR le mot de passe d'un compte XMPP interne (jicofo, jvb, ...)
# déjà enregistré dans son stockage persistant (${CONFIG}/storage/prosody)
# — il ne le crée qu'une fois. Si JICOFO_AUTH_PASSWORD/JVB_AUTH_PASSWORD
# changent ensuite (gen-passwords.sh relancé, ou ${CONFIG} réutilisé d'un
# essai Docker précédent), les comptes stockés restent sur l'ANCIEN mot de
# passe : Jicofo/JVB présentent le nouveau, Prosody attend l'ancien -> SASL
# not-authorized en boucle, même TCP grand ouvert. Référence :
#   https://www.cynkra.com/blog/2020-11-02-jitsi-load-balanced/
#   ("Do not run gen-passwords.sh multiple times... delete all config
#    folders before running docker-compose up again")
#
# Ne touche QUE ${CONFIG}/storage/prosody (comptes, roster, certs
# auto-générés) — jamais ${CONFIG}/storage/web (certificats web) ni les
# répertoires de configuration en lecture seule. Prosody redémarre ensuite
# avec un stockage vide et recrée les comptes à partir du .env ACTUEL ;
# Jicofo/JVB, déjà en boucle de reconnexion, retrouvent l'accès sans qu'il
# soit nécessaire de les redémarrer.
reset_prosody_account_storage() {
    local jitsi_dir="$1" env_file config_dir prosody_storage
    env_file="$jitsi_dir/.env"

    [[ -f "$env_file" ]] || die "$env_file introuvable."

    config_dir=$(grep -E '^CONFIG=' "$env_file" | tail -1 | cut -d= -f2-)
    [[ -n "$config_dir" ]] || die "CONFIG= absent ou vide dans $env_file."
    config_dir="${config_dir/#\~/$HOME}"
    prosody_storage="$config_dir/storage/prosody"

    [[ "$prosody_storage" == */storage/prosody ]] || die "Chemin de stockage Prosody inattendu, arrêt par sécurité : $prosody_storage"

    info "Arrêt de Prosody..."
    ( cd "$jitsi_dir" && docker compose stop prosody ) \
        || die "Échec de l'arrêt du conteneur prosody."

    info "Purge de $prosody_storage (comptes XMPP internes)..."
    rm -rf --one-file-system -- "${prosody_storage:?}"/* "${prosody_storage:?}"/.[!.]* 2>/dev/null
    mkdir -p "$prosody_storage" && chmod 777 "$prosody_storage" \
        || die "Échec de la recréation de $prosody_storage"

    # Réécrit l'empreinte tout de suite : le stockage est vide, donc les
    # comptes que Prosody va recréer correspondront forcément au .env
    # actuel — cf. sync_prosody_accounts_with_env(), qui se fie à ce fichier
    # aux démarrages suivants pour ne plus jamais avoir besoin de ce script.
    grep -E '^(JICOFO_AUTH_PASSWORD|JVB_AUTH_PASSWORD)=' "$env_file" | sort | sha256sum | cut -d' ' -f1 \
        > "$prosody_storage/.civitas_auth_fingerprint" 2>/dev/null || true

    info "Redémarrage de Prosody (comptes recréés depuis $env_file)..."
    ( cd "$jitsi_dir" && docker compose up -d prosody ) \
        || die "Échec du redémarrage du conteneur prosody."

    log "Stockage Prosody réinitialisé — Jicofo/JVB devraient se réauthentifier automatiquement (boucle de reconnexion déjà active)."
}
