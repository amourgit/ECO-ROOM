# Repris de services/peer/Dockerfile (base Playwright inchangée — Chromium headless).
# Une image, instanciée en N containers (un par room) par civitas-orchestrator — cf.
# docs/architecture/03-isolation-et-orchestration.md §4.3.

FROM mcr.microsoft.com/playwright/python:v1.45.0-jammy

WORKDIR /app

COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

COPY app ./app

# Label utilisé par civitas-orchestrator pour reconstruire son registre au redémarrage
# (cf. docs/architecture/03-isolation-et-orchestration.md §4.5). civitas.room_id est posé
# dynamiquement au `docker run`, pas ici (valeur inconnue au build).
LABEL civitas.agent="true"

EXPOSE 8300

CMD ["python", "-m", "app.main"]
