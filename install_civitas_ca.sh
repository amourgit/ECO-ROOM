#!/usr/bin/env bash
# =============================================================================
# CIVITAS — Installation CA interne sur machine cliente
# À exécuter sur chaque poste qui accède à meet.civitas.local
#
# Ce script tourne sur la machine CLIENTE (pas sur le serveur CIVITAS) : il
# ne peut donc pas auto-détecter l'IP du serveur (contrairement à
# 01_system_base.sh, qui lui tourne sur le serveur et détecte sa propre IP).
# L'IP doit être fournie explicitement — jamais supposée.
#
# Usage :
#   sudo bash install_civitas_ca.sh <IP_SERVEUR>
#   CIVITAS_SERVER_IP=x.x.x.x sudo -E bash install_civitas_ca.sh
# =============================================================================
set -euo pipefail

log()  { echo -e "\033[0;32m[✓]\033[0m $*"; }
info() { echo -e "\033[0;34m[→]\033[0m $*"; }
die()  { echo -e "\033[0;31m[✗]\033[0m $*" >&2; exit 1; }

SERVER_IP="${1:-${CIVITAS_SERVER_IP:-}}"
if [[ -z "$SERVER_IP" ]]; then
    die "IP du serveur CIVITAS requise.
  Usage : sudo bash install_civitas_ca.sh <IP_SERVEUR>
  (ou)   CIVITAS_SERVER_IP=x.x.x.x sudo -E bash install_civitas_ca.sh

  L'IP du serveur est affichée à la fin de 01_system_base.sh (section
  'ACTION REQUISE'), ou récupérable via : cat /opt/civitas/config/civitas.env | grep CIVITAS_IP"
fi

[[ $EUID -eq 0 ]] || die "Exécuter en root"

OS=$(uname -s)

if [[ "$OS" == "Linux" ]]; then
    # Debian/Ubuntu
    if command -v apt-get &>/dev/null; then
        info "Installation CA sur Debian/Ubuntu..."
        # Option 1 : via scp depuis le serveur
        info "Copie de la CA depuis le serveur..."
        scp civitas@${SERVER_IP}:/opt/civitas/certs/ca/rootCA.pem \
            /usr/local/share/ca-certificates/civitas-ca.crt
        update-ca-certificates --fresh
        log "CA installée (Debian/Ubuntu)"
    fi

    # Ajouter DNS dans /etc/hosts si dnsmasq non dispo
    info "Ajout des entrées DNS dans /etc/hosts..."
    grep -q "meet.civitas.local" /etc/hosts || \
        echo "${SERVER_IP}  meet.civitas.local civitas.local kafka-ui.civitas.local grafana.civitas.local" \
        >> /etc/hosts
    log "DNS /etc/hosts mis à jour"

elif [[ "$OS" == "Darwin" ]]; then
    info "Installation CA sur macOS..."
    SCP_PATH="/tmp/civitas-ca.pem"
    scp civitas@${SERVER_IP}:/opt/civitas/certs/ca/rootCA.pem "$SCP_PATH"
    sudo security add-trusted-cert -d -r trustRoot \
        -k /Library/Keychains/System.keychain "$SCP_PATH"
    log "CA installée (macOS)"

    # /etc/hosts
    grep -q "meet.civitas.local" /etc/hosts || \
        echo "${SERVER_IP}  meet.civitas.local civitas.local" >> /etc/hosts
fi

echo ""
echo "============================================"
echo " CA Civitas installée avec succès"
echo " meet.civitas.local → ${SERVER_IP}"
echo "============================================"
