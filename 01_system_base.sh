#!/usr/bin/env bash
# =============================================================================
# CIVITAS PLATFORM — Étape 1 : Fondations système
# Debian minimale · IP détectée dynamiquement · Qualité production
#
# Usage : sudo bash 01_system_base.sh
# Variables d'environnement optionnelles (si l'auto-détection ne convient
# pas, par exemple sur une machine multi-cartes réseau) :
#   CIVITAS_IP       Force l'IP du serveur (défaut : auto-détectée)
#   CIVITAS_SUBNET   Force le sous-réseau CIDR pour les règles UFW internes
#                    (défaut : auto-détecté depuis l'interface principale)
# =============================================================================
set -euo pipefail
IFS=$'\n\t'

# --- Couleurs -----------------------------------------------------------------
RED='\033[0;31m'; GREEN='\033[0;32m'; YELLOW='\033[1;33m'
BLUE='\033[0;34m'; BOLD='\033[1m'; NC='\033[0m'

log()  { echo -e "${GREEN}[✓]${NC} $*"; }
info() { echo -e "${BLUE}[→]${NC} $*"; }
warn() { echo -e "${YELLOW}[!]${NC} $*"; }
die()  { echo -e "${RED}[✗] ERREUR : $*${NC}" >&2; exit 1; }

# --- Vérifications préalables -------------------------------------------------
[[ $EUID -eq 0 ]] || die "Ce script doit être exécuté en root (sudo)"

export DEBIAN_FRONTEND=noninteractive

# --- Détection dynamique de l'IP et du sous-réseau du serveur ---------------
# Jamais d'IP en dur : détectée via la route par défaut (celle que le noyau
# utiliserait pour sortir vers Internet), avec override possible via
# CIVITAS_IP/CIVITAS_SUBNET pour les cas où l'auto-détection ne suffit pas.
detect_server_ip() {
    if [[ -n "${CIVITAS_IP:-}" ]]; then
        echo "$CIVITAS_IP"
        return 0
    fi
    ip -4 route get 1.1.1.1 2>/dev/null | awk '{for(i=1;i<=NF;i++) if ($i=="src") print $(i+1)}'
}

detect_server_cidr() {
    if [[ -n "${CIVITAS_SUBNET:-}" ]]; then
        echo "$CIVITAS_SUBNET"
        return 0
    fi
    local iface
    iface=$(ip -4 route get 1.1.1.1 2>/dev/null | awk '{for(i=1;i<=NF;i++) if ($i=="dev") print $(i+1)}')
    [[ -z "$iface" ]] && return 1
    ip -o -4 addr show dev "$iface" scope global 2>/dev/null | awk '{print $4}' | head -1
}

SERVER_IP="$(detect_server_ip)"
[[ -n "$SERVER_IP" ]] || die "Impossible de détecter l'IP du serveur automatiquement. Relancer avec : CIVITAS_IP=x.x.x.x sudo -E bash 01_system_base.sh"

SERVER_CIDR="$(detect_server_cidr)"
[[ -n "$SERVER_CIDR" ]] || die "Impossible de détecter le sous-réseau du serveur automatiquement. Relancer avec : CIVITAS_SUBNET=x.x.x.x/24 sudo -E bash 01_system_base.sh"

info "============================================================"
info " CIVITAS PLATFORM — Fondations système"
info " Debian minimale · $(date '+%Y-%m-%d %H:%M')"
info "============================================================"
info " IP serveur détectée     : $SERVER_IP"
info " Sous-réseau détecté     : $SERVER_CIDR"
info "============================================================"
warn "Si l'une de ces valeurs est incorrecte, interrompre (Ctrl+C) et relancer avec :"
warn "  CIVITAS_IP=x.x.x.x CIVITAS_SUBNET=x.x.x.x/24 sudo -E bash 01_system_base.sh"
sleep 5

# =============================================================================
# 1. MISE À JOUR DU SYSTÈME
# =============================================================================
info "Mise à jour du système..."
apt-get update -qq
apt-get upgrade -y -qq
apt-get install -y -qq \
    curl wget git vim htop \
    net-tools iputils-ping dnsutils \
    ca-certificates gnupg lsb-release \
    software-properties-common \
    apt-transport-https \
    openssl unzip jq \
    ufw fail2ban \
    sudo tree \
    2>/dev/null

log "Système mis à jour"

# =============================================================================
# 2. UTILISATEUR DÉDIÉ : civitas
# =============================================================================
info "Création de l'utilisateur civitas..."

if id "civitas" &>/dev/null; then
    warn "Utilisateur civitas existe déjà — skip"
else
    useradd -m -s /bin/bash -c "Civitas Platform" civitas
    usermod -aG sudo civitas
    # Mot de passe désactivé (accès SSH par clé uniquement)
    passwd -l civitas
    log "Utilisateur civitas créé"
fi

# Répertoire de travail
mkdir -p /opt/civitas/{config,certs,logs,data,scripts}
chown -R civitas:civitas /opt/civitas
chmod 750 /opt/civitas
chmod 700 /opt/civitas/certs

log "Structure /opt/civitas créée"

# =============================================================================
# 3. SÉCURITÉ SSH
# =============================================================================
info "Hardening SSH..."

SSH_CONFIG="/etc/ssh/sshd_config.d/99-civitas.conf"
cat > "$SSH_CONFIG" <<'EOF'
# CIVITAS — SSH hardening
Protocol 2
PermitRootLogin no
PasswordAuthentication yes
PubkeyAuthentication yes
AuthorizedKeysFile .ssh/authorized_keys
MaxAuthTries 3
LoginGraceTime 30
ClientAliveInterval 300
ClientAliveCountMax 2
AllowUsers civitas
X11Forwarding no
AllowTcpForwarding no
EOF

chmod 644 "$SSH_CONFIG"
systemctl reload sshd
log "SSH durci"

# =============================================================================
# 4. FIREWALL UFW
# =============================================================================
info "Configuration du firewall..."

ufw --force reset
ufw default deny incoming
ufw default allow outgoing

# SSH
ufw allow 22/tcp comment "SSH"

# HTTP/HTTPS (Nginx + Jitsi)
ufw allow 80/tcp  comment "HTTP"
ufw allow 443/tcp comment "HTTPS"

# Jitsi Videobridge (UDP média)
ufw allow 10000/udp comment "JVB media"

# TURN/STUN (Coturn)
ufw allow 3478/tcp  comment "TURN TCP"
ufw allow 3478/udp  comment "TURN UDP"
ufw allow 5349/tcp  comment "TURNS TLS"
ufw allow 5349/udp  comment "TURNS TLS UDP"
ufw allow 49152:65535/udp comment "TURN relay range"

# Kafka (interne uniquement)
ufw allow from "$SERVER_CIDR" to any port 9092  comment "Kafka interne"
ufw allow from "$SERVER_CIDR" to any port 9093  comment "Kafka controller"

# Grafana (interne uniquement)
ufw allow from "$SERVER_CIDR" to any port 3000  comment "Grafana interne"

# Kafka UI (interne uniquement) — le conteneur kafka-ui publie réellement
# 8090 (cf. kafka/docker-compose.yml : SERVER_PORT / ports "8090:8090"),
# pas 8080 : garder ce port aligné avec le compose sous peine de bloquer
# l'accès à l'interface par le firewall.
ufw allow from "$SERVER_CIDR" to any port 8090  comment "Kafka UI interne"

# Prosody XMPP (interne)
ufw allow from 127.0.0.1 to any port 5222 comment "XMPP client local"
ufw allow from 127.0.0.1 to any port 5269 comment "XMPP server local"

ufw --force enable
log "Firewall configuré"
ufw status verbose

# =============================================================================
# 5. FAIL2BAN
# =============================================================================
info "Configuration fail2ban..."

cat > /etc/fail2ban/jail.d/civitas.conf <<'EOF'
[DEFAULT]
bantime  = 3600
findtime = 600
maxretry = 5
backend  = systemd

[sshd]
enabled  = true
port     = ssh
logpath  = %(sshd_log)s
maxretry = 3
bantime  = 86400
EOF

systemctl enable fail2ban --quiet
systemctl restart fail2ban
log "fail2ban actif"

# =============================================================================
# 6. DOCKER
# =============================================================================
info "Installation de Docker..."

if command -v docker &>/dev/null; then
    warn "Docker déjà installé — $(docker --version)"
else
    install -m 0755 -d /etc/apt/keyrings
    curl -fsSL https://download.docker.com/linux/debian/gpg \
        | gpg --dearmor -o /etc/apt/keyrings/docker.gpg
    chmod a+r /etc/apt/keyrings/docker.gpg

    echo \
      "deb [arch=$(dpkg --print-architecture) \
      signed-by=/etc/apt/keyrings/docker.gpg] \
      https://download.docker.com/linux/debian \
      $(lsb_release -cs) stable" \
      > /etc/apt/sources.list.d/docker.list

    apt-get update -qq
    apt-get install -y -qq \
        docker-ce docker-ce-cli containerd.io \
        docker-buildx-plugin docker-compose-plugin

    log "Docker installé — $(docker --version)"
fi

# Ajouter civitas au groupe docker
usermod -aG docker civitas

# Configuration Docker daemon — production
mkdir -p /etc/docker
cat > /etc/docker/daemon.json <<'EOF'
{
  "log-driver": "json-file",
  "log-opts": {
    "max-size": "50m",
    "max-file": "5"
  },
  "storage-driver": "overlay2",
  "live-restore": true,
  "userland-proxy": false,
  "default-ulimits": {
    "nofile": {
      "Name": "nofile",
      "Hard": 65536,
      "Soft": 65536
    }
  }
}
EOF

systemctl enable docker --quiet
systemctl restart docker
log "Docker configuré (production)"

# Réseau Docker dédié Civitas
docker network create civitas-net \
    --driver bridge \
    --subnet 172.20.0.0/16 \
    --gateway 172.20.0.1 \
    2>/dev/null || warn "Réseau civitas-net existe déjà"

log "Réseau Docker civitas-net créé (172.20.0.0/16)"

# =============================================================================
# 7. DNSMASQ — résolution civitas.local
# =============================================================================
info "Installation et configuration dnsmasq..."

apt-get install -y -qq dnsmasq

# Sauvegarde config originale
cp /etc/dnsmasq.conf /etc/dnsmasq.conf.bak 2>/dev/null || true

cat > /etc/dnsmasq.conf <<EOF
# CIVITAS — dnsmasq configuration
# Généré le $(date '+%Y-%m-%d %H:%M')

# Interface d'écoute
interface=lo
bind-interfaces

# Pas de résolution depuis /etc/hosts sauf entrées explicites
no-hosts

# Domaine local civitas
local=/civitas.local/

# Entrées DNS civitas.local
address=/meet.civitas.local/$SERVER_IP
address=/civitas.local/$SERVER_IP
address=/kafka.civitas.local/$SERVER_IP
address=/grafana.civitas.local/$SERVER_IP
address=/kafka-ui.civitas.local/$SERVER_IP
address=/jibri.civitas.local/$SERVER_IP

# Upstream DNS (Cloudflare + Google fallback)
server=1.1.1.1
server=8.8.8.8

# Cache
cache-size=1000
neg-ttl=60

# Logs
log-queries=extra
log-facility=/var/log/dnsmasq.log
EOF

# Désactiver systemd-resolved si présent (conflit port 53)
if systemctl is-active --quiet systemd-resolved 2>/dev/null; then
    systemctl disable systemd-resolved --quiet
    systemctl stop systemd-resolved
    rm -f /etc/resolv.conf
    echo "nameserver 127.0.0.1" > /etc/resolv.conf
    echo "nameserver 1.1.1.1"  >> /etc/resolv.conf
    warn "systemd-resolved désactivé"
fi

systemctl enable dnsmasq --quiet
systemctl restart dnsmasq

log "dnsmasq configuré"

# Test résolution
sleep 1
if host meet.civitas.local 127.0.0.1 &>/dev/null; then
    log "DNS meet.civitas.local → $SERVER_IP ✓"
else
    warn "DNS test échoué — vérifier dnsmasq"
fi

# =============================================================================
# 8. MKCERT — CA interne + certificats TLS
# =============================================================================
info "Installation mkcert et génération CA interne..."

MKCERT_VERSION="v1.4.4"
ARCH=$(uname -m)
case $ARCH in
    x86_64)  MKCERT_BIN="mkcert-${MKCERT_VERSION}-linux-amd64" ;;
    aarch64) MKCERT_BIN="mkcert-${MKCERT_VERSION}-linux-arm64" ;;
    *)       die "Architecture non supportée : $ARCH" ;;
esac

if ! command -v mkcert &>/dev/null; then
    curl -fsSL \
        "https://github.com/FiloSottile/mkcert/releases/download/${MKCERT_VERSION}/${MKCERT_BIN}" \
        -o /usr/local/bin/mkcert
    chmod +x /usr/local/bin/mkcert
    log "mkcert installé"
fi

# Installer la CA locale
export CAROOT="/opt/civitas/certs/ca"
mkdir -p "$CAROOT"
mkcert -install

# Générer les certificats pour tous les sous-domaines
cd /opt/civitas/certs

mkcert \
    "civitas.local" \
    "*.civitas.local" \
    "meet.civitas.local" \
    "kafka.civitas.local" \
    "grafana.civitas.local" \
    "kafka-ui.civitas.local" \
    "$SERVER_IP" \
    "localhost" \
    "127.0.0.1"

# Renommer pour clarté
mv civitas.local+8.pem     civitas.local.crt 2>/dev/null || \
    mv *+*.pem              civitas.local.crt 2>/dev/null || true
mv civitas.local+8-key.pem civitas.local.key 2>/dev/null || \
    mv *+*-key.pem          civitas.local.key 2>/dev/null || true

chmod 644 /opt/civitas/certs/civitas.local.crt
chmod 600 /opt/civitas/certs/civitas.local.key
chown civitas:civitas /opt/civitas/certs/*.crt
chown civitas:civitas /opt/civitas/certs/*.key

# Copier la CA dans le store système
cp "${CAROOT}/rootCA.pem" /usr/local/share/ca-certificates/civitas-ca.crt
update-ca-certificates --fresh --quiet

log "Certificats TLS générés :"
log "  Cert : /opt/civitas/certs/civitas.local.crt"
log "  Clé  : /opt/civitas/certs/civitas.local.key"
log "  CA   : ${CAROOT}/rootCA.pem"

# =============================================================================
# 9. PARAMÈTRES KERNEL — performance réseau
# =============================================================================
info "Optimisation kernel réseau..."

cat > /etc/sysctl.d/99-civitas.conf <<'EOF'
# CIVITAS — optimisations réseau production

# Buffers réseau
net.core.rmem_max          = 134217728
net.core.wmem_max          = 134217728
net.core.netdev_max_backlog = 5000

# TCP
net.ipv4.tcp_rmem = 4096 87380 134217728
net.ipv4.tcp_wmem = 4096 65536 134217728
net.ipv4.tcp_congestion_control = bbr
net.ipv4.tcp_slow_start_after_idle = 0

# File descriptors
fs.file-max = 2097152

# WebRTC UDP (important pour JVB)
net.core.rmem_default = 26214400
net.core.wmem_default = 26214400

# IP Forward (Docker)
net.ipv4.ip_forward = 1
EOF

sysctl -p /etc/sysctl.d/99-civitas.conf --quiet
log "Kernel optimisé"

# Limites système
cat > /etc/security/limits.d/civitas.conf <<'EOF'
civitas soft nofile 65536
civitas hard nofile 65536
civitas soft nproc  65536
civitas hard nproc  65536
root    soft nofile 65536
root    hard nofile 65536
EOF

log "Limites système configurées"

# =============================================================================
# 10. FICHIER D'ENVIRONNEMENT GLOBAL
# =============================================================================
info "Création du fichier d'environnement global..."

cat > /opt/civitas/config/civitas.env <<EOF
# CIVITAS PLATFORM — Variables d'environnement globales
# Généré le $(date '+%Y-%m-%d %H:%M')
# NE PAS COMMITTER CE FICHIER

# Réseau
CIVITAS_DOMAIN=civitas.local
CIVITAS_IP=$SERVER_IP
CIVITAS_SUBNET=$SERVER_CIDR

# Domaines
JITSI_DOMAIN=meet.civitas.local
KAFKA_DOMAIN=kafka.civitas.local
GRAFANA_DOMAIN=grafana.civitas.local
KAFKA_UI_DOMAIN=kafka-ui.civitas.local

# Certificats
TLS_CERT=/opt/civitas/certs/civitas.local.crt
TLS_KEY=/opt/civitas/certs/civitas.local.key
CA_CERT=/opt/civitas/certs/ca/rootCA.pem

# Docker réseau
DOCKER_NETWORK=civitas-net
DOCKER_SUBNET=172.20.0.0/16

# Ports exposés
JITSI_HTTP_PORT=80
JITSI_HTTPS_PORT=443
JVB_PORT=10000
COTURN_PORT=3478
# Listener PLAINTEXT externe uniquement (clients hors réseau Docker).
# Les services CIVITAS internes (peer, room-spawner, room-config) utilisent
# TOUJOURS civitas-kafka:9094 (listener INTERNAL), jamais cette IP/port —
# cf. kafka/docker-compose.yml et README.md § Kafka.
KAFKA_PORT=9092
GRAFANA_PORT=3000
KAFKA_UI_PORT=8090
EOF

chmod 640 /opt/civitas/config/civitas.env
chown civitas:civitas /opt/civitas/config/civitas.env

log "Environnement global : /opt/civitas/config/civitas.env"

# =============================================================================
# RÉSUMÉ FINAL
# =============================================================================
echo ""
echo -e "${BOLD}============================================================${NC}"
echo -e "${GREEN}  ÉTAPE 1 TERMINÉE — Fondations système${NC}"
echo -e "${BOLD}============================================================${NC}"
echo ""
echo -e "  ${GREEN}✓${NC} Système Debian mis à jour"
echo -e "  ${GREEN}✓${NC} Utilisateur civitas créé (/opt/civitas)"
echo -e "  ${GREEN}✓${NC} SSH durci (pas de root, max 3 essais)"
echo -e "  ${GREEN}✓${NC} Firewall UFW configuré"
echo -e "  ${GREEN}✓${NC} fail2ban actif (ban 24h après 3 échecs SSH)"
echo -e "  ${GREEN}✓${NC} Docker installé et configuré (production)"
echo -e "  ${GREEN}✓${NC} Réseau Docker civitas-net (172.20.0.0/16)"
echo -e "  ${GREEN}✓${NC} dnsmasq — civitas.local résolu sur $SERVER_IP"
echo -e "  ${GREEN}✓${NC} mkcert — CA interne + certificats wildcard *.civitas.local"
echo -e "  ${GREEN}✓${NC} Kernel optimisé (WebRTC, TCP BBR)"
echo -e "  ${GREEN}✓${NC} /opt/civitas/config/civitas.env"
echo ""
echo -e "${YELLOW}  ACTION REQUISE :${NC}"
echo -e "  Sur chaque machine cliente du réseau, ajouter dans /etc/hosts :"
echo -e "  ${BOLD}$SERVER_IP  meet.civitas.local civitas.local${NC}"
echo -e ""
echo -e "  Ou configurer le DNS du routeur sur $SERVER_IP"
echo -e ""
echo -e "  Installer la CA sur les clients :"
echo -e "  ${BOLD}scp civitas@$SERVER_IP:/opt/civitas/certs/ca/rootCA.pem .${NC}"
echo -e "  ${BOLD}sudo bash install_civitas_ca.sh $SERVER_IP${NC}  (cf. script fourni)"
echo -e ""
echo -e "${BLUE}  Prêt pour l'étape 2 : Jitsi Meet${NC}"
echo ""
