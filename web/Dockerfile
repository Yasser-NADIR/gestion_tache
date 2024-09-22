FROM python:3.9-slim

RUN apt-get update && apt-get install -y \
    build-essential \
    libmariadb-dev \
    libmariadb-dev-compat \
    gcc \
    && apt-get clean \
    && rm -rf /var/lib/apt/lists/*

WORKDIR /app

COPY requirements.txt requirements.txt

RUN pip install --no-cache-dir -r requirements.txt

COPY dev/. .

# ENV FLASK_APP=/app/run.py

ENTRYPOINT [ "python", "run.py" ]