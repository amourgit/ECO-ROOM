Test git global

# CIVITAS — Documentation API complète & Guide de test CLI (curl)

> Toutes les requêtes curl pour tester chaque endpoint de la plateforme CIVITAS.  
> IP hôte : `192.168.1.89` · Tokens Bearer ci-dessous.

---

## Tokens d'authentification

| Service | Token |
|---------|-------|
| Room Config | `civitas-room-config-token` |
| Room Spawner | `civitas-peer-token` |
| Peer Service | `civitas-peer-token` |

---

## Sommaire

1. [Event Bridge (:8100)](#1-event-bridge-8100)
2. [Room Config Service (:8010)](#2-room-config-service-8010)
3. [Room Spawner (:8011)](#3-room-spawner-8011)
4. [Peer Service (:8002)](#4-peer-service-8002)
5. [Kafka UI (:8090)](#5-kafka-ui-8090)
6. [Grafana (:3000)](#6-grafana-3000)
7. [Prometheus (:9091)](#7-prometheus-9091)
8. [Loki (:3100)](#8-loki-3100)
9. [Tests de flux complets](#9-tests-de-flux-complets)

---

## 1. Event Bridge (:8100)

Base URL : `http://192.168.1.89:8100`

### GET /health

Vérifie l'état du service et du producteur Kafka.

```bash
curl -s http://192.168.1.89:8100/health | python3 -m json.tool
```

**Réponse JSON :**
```json
{
  "service": "jitsi-event-bridge",
  "version": "2.0.0",
  "status": "ok",
  "active_rooms": 2,
  "kafka": "civitas-kafka:9094"
}
```

---

### GET /rooms

Liste toutes les rooms actives connues de l'Event Bridge (état en mémoire).

```bash
curl -s http://192.168.1.89:8100/rooms | python3 -m json.tool
```

**Réponse JSON :**
```json
{
  "rooms": [
    {
      "room_id": "salle-42",
      "participant_count": 3,
      "participants": [
        {
          "jid": "user1@meet.civitas.local/resource1",
          "nick": "Jean Dupont",
          "role": "moderator",
          "affiliation": "owner",
          "joined_at": "2024-01-15T10:25:00"
        }
      ],
      "snapshot_at": "2024-01-15T10:30:00"
    }
  ],
  "total_rooms": 1,
  "total_participants": 3
}
```

---

### GET /rooms/{room_id}

État détaillé d'une room spécifique.

```bash
curl -s http://192.168.1.89:8100/rooms/salle-42 | python3 -m json.tool
```

**Réponse JSON (succès) :**
```json
{
  "room_id": "salle-42",
  "participant_count": 2,
  "participants": [
    {
      "jid": "user1@meet.civitas.local/abc123",
      "nick": "Marie Martin",
      "role": "participant",
      "affiliation": "none",
      "joined_at": "2024-01-15T10:20:00"
    }
  ],
  "snapshot_at": "2024-01-15T10:30:00"
}
```

**Réponse JSON (404 - room inconnue) :**
```json
{
  "detail": "Room inconnue"
}
```

---

### POST /webhook

Reçoit un événement Prosody et le publie sur Kafka. Normalement appelé par Prosody, mais peut être appelé manuellement pour tester.

**Créer une room :**
```bash
curl -s -X POST http://192.168.1.89:8100/webhook \
  -H "Content-Type: application/json" \
  -d '{
    "event_name": "muc-room-created",
    "room_name": "test-salle",
    "room": "test-salle"
  }' | python3 -m json.tool
```

**Participant rejoint :**
```bash
curl -s -X POST http://192.168.1.89:8100/webhook \
  -H "Content-Type: application/json" \
  -d '{
    "event_name": "muc-occupant-joined",
    "room_name": "test-salle",
    "occupant_jid": "jean@meet.civitas.local/abc",
    "occupant_nick": "Jean Dupont",
    "role": "participant",
    "affiliation": "none"
  }' | python3 -m json.tool
```

**Participant quitte :**
```bash
curl -s -X POST http://192.168.1.89:8100/webhook \
  -H "Content-Type: application/json" \
  -d '{
    "event_name": "muc-occupant-left",
    "room_name": "test-salle",
    "occupant_jid": "jean@meet.civitas.local/abc",
    "occupant_nick": "Jean Dupont"
  }' | python3 -m json.tool
```

**Détruire une room :**
```bash
curl -s -X POST http://192.168.1.89:8100/webhook \
  -H "Content-Type: application/json" \
  -d '{
    "event_name": "muc-room-destroyed",
    "room_name": "test-salle"
  }' | python3 -m json.tool
```

**Message chat :**
```bash
curl -s -X POST http://192.168.1.89:8100/webhook \
  -H "Content-Type: application/json" \
  -d '{
    "event_name": "muc-message",
    "room_name": "test-salle",
    "occupant_nick": "Jean Dupont",
    "body": "Bonjour tout le monde !"
  }' | python3 -m json.tool
```

**Changement de rôle :**
```bash
curl -s -X POST http://192.168.1.89:8100/webhook \
  -H "Content-Type: application/json" \
  -d '{
    "event_name": "occupant-role-changed",
    "room_name": "test-salle",
    "jid": "jean@meet.civitas.local/abc",
    "role": "moderator"
  }' | python3 -m json.tool
```

**Réponse JSON (webhook) :**
```json
{
  "status": "ok",
  "topic": "jitsi.room.events",
  "event": "muc-room-created"
}
```

**Types de données en entrée (webhook) :**

| Champ | Type | Obligatoire | Description |
|-------|------|-------------|-------------|
| `event_name` | string | oui | Nom de l'événement Prosody |
| `room_name` | string | conditonnel | Identifiant de la room (ou `room`) |
| `room` | string | conditionnel | Alias de `room_name` |
| `occupant_jid` | string | non | JID complet de l'occupant |
| `jid` | string | non | Alias de `occupant_jid` |
| `occupant_nick` | string | non | Nom affiché |
| `nick` | string | non | Alias de `occupant_nick` |
| `role` | string | non | `moderator`, `participant`, `visitor` |
| `affiliation` | string | non | `owner`, `admin`, `member`, `none` |
| `body` | string | non | Corps du message chat |

---

## 2. Room Config Service (:8010)

Base URL : `http://192.168.1.89:8010`  
Auth : `Authorization: Bearer civitas-room-config-token`

### GET /health

```bash
curl -s http://192.168.1.89:8010/health | python3 -m json.tool
```

**Réponse JSON :**
```json
{
  "service": "room-config",
  "status": "ok",
  "database": "ok",
  "version": "1.0.0"
}
```

---

### GET /rooms/

Liste toutes les configurations de rooms.

```bash
curl -s http://192.168.1.89:8010/rooms/ \
  -H "Authorization: Bearer civitas-room-config-token" \
  | python3 -m json.tool
```

**Paramètres de query :**

| Paramètre | Type | Défaut | Description |
|-----------|------|--------|-------------|
| `skip` | int | 0 | Offset de pagination |
| `limit` | int | 100 | Nombre max de résultats |

```bash
# Pagination
curl -s "http://192.168.1.89:8010/rooms/?skip=0&limit=10" \
  -H "Authorization: Bearer civitas-room-config-token" \
  | python3 -m json.tool
```

**Réponse JSON (tableau de RoomConfigResponse) :**
```json
[
  {
    "room_id": "salle-42",
    "agent_name": "CIVITAS",
    "system_prompt": "Tu es CIVITAS, un assistant IA...",
    "behavior_mode": "on_call",
    "language": "fr",
    "can_speak": true,
    "can_write_chat": true,
    "can_use_tools": false,
    "can_use_rag": false,
    "can_moderate": false,
    "invocation_keywords": ["civitas"],
    "tools_allowed": [],
    "extra_config": {},
    "is_active": true,
    "created_at": "2024-01-15T10:00:00",
    "updated_at": "2024-01-15T10:00:00"
  }
]
```

---

### GET /rooms/{room_id}

Récupère la config d'une room spécifique.

```bash
curl -s http://192.168.1.89:8010/rooms/salle-42 \
  -H "Authorization: Bearer civitas-room-config-token" \
  | python3 -m json.tool
```

**Réponse JSON (404) :**
```json
{
  "detail": "Room config introuvable"
}
```

---

### GET /rooms/{room_id}/context

**Endpoint principal utilisé par le Peer.** Retourne le contexte agent optimisé. Crée automatiquement une config par défaut si elle n'existe pas.

```bash
curl -s http://192.168.1.89:8010/rooms/salle-42/context \
  -H "Authorization: Bearer civitas-room-config-token" \
  | python3 -m json.tool
```

**Réponse JSON (AgentContextResponse) :**
```json
{
  "room_id": "salle-42",
  "agent_name": "CIVITAS",
  "system_prompt": "Tu es CIVITAS, un assistant IA dans une réunion en ligne...",
  "behavior_mode": "on_call",
  "language": "fr",
  "permissions": {
    "can_speak": true,
    "can_write_chat": true,
    "can_use_tools": false,
    "can_use_rag": false,
    "can_moderate": false
  },
  "invocation_keywords": ["civitas"],
  "tools_allowed": []
}
```

---

### POST /rooms/

Crée une nouvelle configuration de room.

```bash
curl -s -X POST http://192.168.1.89:8010/rooms/ \
  -H "Authorization: Bearer civitas-room-config-token" \
  -H "Content-Type: application/json" \
  -d '{
    "room_id": "ma-salle-custom",
    "agent_name": "ALEX",
    "system_prompt": "Tu es ALEX, assistant spécialisé en DevOps. Réponds uniquement si on cite ton nom.",
    "behavior_mode": "on_call",
    "language": "fr",
    "can_speak": true,
    "can_write_chat": true,
    "can_use_tools": true,
    "can_use_rag": false,
    "can_moderate": false,
    "invocation_keywords": ["alex", "assistant"],
    "tools_allowed": ["docker", "kubectl"],
    "extra_config": {},
    "is_active": true
  }' | python3 -m json.tool
```

**Corps de requête (RoomConfigCreate) :**

| Champ | Type | Obligatoire | Défaut | Description |
|-------|------|-------------|--------|-------------|
| `room_id` | string | oui | — | ID unique de la room |
| `agent_name` | string | non | `"CIVITAS"` | Nom affiché de l'agent |
| `system_prompt` | string | non | `""` | Prompt Gemini (généré si vide) |
| `behavior_mode` | string | non | `"on_call"` | `on_call` / `proactive` / `silent` |
| `language` | string | non | `"fr"` | Langue de réponse |
| `can_speak` | bool | non | `true` | Répond en audio |
| `can_write_chat` | bool | non | `true` | Écrit dans le chat |
| `can_use_tools` | bool | non | `false` | Accès outils |
| `can_use_rag` | bool | non | `false` | Accès base de connaissances |
| `can_moderate` | bool | non | `false` | Peut modérer |
| `invocation_keywords` | string[] | non | `["civitas"]` | Mots-clés déclencheurs |
| `tools_allowed` | string[] | non | `[]` | Outils autorisés |
| `extra_config` | object | non | `{}` | Config additionnelle libre |
| `is_active` | bool | non | `true` | Config active |

**Réponse (201 Created) :** `RoomConfigResponse` (même structure que GET /rooms/{room_id})

---

### PATCH /rooms/{room_id}

Met à jour partiellement une config de room.

```bash
# Changer le mode de comportement
curl -s -X PATCH http://192.168.1.89:8010/rooms/salle-42 \
  -H "Authorization: Bearer civitas-room-config-token" \
  -H "Content-Type: application/json" \
  -d '{"behavior_mode": "silent"}' \
  | python3 -m json.tool

# Activer la modération
curl -s -X PATCH http://192.168.1.89:8010/rooms/salle-42 \
  -H "Authorization: Bearer civitas-room-config-token" \
  -H "Content-Type: application/json" \
  -d '{"can_moderate": true}' \
  | python3 -m json.tool

# Changer les mots-clés d'invocation
curl -s -X PATCH http://192.168.1.89:8010/rooms/salle-42 \
  -H "Authorization: Bearer civitas-room-config-token" \
  -H "Content-Type: application/json" \
  -d '{"invocation_keywords": ["civitas", "alex", "assistant"]}' \
  | python3 -m json.tool

# Changer le prompt système
curl -s -X PATCH http://192.168.1.89:8010/rooms/salle-42 \
  -H "Authorization: Bearer civitas-room-config-token" \
  -H "Content-Type: application/json" \
  -d '{
    "system_prompt": "Tu es CIVITAS, modérateur de cette réunion gouvernementale. Assure-toi que tout le monde peut s'\''exprimer. Réponds uniquement si on mentionne ton nom."
  }' | python3 -m json.tool

# Désactiver le peer pour cette room
curl -s -X PATCH http://192.168.1.89:8010/rooms/salle-42 \
  -H "Authorization: Bearer civitas-room-config-token" \
  -H "Content-Type: application/json" \
  -d '{"extra_config": {"peer_enabled": false}}' \
  | python3 -m json.tool
```

**Corps de requête (RoomConfigUpdate — tous les champs sont optionnels) :**

Tous les champs de RoomConfigCreate sauf `room_id`, avec toutes les valeurs nullable.

**Réponse (200) :** `RoomConfigResponse` mise à jour  
**Réponse (404) :** `{"detail": "Room config introuvable"}`

---

### DELETE /rooms/{room_id}

Supprime une config de room.

```bash
curl -s -X DELETE http://192.168.1.89:8010/rooms/ma-salle-custom \
  -H "Authorization: Bearer civitas-room-config-token" \
  -w "\nHTTP Status: %{http_code}\n"
```

**Réponse :** HTTP 204 No Content (succès) ou 404.

---

## 3. Room Spawner (:8011)

Base URL : `http://192.168.1.89:8011`  
Auth : `Authorization: Bearer civitas-peer-token`

### GET /health

```bash
curl -s http://192.168.1.89:8011/health | python3 -m json.tool
```

**Réponse JSON :**
```json
{
  "service": "room-spawner",
  "status": "ok",
  "auto_join": true,
  "auto_leave": true,
  "active_rooms": 2,
  "version": "1.0.0"
}
```

---

### GET /rooms/active

Liste les rooms où un peer est actuellement actif.

```bash
curl -s http://192.168.1.89:8011/rooms/active \
  -H "Authorization: Bearer civitas-peer-token" \
  | python3 -m json.tool
```

**Réponse JSON :**
```json
{
  "active_rooms": ["salle-42", "reunion-tech"],
  "peer_instances": {
    "count": 2,
    "instances": [
      {
        "room_id": "salle-42",
        "active": true,
        "agent_name": "CIVITAS",
        "behavior_mode": "on_call",
        "started_at": "2024-01-15T10:00:00",
        "duration_minutes": 25
      }
    ]
  }
}
```

---

### POST /moderator/inject

Injecte manuellement le peer dans une room. Le peer rejoint et active la config.

```bash
curl -s -X POST http://192.168.1.89:8011/moderator/inject \
  -H "Authorization: Bearer civitas-peer-token" \
  -H "Content-Type: application/json" \
  -d '{"room_id": "salle-42"}' \
  | python3 -m json.tool
```

**Corps de requête :**
```json
{
  "room_id": "string (obligatoire)"
}
```

**Réponse JSON (succès) :**
```json
{
  "status": "injected",
  "room_id": "salle-42"
}
```

**Réponse JSON (déjà actif) :**
```json
{
  "status": "already_active",
  "room_id": "salle-42"
}
```

**Réponse JSON (erreur) :**
```json
{
  "status": "error",
  "room_id": "salle-42",
  "detail": "Peer join failed"
}
```

---

### POST /moderator/eject

Éjecte manuellement le peer d'une room. Désactive aussi la config (`peer_enabled: false`).

```bash
curl -s -X POST http://192.168.1.89:8011/moderator/eject \
  -H "Authorization: Bearer civitas-peer-token" \
  -H "Content-Type: application/json" \
  -d '{"room_id": "salle-42"}' \
  | python3 -m json.tool
```

**Réponse JSON :**
```json
{
  "status": "ejected",
  "room_id": "salle-42"
}
```

**Réponse JSON (pas actif) :**
```json
{
  "status": "not_active",
  "room_id": "salle-42"
}
```

---

### POST /moderator/standby

Met le peer en mode `silent`. Il reste dans la room mais n'intervient plus.

```bash
curl -s -X POST http://192.168.1.89:8011/moderator/standby \
  -H "Authorization: Bearer civitas-peer-token" \
  -H "Content-Type: application/json" \
  -d '{"room_id": "salle-42"}' \
  | python3 -m json.tool
```

**Réponse JSON :**
```json
{
  "status": "standby",
  "room_id": "salle-42"
}
```

---

### POST /moderator/activate

Réactive le peer depuis le mode `silent` vers `on_call`.

```bash
curl -s -X POST http://192.168.1.89:8011/moderator/activate \
  -H "Authorization: Bearer civitas-peer-token" \
  -H "Content-Type: application/json" \
  -d '{"room_id": "salle-42"}' \
  | python3 -m json.tool
```

**Réponse JSON :**
```json
{
  "status": "activated",
  "room_id": "salle-42"
}
```

---

## 4. Peer Service (:8002)

Base URL : `http://192.168.1.89:8002`  
Auth : `Authorization: Bearer civitas-peer-token`

### GET /health

```bash
curl -s http://192.168.1.89:8002/health | python3 -m json.tool
```

**Réponse JSON :**
```json
{
  "service": "civitas-peer",
  "version": "3.0.0",
  "status": "ok",
  "active_instances": 2,
  "jitsi_host": "meet.civitas.local"
}
```

---

### POST /peer/join

Crée une instance Peer dans une room Jitsi et démarre l'agent.

```bash
curl -s -X POST http://192.168.1.89:8002/peer/join \
  -H "Authorization: Bearer civitas-peer-token" \
  -H "Content-Type: application/json" \
  -d '{"room_id": "salle-42"}' \
  | python3 -m json.tool
```

**Corps de requête :**
```json
{
  "room_id": "string (obligatoire)"
}
```

**Réponse JSON (succès) :**
```json
{
  "status": "joined",
  "room_id": "salle-42",
  "active": true,
  "agent_name": "CIVITAS",
  "behavior_mode": "on_call"
}
```

> **Note :** Si l'instance existe déjà pour cette room, elle est retournée telle quelle.

---

### POST /peer/leave/{room_id}

Arrête et détruit l'instance Peer d'une room.

```bash
curl -s -X POST http://192.168.1.89:8002/peer/leave/salle-42 \
  -H "Authorization: Bearer civitas-peer-token" \
  | python3 -m json.tool
```

**Réponse JSON :**
```json
{
  "status": "left",
  "room_id": "salle-42"
}
```

---

### GET /peer/instances

Liste toutes les instances Peer actives.

```bash
curl -s http://192.168.1.89:8002/peer/instances \
  -H "Authorization: Bearer civitas-peer-token" \
  | python3 -m json.tool
```

**Réponse JSON :**
```json
{
  "count": 2,
  "instances": [
    {
      "room_id": "salle-42",
      "active": true,
      "agent_name": "CIVITAS",
      "behavior_mode": "on_call",
      "started_at": "2024-01-15T10:00:00",
      "duration_minutes": 25
    },
    {
      "room_id": "reunion-tech",
      "active": true,
      "agent_name": "ALEX",
      "behavior_mode": "proactive",
      "started_at": "2024-01-15T10:15:00",
      "duration_minutes": 10
    }
  ]
}
```

---

### POST /peer/{room_id}/send_text

Envoie un texte directement à la session Gemini de la room (injection de prompt).

```bash
curl -s -X POST http://192.168.1.89:8002/peer/salle-42/send_text \
  -H "Authorization: Bearer civitas-peer-token" \
  -H "Content-Type: application/json" \
  -d '{"text": "Résume les 5 dernières minutes de la réunion."}' \
  | python3 -m json.tool
```

**Corps de requête :**
```json
{
  "text": "string (obligatoire)"
}
```

**Réponse JSON :**
```json
{
  "status": "sent"
}
```

**Réponse JSON (404 - room sans peer) :**
```json
{
  "detail": "Instance introuvable"
}
```

---

### POST /peer/{room_id}/send_chat

Envoie un message de chat dans la room Jitsi (depuis l'agent CIVITAS).

```bash
curl -s -X POST http://192.168.1.89:8002/peer/salle-42/send_chat \
  -H "Authorization: Bearer civitas-peer-token" \
  -H "Content-Type: application/json" \
  -d '{"text": "👋 Bonjour, je suis de retour !"}' \
  | python3 -m json.tool
```

**Corps de requête :**
```json
{
  "text": "string (obligatoire)"
}
```

**Réponse JSON :**
```json
{
  "status": "sent"
}
```

---

## 5. Kafka UI (:8090)

Interface web uniquement (pas d'API REST propre).

```bash
# Tester l'accessibilité
curl -s -o /dev/null -w "%{http_code}" http://192.168.1.89:8090/
# Doit retourner 302 (redirection vers login)

# Connexion : login civitas / password civitas2024
# URL : http://192.168.1.89:8090
```

---

## 6. Grafana (:3000)

```bash
# Health check
curl -s http://192.168.1.89:3000/api/health | python3 -m json.tool

# Connexion : civitas / civitas2024
# URL : http://192.168.1.89:3000

# Lister les datasources (avec auth basic)
curl -s http://civitas:civitas2024@192.168.1.89:3000/api/datasources | python3 -m json.tool

# Lister les dashboards
curl -s http://civitas:civitas2024@192.168.1.89:3000/api/search | python3 -m json.tool
```

---

## 7. Prometheus (:9091)

```bash
# Health
curl -s http://192.168.1.89:9091/-/healthy

# Ready
curl -s http://192.168.1.89:9091/-/ready

# Métriques brutes
curl -s http://192.168.1.89:9091/metrics | head -50

# API Query — obtenir une métrique
curl -s "http://192.168.1.89:9091/api/v1/query?query=up" | python3 -m json.tool

# Lister les targets scrape
curl -s "http://192.168.1.89:9091/api/v1/targets" | python3 -m json.tool

# Exemple requête : CPU usage
curl -s "http://192.168.1.89:9091/api/v1/query?query=100-(avg+by+(instance)(rate(node_cpu_seconds_total{mode='idle'}[5m]))*100)" | python3 -m json.tool
```

---

## 8. Loki (:3100)

```bash
# Health
curl -s http://192.168.1.89:3100/ready

# Lister les labels disponibles
curl -s "http://192.168.1.89:3100/loki/api/v1/labels" | python3 -m json.tool

# Valeurs d'un label
curl -s "http://192.168.1.89:3100/loki/api/v1/label/job/values" | python3 -m json.tool

# Requête de logs Jitsi (dernières 1h)
curl -s -G "http://192.168.1.89:3100/loki/api/v1/query_range" \
  --data-urlencode 'query={job="jitsi"}' \
  --data-urlencode "start=$(date -d '1 hour ago' +%s)000000000" \
  --data-urlencode "end=$(date +%s)000000000" \
  --data-urlencode "limit=50" \
  | python3 -m json.tool

# Requête de logs Nginx
curl -s -G "http://192.168.1.89:3100/loki/api/v1/query_range" \
  --data-urlencode 'query={job="nginx"}' \
  --data-urlencode "start=$(date -d '30 minutes ago' +%s)000000000" \
  --data-urlencode "end=$(date +%s)000000000" \
  --data-urlencode "limit=20" \
  | python3 -m json.tool
```

---

## 9. Tests de flux complets

### Test 1 — Vérification de l'état de toute la plateforme

```bash
#!/bin/bash
echo "=== Health Check CIVITAS ==="
echo ""
echo "[1] Event Bridge"
curl -s http://192.168.1.89:8100/health | python3 -m json.tool
echo ""
echo "[2] Room Config"
curl -s http://192.168.1.89:8010/health | python3 -m json.tool
echo ""
echo "[3] Room Spawner"
curl -s http://192.168.1.89:8011/health | python3 -m json.tool
echo ""
echo "[4] Peer Service"
curl -s http://192.168.1.89:8002/health | python3 -m json.tool
echo ""
echo "[5] Prometheus"
curl -s http://192.168.1.89:9091/-/healthy
echo ""
```

---

### Test 2 — Créer une room custom et vérifier la config

```bash
#!/bin/bash

# 1. Créer la config
echo "=== Création config room ==="
curl -s -X POST http://192.168.1.89:8010/rooms/ \
  -H "Authorization: Bearer civitas-room-config-token" \
  -H "Content-Type: application/json" \
  -d '{
    "room_id": "gouvernement-2024",
    "agent_name": "CIVITAS-GOV",
    "system_prompt": "Tu es CIVITAS-GOV, assistant de la réunion gouvernementale. Tu réponds uniquement si on cite ton nom. Tu es neutre, professionnel et précis.",
    "behavior_mode": "on_call",
    "language": "fr",
    "can_speak": true,
    "can_write_chat": true,
    "invocation_keywords": ["civitas", "civitas-gov", "assistant"]
  }' | python3 -m json.tool

echo ""
echo "=== Vérification du contexte agent ==="
curl -s http://192.168.1.89:8010/rooms/gouvernement-2024/context \
  -H "Authorization: Bearer civitas-room-config-token" \
  | python3 -m json.tool
```

---

### Test 3 — Simulation du cycle complet (sans Jitsi réel)

```bash
#!/bin/bash

ROOM="test-cli-$(date +%s)"

echo "=== Test cycle complet — room: $ROOM ==="

# Étape 1 : Simuler création room via Prosody
echo "[1] Simulation webhook muc-room-created"
curl -s -X POST http://192.168.1.89:8100/webhook \
  -H "Content-Type: application/json" \
  -d "{\"event_name\": \"muc-room-created\", \"room_name\": \"$ROOM\"}" \
  | python3 -m json.tool

sleep 2

# Étape 2 : Vérifier l'état Event Bridge
echo ""
echo "[2] État rooms Event Bridge"
curl -s http://192.168.1.89:8100/rooms | python3 -m json.tool

# Étape 3 : Simuler un participant
echo ""
echo "[3] Simulation participant join"
curl -s -X POST http://192.168.1.89:8100/webhook \
  -H "Content-Type: application/json" \
  -d "{
    \"event_name\": \"muc-occupant-joined\",
    \"room_name\": \"$ROOM\",
    \"occupant_jid\": \"ministre@meet.civitas.local/abc\",
    \"occupant_nick\": \"Ministre de la Santé\",
    \"role\": \"moderator\",
    \"affiliation\": \"owner\"
  }" | python3 -m json.tool

sleep 1

# Étape 4 : Vérifier présence dans la room
echo ""
echo "[4] État room spécifique"
curl -s "http://192.168.1.89:8100/rooms/$ROOM" | python3 -m json.tool

# Étape 5 : Vérifier Room Spawner
echo ""
echo "[5] Rooms actives (Spawner)"
curl -s http://192.168.1.89:8011/rooms/active \
  -H "Authorization: Bearer civitas-peer-token" \
  | python3 -m json.tool

# Étape 6 : Vérifier Peer instances
echo ""
echo "[6] Instances Peer actives"
curl -s http://192.168.1.89:8002/peer/instances \
  -H "Authorization: Bearer civitas-peer-token" \
  | python3 -m json.tool

# Étape 7 : Nettoyage
echo ""
echo "[7] Simulation room détruite"
curl -s -X POST http://192.168.1.89:8100/webhook \
  -H "Content-Type: application/json" \
  -d "{\"event_name\": \"muc-room-destroyed\", \"room_name\": \"$ROOM\"}" \
  | python3 -m json.tool
```

---

### Test 4 — Contrôle modérateur complet

```bash
#!/bin/bash

ROOM="salle-ministere"

echo "=== Contrôle modérateur ==="

# Injecter l'agent manuellement
echo "[1] Injection manuelle du peer"
curl -s -X POST http://192.168.1.89:8011/moderator/inject \
  -H "Authorization: Bearer civitas-peer-token" \
  -H "Content-Type: application/json" \
  -d "{\"room_id\": \"$ROOM\"}" \
  | python3 -m json.tool

sleep 3

# Mettre en veille
echo ""
echo "[2] Mise en veille (silent)"
curl -s -X POST http://192.168.1.89:8011/moderator/standby \
  -H "Authorization: Bearer civitas-peer-token" \
  -H "Content-Type: application/json" \
  -d "{\"room_id\": \"$ROOM\"}" \
  | python3 -m json.tool

sleep 2

# Vérifier la config (doit être silent)
echo ""
echo "[3] Vérifier mode (doit être silent)"
curl -s "http://192.168.1.89:8010/rooms/$ROOM" \
  -H "Authorization: Bearer civitas-room-config-token" \
  | python3 -c "import sys,json; d=json.load(sys.stdin); print('behavior_mode:', d['behavior_mode'])"

# Réactiver
echo ""
echo "[4] Réactivation"
curl -s -X POST http://192.168.1.89:8011/moderator/activate \
  -H "Authorization: Bearer civitas-peer-token" \
  -H "Content-Type: application/json" \
  -d "{\"room_id\": \"$ROOM\"}" \
  | python3 -m json.tool

sleep 1

# Envoyer un message texte à l'agent
echo ""
echo "[5] Injection de prompt dans Gemini"
curl -s -X POST "http://192.168.1.89:8002/peer/$ROOM/send_text" \
  -H "Authorization: Bearer civitas-peer-token" \
  -H "Content-Type: application/json" \
  -d '{"text": "Annonce aux participants que la réunion va commencer dans 5 minutes."}' \
  | python3 -m json.tool

sleep 2

# Envoyer un message chat direct
echo ""
echo "[6] Message chat direct"
curl -s -X POST "http://192.168.1.89:8002/peer/$ROOM/send_chat" \
  -H "Authorization: Bearer civitas-peer-token" \
  -H "Content-Type: application/json" \
  -d '{"text": "📢 La réunion débutera dans 5 minutes. Merci de vous préparer."}' \
  | python3 -m json.tool

# Éjecter
echo ""
echo "[7] Éjection finale"
curl -s -X POST http://192.168.1.89:8011/moderator/eject \
  -H "Authorization: Bearer civitas-peer-token" \
  -H "Content-Type: application/json" \
  -d "{\"room_id\": \"$ROOM\"}" \
  | python3 -m json.tool
```

---

### Test 5 — Configuration avancée agent modérateur

```bash
#!/bin/bash

# Créer une config avec tous les droits de modération
curl -s -X POST http://192.168.1.89:8010/rooms/ \
  -H "Authorization: Bearer civitas-room-config-token" \
  -H "Content-Type: application/json" \
  -d '{
    "room_id": "salle-pleniere",
    "agent_name": "MODÉRATEUR-CIVITAS",
    "system_prompt": "Tu es MODÉRATEUR-CIVITAS, modérateur IA de cette séance plénière. Tu surveilles activement les débats. Si quelqu'\''un est irrespectueux, tu interviens immédiatement. Tu signales toutes les mains levées. Tu fais des résumés toutes les 15 minutes si on te le demande. Tu réponds en français, de façon formelle et neutre.",
    "behavior_mode": "proactive",
    "language": "fr",
    "can_speak": true,
    "can_write_chat": true,
    "can_use_tools": false,
    "can_use_rag": false,
    "can_moderate": true,
    "invocation_keywords": ["modérateur", "civitas", "modérateur-civitas"],
    "extra_config": {
      "auto_summary_interval_minutes": 15,
      "respect_policy": "strict"
    }
  }' | python3 -m json.tool
```

---

### Test 6 — Vérification Kafka (topics et messages)

> Nécessite les outils kafka-console installés, ou l'accès au container kafka.

> ⚠️ Ne jamais utiliser `--bootstrap-server localhost:9092` (listener `PLAINTEXT`)
> dans ces commandes : ce listener est annoncé sur `192.168.1.89:9092`
> (`KAFKA_ADVERTISED_LISTENERS`), donc le client se reconnecte sur cette IP
> après le premier contact — souvent injoignable en boucle depuis le
> conteneur, d'où des commandes qui restent bloquées puis expirent.
> Utiliser systématiquement le listener `INTERNAL` (`civitas-kafka:9094`).

```bash
# Via docker exec
docker exec civitas-kafka kafka-topics --bootstrap-server civitas-kafka:9094 --list

# Consommer les messages du topic room.transcriptions
docker exec civitas-kafka kafka-console-consumer \
  --bootstrap-server civitas-kafka:9094 \
  --topic room.transcriptions \
  --from-beginning \
  --max-messages 10

# Consommer les événements room Jitsi
docker exec civitas-kafka kafka-console-consumer \
  --bootstrap-server civitas-kafka:9094 \
  --topic jitsi.room.events \
  --from-beginning \
  --max-messages 5

# Consommer les événements participants
docker exec civitas-kafka kafka-console-consumer \
  --bootstrap-server civitas-kafka:9094 \
  --topic jitsi.participant.events \
  --from-beginning \
  --max-messages 10

# Lister les topics avec leurs offsets
docker exec civitas-kafka kafka-run-class kafka.tools.GetOffsetShell \
  --broker-list civitas-kafka:9094 \
  --topic room.transcriptions
```

---

## Résumé des codes de retour

| Code | Signification |
|------|---------------|
| 200 | Succès |
| 201 | Ressource créée |
| 204 | Succès sans contenu (DELETE) |
| 400 | Requête invalide (JSON malformé, etc.) |
| 401 | Token Bearer manquant ou invalide |
| 404 | Ressource introuvable |
| 422 | Validation échouée (type de données incorrect) |
| 500 | Erreur serveur interne |

---

## Variables d'environnement — résumé

Pour tester en CLI, vous pouvez définir ces variables :

```bash
export API_BASE_RC="http://192.168.1.89:8010"
export API_BASE_RS="http://192.168.1.89:8011"
export API_BASE_PEER="http://192.168.1.89:8002"
export API_BASE_EB="http://192.168.1.89:8100"
export TOKEN_RC="civitas-room-config-token"
export TOKEN_PEER="civitas-peer-token"

# Puis utiliser:
curl -s $API_BASE_RC/health | python3 -m json.tool
curl -s -H "Authorization: Bearer $TOKEN_RC" $API_BASE_RC/rooms/ | python3 -m json.tool
```

