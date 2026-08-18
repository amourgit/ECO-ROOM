"""
conftest.py — positionne les variables d'environnement obligatoires (ROOM_ID, GEMINI_API_KEY,
cf. app/config.py) AVANT tout import de `app.*`, pour que la suite de tests puisse s'exécuter
sans dépendre d'un vrai déploiement (Jitsi, Gemini, Kafka, Postgres, Docker — aucun de ces
systèmes n'est disponible dans l'environnement où ces tests sont écrits et exécutés, cf.
docs/architecture/04-plan-migration.md Phase 0 "Ce qui n'est PAS fait en Phase 0").

Ces tests couvrent la LOGIQUE PURE du CIVITAS Agent (état, registre d'outils, graphe LangGraph
assemblé et exécuté avec des dépendances simulées) — pas d'intégration avec un vrai navigateur
headless, une vraie session Gemini Live, un vrai broker Kafka ou un vrai Postgres. C'est
volontaire et documenté : ces intégrations réelles restent le critère de bascule vers la Phase
2 du plan de migration (doc 04), qui nécessite un environnement de déploiement réel.
"""
import os

os.environ.setdefault("ROOM_ID", "test-room")
os.environ.setdefault("GEMINI_API_KEY", "dummy-key-for-unit-tests")
