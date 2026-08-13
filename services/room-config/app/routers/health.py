from fastapi import APIRouter
from app.database import engine

router = APIRouter(tags=["health"])


@router.get("/health")
async def health():
    try:
        with engine.connect() as conn:
            conn.execute(__import__("sqlalchemy").text("SELECT 1"))
        db_status = "ok"
    except Exception as e:
        db_status = f"error: {e}"

    return {
        "service": "room-config",
        # AVANT : toujours "ok" même si la DB était en erreur (db_status
        # n'était jamais répercuté ici) — un monitoring qui ne regarde que
        # ce champ racine ne détectait jamais une panne DB.
        "status": "ok" if db_status == "ok" else "degraded",
        "database": db_status,
        "version": "1.0.0",
    }
