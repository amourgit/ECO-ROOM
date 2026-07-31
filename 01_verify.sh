#!/usr/bin/env bash
# =============================================================================
# CIVITAS — Vérification étape 1
# Valide que toutes les fondations sont correctement installées
# Usage : bash 01_verify.sh
# =============================================================================
set -uo pipefail

GREEN='\033[0;32m'; RED='\033[0;31m'; YELLOW='\033[1;33m'
BOLD='\033[1m'; NC='\033[0m'

ok=0; fail=0

check() {
    local desc="$1"; shift
    if "$@" &>/dev/null 2>&1; then
        echo -e "  ${GREEN}✓${NC} $desc"
        ((ok++))
    else
        echo -e "  ${RED}✗${NC} $desc"
        ((fail++))
    fi
}

echo ""
echo -e "${BOLD}CIVITAS — Vérification étape 1${NC}"
echo "======================================"

echo ""
echo -e "${BOLD}Système${NC}"
check "Utilisateur civitas existe"        id civitas
check "Répertoire /opt/civitas existe"    test -d /opt/civitas
check "Config env existe"                 test -f /opt/civitas/config/civitas.env

echo ""
echo -e "${BOLD}Réseau${NC}"
check "UFW actif"                         systemctl is-active ufw
check "fail2ban actif"                    systemctl is-active fail2ban
check "Port SSH ouvert (22)"              bash -c "ufw status | grep -q '22/tcp'"

echo ""
echo -e "${BOLD}Docker${NC}"
check "Docker installé"                   command -v docker
check "Docker actif"                      systemctl is-active docker
check "Réseau civitas-net existe"         docker network inspect civitas-net
check "civitas dans groupe docker"        id civitas | grep -q docker

echo ""
echo -e "${BOLD}DNS${NC}"
check "dnsmasq actif"                     systemctl is-active dnsmasq
check "meet.civitas.local résolu"         host meet.civitas.local 127.0.0.1
check "kafka.civitas.local résolu"        host kafka.civitas.local 127.0.0.1
check "grafana.civitas.local résolu"      host grafana.civitas.local 127.0.0.1

echo ""
echo -e "${BOLD}Certificats TLS${NC}"
check "mkcert installé"                   command -v mkcert
check "Certificat civitas.local.crt"      test -f /opt/civitas/certs/civitas.local.crt
check "Clé privée civitas.local.key"      test -f /opt/civitas/certs/civitas.local.key
check "CA rootCA.pem"                     test -f /opt/civitas/certs/ca/rootCA.pem
check "CA dans store système"             test -f /usr/local/share/ca-certificates/civitas-ca.crt

echo ""
echo -e "${BOLD}Kernel${NC}"
check "IP Forward activé"                 bash -c "sysctl net.ipv4.ip_forward | grep -q '= 1'"
check "TCP BBR actif"                     bash -c "sysctl net.ipv4.tcp_congestion_control | grep -q bbr"

echo ""
echo "======================================"
echo -e "  ${GREEN}Succès : $ok${NC}   ${RED}Échecs : $fail${NC}"
echo ""
if [[ $fail -eq 0 ]]; then
    echo -e "${GREEN}${BOLD}  Étape 1 validée — prêt pour l'étape 2 (Jitsi)${NC}"
else
    echo -e "${RED}  $fail vérification(s) échouée(s) — corriger avant de continuer${NC}"
fi
echo ""
