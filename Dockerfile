FROM python:3.11-slim
LABEL authors="pitrlabs"

WORKDIR /app

COPY . /app/

RUN apt-get update && apt-get install -y \
    git build-essential curl unzip libgl1 libglib2.0-0 && \
    rm -rf /var/lib/apt/lists/*

COPY --from=ghcr.io/astral-sh/uv:latest /uv /uvx /bin/

ENV PATH="/root/.local/bin:$PATH"

RUN uv sync

RUN uv pip install torch
