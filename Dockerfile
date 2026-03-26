FROM python:3.11-slim
WORKDIR /app
COPY . /app
CMD ["python", "-c", "import json; print(json.dumps(open('/app/config.json').read()))"]
