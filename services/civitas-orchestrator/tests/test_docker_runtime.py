"""
Tests app/docker_runtime.py::slugify_room_id — doc 03 §3.1 ("slug(room_id), tronqué + suffixe
de hash court en cas de collision"). Ne teste QUE cette fonction pure : instancier
DockerAgentRuntimeProvider nécessiterait un vrai daemon Docker, indisponible dans cet
environnement (cf. docs/architecture/04-plan-migration.md — critère de bascule Phase 2).
"""
import re

from app.docker_runtime import slugify_room_id

VALID_CONTAINER_NAME = re.compile(r"^[a-z0-9-]+$")


def test_slug_is_deterministic():
    assert slugify_room_id("Salle de Réunion 42") == slugify_room_id("Salle de Réunion 42")


def test_slug_only_uses_valid_docker_charset():
    slug = slugify_room_id("Salle Été #42 !! Réunion Généra le")
    assert VALID_CONTAINER_NAME.match(slug), f"charset invalide: {slug}"


def test_slug_starts_with_expected_prefix():
    assert slugify_room_id("room-1").startswith("civitas-agent-")


def test_different_room_ids_that_truncate_to_same_prefix_still_differ():
    """Deux room_id très longs et quasi identiques au-delà de la troncature à 40 caractères
    doivent rester distincts grâce au suffixe de hash — sans quoi deux rooms différentes
    pourraient spawn le même nom de container, ce qui romprait l'isolation (doc 03 §2)."""
    long_a = "a" * 60 + "-room-A"
    long_b = "a" * 60 + "-room-B"
    slug_a = slugify_room_id(long_a)
    slug_b = slugify_room_id(long_b)
    assert slug_a != slug_b


def test_slug_length_is_bounded():
    slug = slugify_room_id("x" * 500)
    assert len(slug) < 80  # marge large sous la limite Docker (63 caractères recommandés)
