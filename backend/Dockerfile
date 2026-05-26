# syntax=docker/dockerfile:1.7
# ---------- Builder ----------
FROM python:3.12-slim AS builder

ENV PYTHONDONTWRITEBYTECODE=1 \
    PYTHONUNBUFFERED=1 \
    UV_LINK_MODE=copy \
    UV_COMPILE_BYTECODE=1 \
    UV_PROJECT_ENVIRONMENT=/app/.venv

# uv from the official image
COPY --from=ghcr.io/astral-sh/uv:latest /uv /uvx /usr/local/bin/

WORKDIR /app

# Install deps first (cached) — only the lockfiles in this layer
COPY backend/pyproject.toml backend/uv.lock /app/
RUN --mount=type=cache,target=/root/.cache/uv \
    uv sync --frozen --no-dev --no-install-project

# ---------- Runtime ----------
FROM python:3.12-slim AS runtime

ENV PYTHONDONTWRITEBYTECODE=1 \
    PYTHONUNBUFFERED=1 \
    PATH="/app/.venv/bin:$PATH" \
    LLM_WIKI_ROOT=/app \
    PORT=8080

# curl for HEALTHCHECK; tini for clean signal handling
RUN apt-get update \
 && apt-get install -y --no-install-recommends curl tini \
 && rm -rf /var/lib/apt/lists/*

# Non-root user
RUN groupadd --system app && useradd --system --gid app --home /app app

WORKDIR /app

# Copy installed venv from builder
COPY --from=builder /app/.venv /app/.venv

# App code + wiki data
COPY backend/app.py        /app/app.py
COPY llm-wiki/retrieval    /app/retrieval
COPY llm-wiki/Wiki         /app/Wiki
COPY llm-wiki/Raw          /app/Raw
COPY llm-wiki/Schema       /app/Schema
COPY llm-wiki/AGENTS.md    /app/AGENTS.md

RUN chown -R app:app /app
USER app

EXPOSE 8080

HEALTHCHECK --interval=30s --timeout=5s --start-period=15s --retries=3 \
    CMD curl -fsS "http://127.0.0.1:${PORT}/health" || exit 1

ENTRYPOINT ["/usr/bin/tini", "--"]
CMD ["sh", "-c", "uvicorn app:app --host 0.0.0.0 --port ${PORT}"]