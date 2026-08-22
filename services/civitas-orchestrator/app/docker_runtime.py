"""
AgentRuntimeProvider — doc 03 §4.3. Interface + implémentation Docker par défaut.
L'interface (Protocol) existe pour qu'un provider Kubernetes puisse la remplacer plus tard
(doc 03 §3.3) sans toucher au reste de l'Orchestrateur.
"""
from __future__ import annotations

import hashlib
import logging
import re
from typing import Protocol

import docker
from docker.errors import NotFound

from app.config import get_settings
from app.registry import AgentHandle, make_handle

log = logging.getLogger(__name__)
settings = get_settings()

AGENT_LABEL = "civitas.agent"
ROOM_LABEL = "civitas.room_id"


def slugify_room_id(room_id: str) -> str:
    """Nom de container Docker valide et déterministe à partir d'un room_id arbitraire —
    cf. doc 03 §3.1 ('slug(room_id), tronqué + suffixe de hash court en cas de collision')."""
    base = re.sub(r"[^a-z0-9-]", "-", room_id.lower()).strip("-")[:40]
    suffix = hashlib.sha1(room_id.encode()).hexdigest()[:6]
    return f"civitas-agent-{base}-{suffix}"


class AgentRuntimeProvider(Protocol):
    async def spawn(self, room_id: str, env: dict[str, str]) -> AgentHandle: ...
    async def teardown(self, handle: AgentHandle) -> None: ...
    async def is_healthy(self, handle: AgentHandle) -> bool: ...
    async def list_running(self) -> list[AgentHandle]: ...


class DockerAgentRuntimeProvider:
    """Implémentation par défaut — cf. doc 03 §3.1. Toutes les méthodes sont synchrones côté
    SDK docker (bloquant) — acceptable ici car l'Orchestrateur ne fait qu'orchestrer, pas de
    chemin de latence critique comme dans un CIVITAS Agent."""

    def __init__(self):
        # Connexion PARESSEUSE, différée au premier usage réel (cf. propriété `_client`
        # ci-dessous) — PAS `docker.from_env()` ici. Une première version connectait
        # immédiatement dans __init__, ce qui empêchait `app.main` d'être ne serait-ce
        # qu'IMPORTÉ (donc testé) sans démon Docker déjà actif, et aurait fait planter
        # l'Orchestrateur au démarrage — avant même de pouvoir servir `/health` — sur une
        # indisponibilité Docker transitoire. La connexion réelle n'est tentée qu'au premier
        # spawn/teardown/is_healthy/list_running effectif.
        self.__client = None

    @property
    def _client(self):
        if self.__client is None:
            self.__client = docker.from_env()
        return self.__client

    async def spawn(self, room_id: str, env: dict[str, str]) -> AgentHandle:
        container_name = slugify_room_id(room_id)
        try:
            existing = self._client.containers.get(container_name)
            existing.remove(force=True)
            log.warning(f"[DockerRuntime] Container résiduel supprimé: {container_name}")
        except NotFound:
            pass

        container = self._client.containers.run(
            settings.AGENT_IMAGE,
            name=container_name,
            detach=True,
            network=settings.AGENT_NETWORK,
            environment={"ROOM_ID": room_id, **env},
            shm_size=settings.AGENT_SHM_SIZE,
            mem_limit=settings.AGENT_MEM_LIMIT,
            labels={AGENT_LABEL: "true", ROOM_LABEL: room_id},
            remove=True,  # --rm — cf. doc 03 §3.1
        )
        log.info(f"[DockerRuntime] Spawn {container_name} (id={container.short_id}) pour room={room_id}")

        return make_handle(
            room_id=room_id, container_name=container_name,
            base_url=f"http://{container_name}:{settings.AGENT_INTERNAL_PORT}",
        )

    async def teardown(self, handle: AgentHandle) -> None:
        try:
            container = self._client.containers.get(handle["container_name"])
            container.stop(timeout=15)
            log.info(f"[DockerRuntime] Arrêté {handle['container_name']}")
        except NotFound:
            log.info(f"[DockerRuntime] Déjà absent: {handle['container_name']}")
        except Exception as e:
            log.warning(f"[DockerRuntime] teardown {handle['container_name']}: {e}")

    async def is_healthy(self, handle: AgentHandle) -> bool:
        try:
            container = self._client.containers.get(handle["container_name"])
            return container.status == "running"
        except NotFound:
            return False

    async def list_running(self) -> list[AgentHandle]:
        """Reconstruction du registre au démarrage — doc 03 §4.5."""
        containers = self._client.containers.list(filters={"label": f"{AGENT_LABEL}=true", "status": "running"})
        handles = []
        for c in containers:
            room_id = c.labels.get(ROOM_LABEL)
            if not room_id:
                continue
            handles.append(make_handle(
                room_id=room_id, container_name=c.name,
                base_url=f"http://{c.name}:{settings.AGENT_INTERNAL_PORT}",
            ))
        log.info(f"[DockerRuntime] {len(handles)} agent(s) actif(s) retrouvé(s) au démarrage")
        return handles
