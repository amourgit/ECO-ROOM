-- mod_muc_webhook.lua
-- Envoie les événements MUC vers un webhook HTTP

local http = require "net.http";
local json = require "util.json";
local module_host = module.host;

local webhook_url = module:get_option_string("muc_webhook_url", "http://127.0.0.1:8100/webhook");

local function send_event(event_name, room, occupant)
    local room_name = room and room.jid and room.jid:match("([^@]+)") or "unknown";
    local payload = {
        event_name = event_name,
        room_name  = room_name,
        room_jid   = room and room.jid or "unknown",
        occupant   = occupant and occupant.nick or nil,
        host       = module_host,
    };
    local body = json.encode(payload);
    http.request(webhook_url, {
        method  = "POST",
        headers = { ["Content-Type"] = "application/json" },
        body    = body,
    }, function(response_body, code)
        if code ~= 200 then
            module:log("warn", "Webhook error %d for event %s", code, event_name);
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

module:log("info", "mod_muc_webhook chargé — webhook: %s", webhook_url);
