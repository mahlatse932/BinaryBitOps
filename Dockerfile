FROM python:3.12.15-alpine3.24

ENV PYTHONDONTWRITEBYTECODE=1 \
    PYTHONUNBUFFERED=1

WORKDIR /app

COPY --chown=10001:10001 binarybitops.py /app/binarybitops.py

USER 10001:10001

CMD ["python", "binarybitops.py"]
