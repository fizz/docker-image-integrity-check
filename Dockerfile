FROM python:3.11-slim AS builder
WORKDIR /app
COPY . /app
RUN python -c "import json; json.loads(open('/app/config.json').read())"

FROM python:3.11-slim
WORKDIR /app
COPY --from=builder /app /app
COPY . /app
CMD ["python", "-c", "import json; print(json.dumps(open('/app/config.json').read()))"]
