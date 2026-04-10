FROM python:3.11-slim AS builder
RUN pip install --no-cache-dir uv==0.9.17
WORKDIR /app
COPY pyproject.toml uv.lock ./
RUN uv sync --frozen
COPY . /app

FROM python:3.11-slim
WORKDIR /app
COPY --from=builder /app/.venv /app/.venv
COPY . /app
CMD ["python", "-c", "import json; print(json.dumps(open('/app/config.json').read()))"]
