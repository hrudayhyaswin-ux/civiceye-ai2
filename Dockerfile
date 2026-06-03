# ── Stage 1: Build React frontend ─────────────────────────────────────────────
FROM node:20-alpine AS frontend-build

WORKDIR /app/frontend

COPY frontend/package*.json ./
RUN npm ci

COPY frontend/ ./
RUN npm run build

# ── Stage 2: Python backend ────────────────────────────────────────────────────
FROM python:3.11-slim AS backend

RUN apt-get update && apt-get install -y --no-install-recommends \
    gcc \
    libpq-dev \
 && rm -rf /var/lib/apt/lists/*

WORKDIR /app

COPY backend/requirements.txt ./
RUN pip install --no-cache-dir -r requirements.txt

COPY backend/ ./

# Copy built frontend into backend's static directory
COPY --from=frontend-build /app/frontend/dist ./static

# Non-root user for security
RUN addgroup --system civiceye && adduser --system --ingroup civiceye civiceye
USER civiceye

EXPOSE 8000

HEALTHCHECK --interval=30s --timeout=10s --start-period=5s --retries=3 \
  CMD python -c "import urllib.request; urllib.request.urlopen('http://localhost:8000/health')"

# Adjust to your framework:
CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8000"]
# Django: CMD ["gunicorn", "civiceye.wsgi:application", "--bind", "0.0.0.0:8000"]
