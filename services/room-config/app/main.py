import logging
import uvicorn
from contextlib import asynccontextmanager
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from app.database import init_db, run_migrations
from app.routers import rooms, health
from app.kafka import consumer as history_consumer
from app.config import get_settings

logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s %(levelname)-8s %(name)s — %(message)s",
)
log = logging.getLogger(__name__)
settings = get_settings()


@asynccontextmanager
async def lifespan(app: FastAPI):
    log.info("[RoomConfig] Démarrage — initialisation base de données...")
    init_db()
    log.info("[RoomConfig] Tables prêtes ✓ — application des migrations...")
    run_migrations()
    log.info("[RoomConfig] Migrations à jour ✓")
    await history_consumer.start()
    yield
    log.info("[RoomConfig] Arrêt")
    await history_consumer.stop()


app = FastAPI(
    title="CIVITAS Room Config Service",
    description="Gestion de la configuration des agents par room",
    version="1.0.0",
    lifespan=lifespan,
)

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(health.router)
app.include_router(rooms.router)


if __name__ == "__main__":
    uvicorn.run(
        "app.main:app",
        host=settings.SERVICE_HOST,
        port=settings.SERVICE_PORT,
        reload=False,
    )
