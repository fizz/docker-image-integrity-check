FROM python:3.11-slim AS builder
RUN pip install --no-cache-dir uv==0.9.17
WORKDIR /build
COPY pyproject.toml uv.lock ./
RUN uv sync --frozen
WORKDIR /app
COPY . /app

FROM python:3.11-slim
COPY --from=builder /build/.venv /opt/venv
WORKDIR /app
COPY . /app
CMD ["python", "-c", "import json; print(json.dumps(open('/app/config.json').read()))"]
