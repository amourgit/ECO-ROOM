#!/usr/bin/env bash
# =============================================================================
# CIVITAS — Réinitialisation des comptes XMPP internes de Prosody
#
# À utiliser quand `docker logs jitsi-jicofo-1` / `docker logs jitsi-jvb-1`
# montrent des erreurs répétées :
#   SASLError using SCRAM-SHA-1: not-authorized
# alors que la configuration (domaines, secrets dans .env) est par ailleurs
# cohérente — c'est le symptôme d'un stockage Prosody (${CONFIG}/storage/
# prosody) qui contient des comptes créés avec un ANCIEN mot de passe
# (gen-passwords.sh relancé, ou répertoire CONFIG réutilisé d'un essai
# Docker précédent). Prosody ne met jamais à jour le mot de passe d'un
# compte déjà enregistré — il faut repartir d'un stockage propre pour qu'il
# recrée les comptes depuis les valeurs ACTUELLES de .env.
#
# Ce script ne touche QUE ${CONFIG}/storage/prosody (comptes, roster,
# certificats auto-générés) — jamais ${CONFIG}/storage/web, ni aucun
# répertoire de configuration en lecture seule.
#
# Usage :
#   sudo bash scripts/jitsi_reset_prosody.sh          # demande confirmation
#   sudo bash scripts/jitsi_reset_prosody.sh --yes     # sans confirmation
#
# Variables d'environnement optionnelles :
#   JITSI_COMPOSE_DIR   Chemin du docker-compose.yml Jitsi, si non trouvé
#                        automatiquement (cf. scripts/lib/jitsi_common.sh)
# =============================================================================
set -uo pipefail

SCRIPT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
# shellcheck source=lib/jitsi_common.sh
source "$SCRIPT_DIR/lib/jitsi_common.sh"

echo ""
info "============================================================"
info " CIVITAS — Réinitialisation des comptes XMPP Prosody"
info "============================================================"

MODE_INFO=$(detect_jitsi_mode) || die "Aucun déploiement Jitsi détecté."
JITSI_MODE="${MODE_INFO%%:*}"
JITSI_DIR="${MODE_INFO#*:}"

[[ "$JITSI_MODE" == "docker" ]] || die "$(cat <<EOF
Ce script ne s'applique qu'au déploiement Docker (docker-jitsi-meet).
Détecté : $JITSI_MODE — rien à faire ici (les paquets natifs Debian
gèrent leurs comptes Prosody directement via prosodyctl, hors Docker).
EOF
)"

log "Déploiement Docker détecté : $JITSI_DIR"

if [[ "${1:-}" != "--yes" ]]; then
    warn "Ceci va arrêter Prosody, PURGER ${JITSI_DIR}/data/storage/prosody"
    warn "(comptes XMPP internes, roster, certificats auto-générés — pas les"
    warn "certificats web ni la configuration), puis le redémarrer."
    warn "Jicofo et JVB, déjà en boucle de reconnexion, se réauthentifieront"
    warn "automatiquement une fois les comptes recréés avec le .env actuel."
    read -r -p "Continuer ? [y/N] " REPLY
    [[ "$REPLY" =~ ^[Yy]$ ]] || die "Annulé."
fi

reset_prosody_account_storage "$JITSI_DIR"

echo ""
info "Vérification (max 60s, test TCP en loopback dans le conteneur prosody)..."
if wait_for_prosody_listening "$JITSI_DIR" 60; then
    log "Prosody écoute à nouveau sur le port ${XMPP_PORT:-5222}"
else
    err "Prosody ne s'est pas remis à écouter — voir : docker compose logs prosody --tail=100"
    exit 1
fi

echo ""
info "Pour confirmer que Jicofo/JVB se sont réauthentifiés :"
info "  cd $JITSI_DIR && docker compose logs jicofo --tail 20   # ne doit plus montrer 'not-authorized'"
info "  cd $JITSI_DIR && docker compose logs jvb --tail 20      # idem"
info "  sudo bash scripts/jitsi_boot.sh        # revérifie tout le stack, y compris"
info "                                          # la santé réelle de Jicofo (auth incluse)"
echo "============================================================"
