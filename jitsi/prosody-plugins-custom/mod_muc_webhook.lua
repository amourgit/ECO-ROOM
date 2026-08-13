-- mod_muc_webhook.lua
-- Envoie les événements MUC de Prosody vers event-bridge (CIVITAS).
--
-- Module custom CIVITAS (absent de la distribution standard jitsi-meet).
-- Corrigé le 2026-08-13 après audit complet — cf.
-- PLAN_SYNCHRONISATION_ROOMS_JITSI.md §1-4/§7.7. Trois bugs réels dans la
-- version précédente (nginx/jitsi-meet-host-backup/prosody-plugins/,
-- copie de l'installation native, jamais corrigée pour le contexte Docker) :
--
--   1. URL par défaut "http://127.0.0.1:8100/webhook" — valide seulement
--      si Prosody et event-bridge tournent SUR LE MÊME HÔTE (install
--      native). En Docker, 127.0.0.1 dans le conteneur prosody ne route
--      JAMAIS vers un autre conteneur : le webhook échouait silencieusement
--      (connexion refusée, juste un warning en log) — jamais un seul
--      événement ne pouvait atteindre event-bridge.
--   2. Champ envoyé "occupant" = occupant.nick, qui en Prosody est le JID
--      COMPLET dans la room (room@muc.host/Pseudo), pas juste un pseudo —
--      et de toute façon event-bridge lit "occupant_jid"/"occupant_nick"/
--      "role"/"affiliation", aucun de ces noms n'était envoyé. Résultat :
--      tout événement de présence (join/leave) retombait sur des valeurs
--      vides côté event-bridge, et plusieurs participants distincts
--      s'écrasaient les uns les autres dans le suivi de présence (même clé
--      "" pour tout le monde).
--   3. Aucune authentification — n'importe qui pouvait se faire passer
--      pour Prosody en POSTant directement sur event-bridge.
--
-- Configuration (prosody.cfg.lua, section du composant MUC — injectée via
-- la variable d'environnement XMPP_MUC_CONFIGURATION du docker-compose
-- Jitsi, cf. jitsi/.env.example) :
--   muc_webhook_url    = "http://civitas-event-bridge:8100/webhook"
--   muc_webhook_secret = "<le même secret que WEBHOOK_SECRET côté event-bridge>"
--
-- Chargé via XMPP_MUC_MODULES=muc_webhook (cf. jitsi/.env.example) — DOIT
-- être un module MUC (pas XMPP_MODULES) car il hook des événements
-- muc-room-*/muc-occupant-* qui n'existent que dans le composant MUC.

local http = require "net.http";
local json = require "util.json";
local jid_split = require "util.jid".split;
local module_host = module.host;

local webhook_url = module:get_option_string("muc_webhook_url", "http://civitas-event-bridge:8100/webhook");
local webhook_secret = module:get_option_string("muc_webhook_secret", nil);

if not webhook_secret then
    module:log("warn", "muc_webhook_secret non configuré — les événements seront envoyés SANS authentification, event-bridge les rejettera (401)");
end

-- occupant.nick est le JID complet dans la room ("room@muc.host/Pseudo") —
-- on en extrait juste la ressource (le pseudo affiché).
local function occupant_display_nick(occupant)
    if not occupant or not occupant.nick then
        return nil;
    end
    local _, _, resource = jid_split(occupant.nick);
    return resource;
end

local function occupant_affiliation(room, occupant)
    if not room or not occupant or not occupant.bare_jid then
        return nil;
    end
    return room:get_affiliation(occupant.bare_jid);
end

local function send_event(event_name, room, occupant)
    local room_name = room and room.jid and room.jid:match("([^@]+)") or "unknown";
    local payload = {
        event_name      = event_name,
        room_name       = room_name,
        room_jid        = room and room.jid or "unknown",
        occupant_jid    = occupant and occupant.bare_jid or nil,
        occupant_nick   = occupant_display_nick(occupant),
        role            = occupant and occupant.role or nil,
        affiliation     = occupant_affiliation(room, occupant),
        host            = module_host,
    };
    local body = json.encode(payload);
    local headers = { ["Content-Type"] = "application/json" };
    if webhook_secret then
        headers["X-Civitas-Webhook-Secret"] = webhook_secret;
    end
    http.request(webhook_url, {
        method  = "POST",
        headers = headers,
        body    = body,
    }, function(response_body, code)
        if code ~= 200 then
            module:log("warn", "Webhook error %d for event %s (room=%s)", code or 0, event_name, room_name);
        end
    end);
end

module:hook("muc-room-created", function(event)
    send_event("muc-room-created", event.room, nil);
end);

module:hook("muc-room-destroyed", function(event)
    send_event("muc-room-destroyed", event.room, nil);
end);

module:hook("muc-occupant-joined", function(event)
    send_event("muc-occupant-joined", event.room, event.occupant);
end);

module:hook("muc-occupant-left", function(event)
    send_event("muc-occupant-left", event.room, event.occupant);
end);

module:log("info", "mod_muc_webhook chargé — webhook: %s (secret: %s)", webhook_url, webhook_secret and "configuré" or "ABSENT");
