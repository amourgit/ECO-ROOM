#!/usr/bin/env bash

# =============================================================================
# CIVITAS — JITSI INFRASTRUCTURE AUDIT
# =============================================================================
#
# Objectif :
#   Inventorier une installation Jitsi Meet installée directement sur l'hôte.
#
# Composants recherchés :
#   - Prosody
#   - Jicofo
#   - Jitsi Videobridge (JVB)
#   - Jitsi Meet Web
#   - Nginx
#   - Coturn / TURN
#   - Let's Encrypt / TLS
#   - Systemd
#   - Java
#   - Node.js
#   - npm
#   - Lua
#   - Ports réseau
#   - Processus
#   - fichiers de configuration
#   - fichiers de données
#   - logs
#   - utilisateurs système
#   - cron / timers
#   - firewall
#   - Docker éventuel
#
# Le script est READ-ONLY.
# Il ne modifie PAS l'installation Jitsi existante.
# =============================================================================

set +e

BASE="/opt/civitas/jitsi-audit"
REPORT="/opt/civitas/JITSI_INFRASTRUCTURE_AUDIT.md"

mkdir -p "$BASE"

touch "$REPORT"

# -----------------------------------------------------------------------------
# Helpers
# -----------------------------------------------------------------------------

section() {
    local title="$1"

    {
        echo ""
        echo ""
        echo "---"
        echo ""
        echo "# $title"
        echo ""
        echo "**Date :** $(date '+%Y-%m-%d %H:%M:%S %Z')"
        echo ""
    } | tee -a "$REPORT"
}

subsection() {
    local title="$1"

    {
        echo ""
        echo "## $title"
        echo ""
    } | tee -a "$REPORT"
}

run_cmd() {
    local description="$1"
    shift

    echo "" | tee -a "$REPORT"
    echo '```text' | tee -a "$REPORT"
    echo "\$ $*" | tee -a "$REPORT"
    echo '```' | tee -a "$REPORT"

    "$@" 2>&1 | tee -a "$REPORT"

    echo "" | tee -a "$REPORT"
}

run_shell() {
    local description="$1"
    local command="$2"

    echo "" | tee -a "$REPORT"
    echo '```text' | tee -a "$REPORT"
    echo "\$ $command" | tee -a "$REPORT"
    echo '```' | tee -a "$REPORT"

    bash -c "$command" 2>&1 | tee -a "$REPORT"

    echo "" | tee -a "$REPORT"
}

run_to_file() {
    local filename="$1"
    shift

    "$@" > "$BASE/$filename" 2>&1
}

# -----------------------------------------------------------------------------
# Header
# -----------------------------------------------------------------------------

cat > "$REPORT" <<EOF
# CIVITAS — Jitsi Infrastructure Audit

> Inventaire de l'installation Jitsi directement installée sur le système.

**Rapport :** \`$REPORT\`

**Répertoire des données brutes :** \`$BASE\`

**Date de début :** $(date '+%Y-%m-%d %H:%M:%S %Z')

> Ce rapport est généré automatiquement.
>
> Le script est conçu pour effectuer des opérations de lecture uniquement.

EOF

# =============================================================================
# 1. SYSTEME
# =============================================================================

section "1. INFORMATIONS SYSTÈME"

subsection "Hostname"

run_cmd "hostname" hostname
run_cmd "hostnamectl" hostnamectl

subsection "OS"

run_cmd "Version OS" cat /etc/os-release
run_cmd "Kernel" uname -a
run_cmd "Architecture" uname -m

subsection "CPU / RAM / DISQUE"

run_cmd "CPU" lscpu
run_cmd "RAM" free -h
run_cmd "Disques" lsblk -o NAME,SIZE,FSTYPE,TYPE,MOUNTPOINTS
run_cmd "Filesystem" df -hT

# =============================================================================
# 2. PACKAGES JITSI
# =============================================================================

section "2. PAQUETS INSTALLÉS"

subsection "Recherche globale des paquets Jitsi"

run_shell "Paquets Jitsi" \
'dpkg -l 2>/dev/null | grep -Ei "jitsi|prosody|jicofo|videobridge|coturn|turnserver|nginx" || true'

subsection "Recherche avec apt"

run_shell "APT Jitsi" \
'apt list --installed 2>/dev/null | grep -Ei "jitsi|prosody|jicofo|videobridge|coturn|turnserver|nginx" || true'

subsection "Versions"

run_shell "Versions Jitsi" \
'dpkg-query -W -f="\${Package}\t\${Version}\n" 2>/dev/null | grep -Ei "jitsi|prosody|jicofo|videobridge|coturn|turnserver" || true'

# =============================================================================
# 3. SYSTEMD
# =============================================================================

section "3. SERVICES SYSTEMD"

subsection "Tous les services contenant Jitsi"

run_shell "systemctl Jitsi" \
'systemctl list-units --type=service --all 2>/dev/null | grep -Ei "jitsi|prosody|jicofo|jvb|videobridge|coturn|turnserver|nginx" || true'

subsection "Services activés"

run_shell "Services enabled" \
'systemctl list-unit-files 2>/dev/null | grep -Ei "jitsi|prosody|jicofo|jvb|videobridge|coturn|turnserver|nginx" || true'

subsection "Fichiers systemd"

run_shell "Systemd files" \
'find /etc/systemd /lib/systemd /usr/lib/systemd -type f 2>/dev/null | grep -Ei "jitsi|prosody|jicofo|jvb|videobridge|coturn|turnserver" || true'

subsection "Détails des services"

for service in \
    prosody \
    jicofo \
    jitsi-videobridge2 \
    jitsi-videobridge \
    coturn \
    turnserver \
    nginx
do
    echo "" | tee -a "$REPORT"
    echo "### Service : $service" | tee -a "$REPORT"
    run_cmd "systemctl status $service" systemctl status "$service" --no-pager
    run_cmd "systemctl cat $service" systemctl cat "$service"
done

# =============================================================================
# 4. PROSODY
# =============================================================================

section "4. PROSODY"

subsection "Binaire"

run_shell "Prosody binary" \
'command -v prosody 2>/dev/null || true'

run_shell "Prosody version" \
'prosodyctl --version 2>/dev/null || true'

subsection "Répertoires Prosody"

run_shell "Prosody directories" \
'find /etc/prosody /usr/lib/prosody /usr/share/prosody /var/lib/prosody /var/log/prosody -maxdepth 4 -print 2>/dev/null || true'

subsection "Configuration Prosody"

run_shell "Prosody configuration files" \
'find /etc/prosody -type f -print 2>/dev/null || true'

subsection "Configuration principale"

run_shell "prosody.cfg.lua" \
'cat /etc/prosody/prosody.cfg.lua 2>/dev/null || true'

subsection "Configurations Jitsi Prosody"

run_shell "Jitsi Prosody configs" \
'find /etc/prosody -type f -iname "*jitsi*" -o -iname "*meet*" 2>/dev/null | sort'

subsection "Virtual hosts"

run_shell "Prosody VirtualHosts" \
'grep -RniE "VirtualHost|Component|authentication|admins" /etc/prosody 2>/dev/null || true'

subsection "Modules"

run_shell "Prosody modules" \
'find /usr/lib/prosody /usr/share/prosody /etc/prosody -type f 2>/dev/null | grep -Ei "module|jitsi" | sort || true'

subsection "Utilisateurs Prosody"

run_shell "Prosody users" \
'prosodyctl list 2>/dev/null || true'

# =============================================================================
# 5. JICOFO
# =============================================================================

section "5. JICOFO"

subsection "Localisation"

run_shell "Jicofo files" \
'find /etc/jitsi /usr/share/jicofo /usr/share/jitsi /usr/lib/jicofo -type f 2>/dev/null | sort | grep -Ei "jicofo|jitsi" || true'

subsection "Configuration"

run_shell "Jicofo configuration" \
'find /etc/jitsi/jicofo -maxdepth 5 -type f -print 2>/dev/null || true'

subsection "Contenu configuration Jicofo"

run_shell "Jicofo configs" \
'for f in /etc/jitsi/jicofo/*; do [ -f "$f" ] && { echo "===== $f ====="; sed -n "1,240p" "$f"; }; done'

subsection "Service Jicofo"

run_cmd "Jicofo status" systemctl status jicofo --no-pager
run_cmd "Jicofo unit" systemctl cat jicofo

# =============================================================================
# 6. JITSI VIDEOBRIDGE
# =============================================================================

section "6. JITSI VIDEOBRIDGE (JVB)"

subsection "Localisation"

run_shell "JVB files" \
'find /etc/jitsi /usr/share/jitsi /usr/share/jitsi-videobridge /usr/lib/jitsi-videobridge -type f 2>/dev/null | sort | grep -Ei "videobridge|jvb|jitsi" || true'

subsection "Configuration JVB"

run_shell "JVB configuration directory" \
'find /etc/jitsi/videobridge -maxdepth 5 -type f -print 2>/dev/null || true'

subsection "Configurations JVB"

run_shell "JVB configs" \
'for f in /etc/jitsi/videobridge/*; do [ -f "$f" ] && { echo "===== $f ====="; sed -n "1,260p" "$f"; }; done'

subsection "JVB service"

run_cmd "JVB status" systemctl status jitsi-videobridge2 --no-pager
run_cmd "JVB unit" systemctl cat jitsi-videobridge2

# =============================================================================
# 7. JITSI MEET WEB
# =============================================================================

section "7. JITSI MEET WEB"

subsection "Répertoires"

run_shell "Jitsi web directories" \
'find /usr/share/jitsi-meet /etc/jitsi-meet /var/lib/jitsi-meet -maxdepth 4 -print 2>/dev/null || true'

subsection "Package"

run_shell "Jitsi Meet package" \
'dpkg -L jitsi-meet 2>/dev/null || true'

subsection "Configuration"

run_shell "Jitsi Meet configuration" \
'find /etc/jitsi -maxdepth 4 -type f -print 2>/dev/null | sort'

subsection "Fichiers JavaScript"

run_shell "Jitsi web JS" \
'find /usr/share/jitsi-meet -type f 2>/dev/null | grep -Ei "\.js$|config|interface_config|external_api" | head -500'

# =============================================================================
# 8. NGINX
# =============================================================================

section "8. NGINX"

subsection "Status"

run_cmd "Nginx status" systemctl status nginx --no-pager

subsection "Configuration"

run_shell "Nginx configuration files" \
'find /etc/nginx -type f -print 2>/dev/null | sort'

subsection "Sites"

run_shell "Nginx sites-enabled" \
'find /etc/nginx/sites-enabled /etc/nginx/sites-available -type f -maxdepth 2 -print 2>/dev/null | sort'

subsection "Recherche Jitsi"

run_shell "Nginx Jitsi configs" \
'grep -RniE "jitsi|prosody|xmpp|websocket|colibri|bosh|focus|meet" /etc/nginx 2>/dev/null || true'

subsection "Configuration complète"

run_cmd "nginx -T" nginx -T

# =============================================================================
# 9. CERTIFICATS TLS
# =============================================================================

section "9. CERTIFICATS TLS"

subsection "Let's Encrypt"

run_shell "Let's Encrypt" \
'find /etc/letsencrypt -maxdepth 5 -type f -print 2>/dev/null | sort || true'

subsection "Certificats"

run_shell "Certbot certificates" \
'certbot certificates 2>/dev/null || true'

subsection "Recherche certificats Jitsi"

run_shell "Jitsi certificates" \
'find /etc/jitsi /etc/prosody -type f 2>/dev/null | grep -Ei "\.(crt|pem|key)$" | sort || true'

# =============================================================================
# 10. COTURN
# =============================================================================

section "10. COTURN / TURN"

subsection "Paquet"

run_shell "Coturn package" \
'dpkg -l 2>/dev/null | grep -Ei "coturn|turnserver" || true'

subsection "Binaire"

run_shell "Turnserver binary" \
'command -v turnserver 2>/dev/null || true'

subsection "Configuration"

run_shell "Coturn configuration" \
'find /etc/turnserver /etc/coturn -type f -print 2>/dev/null || true'

subsection "Configuration principale"

run_shell "turnserver.conf" \
'cat /etc/turnserver.conf 2>/dev/null || true'

subsection "Systemd"

run_cmd "Coturn status" systemctl status coturn --no-pager
run_cmd "Turnserver status" systemctl status turnserver --no-pager

# =============================================================================
# 11. PORTS
# =============================================================================

section "11. PORTS RÉSEAU"

subsection "Tous les ports en écoute"

run_cmd "ss listening" ss -lntup

subsection "Ports Jitsi connus"

run_shell "Jitsi ports" \
'ss -lntup 2>/dev/null | grep -E ":80 |:443 |:5222 |:5269 |:5347 |:3478 |:5349 |:10000 |:4443 |:8080 |:8888 |:8443 " || true'

subsection "Processus liés aux ports"

run_shell "Jitsi sockets" \
'lsof -nP -iTCP -sTCP:LISTEN 2>/dev/null | grep -Ei "java|prosody|nginx|turn|jitsi|node" || true'

# =============================================================================
# 12. PROCESSUS
# =============================================================================

section "12. PROCESSUS"

subsection "Processus Jitsi"

run_shell "Jitsi processes" \
'ps auxww | grep -Ei "jitsi|prosody|jicofo|videobridge|jvb|turnserver|coturn|nginx" | grep -v grep || true'

subsection "Processus Java"

run_shell "Java processes" \
'ps auxww | grep java | grep -v grep || true'

subsection "Processus Prosody"

run_shell "Prosody processes" \
'ps auxww | grep prosody | grep -v grep || true'

# =============================================================================
# 13. FICHIERS JITSI SUR TOUT LE SYSTEME
# =============================================================================

section "13. RECHERCHE GLOBALE DES FICHIERS JITSI"

subsection "Noms contenant jitsi"

run_shell "find jitsi" \
'find / -xdev \( -iname "*jitsi*" -o -iname "*jicofo*" -o -iname "*videobridge*" -o -iname "*prosody*" \) -print 2>/dev/null | sort'

subsection "Configurations"

run_shell "Configuration files" \
'find /etc -xdev -type f 2>/dev/null | grep -Ei "jitsi|jicofo|videobridge|prosody|turnserver" | sort'

subsection "Services"

run_shell "Service files" \
'find /etc/systemd /lib/systemd /usr/lib/systemd -type f 2>/dev/null | grep -Ei "jitsi|jicofo|videobridge|prosody|turn" | sort'

# =============================================================================
# 14. /ETC/JITSI
# =============================================================================

section "14. /ETC/JITSI"

run_shell "/etc/jitsi tree" \
'find /etc/jitsi -print 2>/dev/null | sort || true'

# =============================================================================
# 15. /VAR/LIB
# =============================================================================

section "15. DONNÉES /VAR/LIB"

run_shell "Jitsi /var/lib" \
'find /var/lib -maxdepth 4 \( -iname "*jitsi*" -o -iname "*prosody*" -o -iname "*jicofo*" \) -print 2>/dev/null | sort'

# =============================================================================
# 16. /VAR/LOG
# =============================================================================

section "16. LOGS"

subsection "Répertoires"

run_shell "Jitsi logs" \
'find /var/log -maxdepth 4 \( -iname "*jitsi*" -o -iname "*prosody*" -o -iname "*jicofo*" -o -iname "*videobridge*" -o -iname "*turn*" \) -print 2>/dev/null | sort'

subsection "Journalctl"

run_shell "Journal Jicofo" \
'journalctl -u jicofo --no-pager -n 300 2>/dev/null || true'

run_shell "Journal JVB" \
'journalctl -u jitsi-videobridge2 --no-pager -n 300 2>/dev/null || true'

run_shell "Journal Prosody" \
'journalctl -u prosody --no-pager -n 300 2>/dev/null || true'

run_shell "Journal Coturn" \
'journalctl -u coturn --no-pager -n 300 2>/dev/null || true'

run_shell "Journal Nginx" \
'journalctl -u nginx --no-pager -n 300 2>/dev/null || true'

# =============================================================================
# 17. UTILISATEURS SYSTEME
# =============================================================================

section "17. UTILISATEURS ET GROUPES"

subsection "Utilisateurs Jitsi"

run_shell "Jitsi users" \
'getent passwd | grep -Ei "jitsi|prosody|jicofo|turn" || true'

subsection "Groupes"

run_shell "Jitsi groups" \
'getent group | grep -Ei "jitsi|prosody|jicofo|turn" || true'

subsection "Home directories"

run_shell "Home directories" \
'for u in jitsi jicofo prosody turnserver; do getent passwd "$u" 2>/dev/null; done'

# =============================================================================
# 18. JAVA
# =============================================================================

section "18. JAVA"

run_shell "Java version" \
'java -version 2>&1 || true'

run_shell "Java locations" \
'update-alternatives --list java 2>/dev/null || true'

run_shell "Java packages" \
'dpkg -l 2>/dev/null | grep -Ei "openjdk|java" || true'

# =============================================================================
# 19. NODE
# =============================================================================

section "19. NODE.JS"

run_shell "Node version" \
'node --version 2>/dev/null || true'

run_shell "npm version" \
'npm --version 2>/dev/null || true'

run_shell "Node binary" \
'command -v node 2>/dev/null || true'

run_shell "NPM packages" \
'npm list -g --depth=0 2>/dev/null || true'

# =============================================================================
# 20. LUA
# =============================================================================

section "20. LUA / PROSODY DEPENDENCIES"

run_shell "Lua version" \
'lua -v 2>&1 || true'

run_shell "Lua packages" \
'dpkg -l 2>/dev/null | grep -Ei "lua|prosody" || true'

run_shell "Lua modules" \
'find /usr/lib /usr/share -type f 2>/dev/null | grep -Ei "/lua/|prosody" | head -1000 || true'

# =============================================================================
# 21. FIREWALL
# =============================================================================

section "21. FIREWALL"

subsection "UFW"

run_shell "UFW status" \
'ufw status verbose 2>/dev/null || true'

subsection "iptables"

run_shell "iptables" \
'iptables -S 2>/dev/null || true'

subsection "iptables NAT"

run_shell "iptables NAT" \
'iptables -t nat -S 2>/dev/null || true'

subsection "nftables"

run_shell "nftables" \
'nft list ruleset 2>/dev/null || true'

# =============================================================================
# 22. CRON
# =============================================================================

section "22. CRON / TIMERS"

subsection "Cron"

run_shell "Cron Jitsi" \
'grep -RniE "jitsi|prosody|jicofo|videobridge|turn|certbot" /etc/cron* /var/spool/cron* 2>/dev/null || true'

subsection "Systemd timers"

run_shell "Systemd timers" \
'systemctl list-timers --all --no-pager 2>/dev/null'

# =============================================================================
# 23. CERTBOT
# =============================================================================

section "23. CERTBOT"

run_shell "Certbot version" \
'certbot --version 2>&1 || true'

run_shell "Certbot configuration" \
'find /etc/letsencrypt -type f -maxdepth 5 -print 2>/dev/null | sort || true'

run_shell "Certbot systemd" \
'systemctl list-unit-files 2>/dev/null | grep -i certbot || true'

# =============================================================================
# 24. DOCKER
# =============================================================================

section "24. DOCKER — POUR VÉRIFIER UNE INSTALLATION EXISTANTE"

run_shell "Docker version" \
'docker --version 2>/dev/null || true'

run_shell "Docker containers" \
'docker ps -a 2>/dev/null || true'

run_shell "Docker images" \
'docker images 2>/dev/null || true'

run_shell "Docker compose" \
'docker compose version 2>/dev/null || true'

# =============================================================================
# 25. DNS / HOSTNAME
# =============================================================================

section "25. DNS / HOSTNAME"

run_cmd "hostname" hostname -f

run_shell "Hosts" \
'cat /etc/hosts'

run_shell "Resolv" \
'cat /etc/resolv.conf'

run_shell "DNS Jitsi references" \
'grep -RniE "meet\.|jitsi|xmpp|conference\.|auth\.|focus\.|jvb\." /etc/hosts /etc/jitsi /etc/prosody 2>/dev/null || true'

# =============================================================================
# 26. RESEAU
# =============================================================================

section "26. RÉSEAU"

run_cmd "Interfaces" ip addr
run_cmd "Routes" ip route
run_cmd "IPv6 routes" ip -6 route

subsection "NetworkManager / systemd-networkd"

run_shell "NetworkManager" \
'nmcli connection show 2>/dev/null || true'

run_shell "systemd-networkd" \
'networkctl list 2>/dev/null || true'

# =============================================================================
# 27. VARIABLES ENVIRONNEMENT
# =============================================================================

section "27. VARIABLES D'ENVIRONNEMENT"

subsection "Environnement global"

run_shell "Environment" \
'env | sort'

subsection "Variables Jitsi"

run_shell "Jitsi environment variables" \
'env | grep -Ei "jitsi|jicofo|jvb|prosody|xmpp|turn" || true'

# =============================================================================
# 28. RECHERCHE DE FICHIERS ENV
# =============================================================================

section "28. FICHIERS ENVIRONNEMENT"

run_shell "Environment files" \
'find /etc /opt /var/lib /usr/local -type f \( -name ".env" -o -name "*.env" \) -print 2>/dev/null | sort'

# =============================================================================
# 29. RECHERCHE CONFIGURATION JITSI
# =============================================================================

section "29. RECHERCHE DE MOTS-CLÉS JITSI"

subsection "Configuration globale"

run_shell "Jitsi references in /etc" \
'grep -RniE "jitsi|jicofo|videobridge|prosody|xmpp|colibri|bosh|conference\.|focus\." /etc 2>/dev/null | head -5000 || true'

# =============================================================================
# 30. ARBRE DES RÉPERTOIRES PRINCIPAUX
# =============================================================================

section "30. ARBRE DE L'INSTALLATION"

subsection "/etc/jitsi"

run_shell "tree /etc/jitsi" \
'tree -a -L 6 /etc/jitsi 2>/dev/null || find /etc/jitsi -maxdepth 6 -print 2>/dev/null | sort'

subsection "/etc/prosody"

run_shell "tree /etc/prosody" \
'tree -a -L 6 /etc/prosody 2>/dev/null || find /etc/prosody -maxdepth 6 -print 2>/dev/null | sort'

subsection "/usr/share/jitsi-meet"

run_shell "tree Jitsi web" \
'tree -a -L 4 /usr/share/jitsi-meet 2>/dev/null || find /usr/share/jitsi-meet -maxdepth 4 -print 2>/dev/null | sort'

# =============================================================================
# 31. PAQUETS — FICHIERS EXACTS
# =============================================================================

section "31. FICHIERS FOURNIS PAR LES PAQUETS"

for package in \
    jitsi-meet \
    jitsi-meet-web \
    jitsi-meet-web-config \
    jitsi-meet-prosody \
    jitsi-meet-turnserver \
    jicofo \
    jitsi-videobridge2 \
    prosody \
    coturn \
    nginx
do
    subsection "Package : $package"

    run_shell "dpkg -L $package" \
        "dpkg -L '$package' 2>/dev/null || true"
done

# =============================================================================
# 32. DEPENDANCES
# =============================================================================

section "32. DÉPENDANCES DES PAQUETS"

for package in \
    jitsi-meet \
    jicofo \
    jitsi-videobridge2 \
    jitsi-meet-prosody \
    jitsi-meet-turnserver
do
    subsection "$package"

    run_shell "Dependencies" \
        "apt-cache depends '$package' 2>/dev/null || true"
done

# =============================================================================
# 33. VERSION EXACTE
# =============================================================================

section "33. VERSIONS EXACTES"

run_shell "Jitsi versions" \
'dpkg-query -W -f="${Package} ${Version}\n" 2>/dev/null | grep -Ei "jitsi|jicofo|prosody|coturn" || true'

run_shell "Kernel" \
'uname -r'

run_shell "OS" \
'cat /etc/os-release'

run_shell "Java" \
'java -version 2>&1 || true'

run_shell "Node" \
'node -v 2>/dev/null || true'

run_shell "Prosody" \
'prosodyctl --version 2>/dev/null || true'

# =============================================================================
# 34. RÉSUMÉ AUTOMATIQUE
# =============================================================================

section "34. RÉSUMÉ AUTOMATIQUE"

subsection "Services détectés"

run_shell "Detected services" \
'systemctl list-unit-files 2>/dev/null | grep -Ei "jitsi|prosody|jicofo|videobridge|jvb|coturn|turnserver|nginx" || true'

subsection "Ports détectés"

run_shell "Detected ports" \
'ss -lntup 2>/dev/null | grep -Ei "java|prosody|nginx|turn|jitsi|node" || true'

subsection "Processus détectés"

run_shell "Detected processes" \
'ps auxww 2>/dev/null | grep -Ei "jitsi|prosody|jicofo|videobridge|jvb|turnserver|coturn|nginx" | grep -v grep || true'

# =============================================================================
# 35. FIN
# =============================================================================

cat >> "$REPORT" <<EOF

---

# FIN DE L'AUDIT

**Date de fin :** $(date '+%Y-%m-%d %H:%M:%S %Z')

## Fichiers générés

- Rapport principal :
  \`$REPORT\`

- Données brutes :
  \`$BASE/\`

## Objectif suivant

À partir de cet inventaire, reconstruire l'architecture Jitsi sous Docker Compose :

\`\`\`
Internet
   |
   v
Reverse Proxy / Nginx
   |
   +-----------------------+
   |                       |
   v                       v
Jitsi Meet Web          Prosody
                           |
                           +---- Jicofo
                           |
                           +---- JVB
                           |
                           +---- TURN / Coturn
\`\`\`

L'objectif est de reproduire les fonctionnalités de l'installation actuelle
sans modifier cette dernière pendant la phase d'analyse.

EOF

echo ""
echo "=============================================================="
echo " AUDIT JITSI TERMINÉ"
echo "=============================================================="
echo ""
echo "Rapport : $REPORT"
echo "Données : $BASE"
echo ""
