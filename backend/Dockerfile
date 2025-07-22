# backend/Dockerfile
FROM python:3.11-slim

# Evita .pyc e buffer no stdout
ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1

# Dependências do sistema
RUN apt-get update && apt-get install -y build-essential \
    && rm -rf /var/lib/apt/lists/*

# Instala Poetry
RUN pip install --upgrade pip \
    && pip install poetry

WORKDIR /app

# Copia definições de dependências e instala
COPY pyproject.toml poetry.lock* README.md /app/
RUN poetry config virtualenvs.create false \
    && poetry install --no-root --no-interaction --no-ansi

# Copia código
COPY . /app

# Porta que o Django irá usar
EXPOSE 8000

# Comando padrão (modo dev)
CMD ["poetry", "run", "python", "manage.py", "runserver", "0.0.0.0:8000"]
