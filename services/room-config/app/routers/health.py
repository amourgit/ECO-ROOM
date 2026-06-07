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
        "status": "ok",
        "database": db_status,
        "version": "1.0.0",
    }
