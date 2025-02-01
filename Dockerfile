# Image de base
FROM python:3.13.1-slim

# Répertoire de travail
WORKDIR /app

# Variables d'environnement
ENV PYTHONUNBUFFERED=1
ENV PYTHONDONTWRITEBYTECODE=1
ENV DISCOGS_API_TOKEN=""
ENV GOOGLE_APPLICATION_CREDENTIALS="/app/gcp_key.json"


# Installation des dépendances système nécessaires
RUN apt-get update && \
    apt-get install -y --no-install-recommends \
    build-essential \
    curl \
    && rm -rf /var/lib/apt/lists/*

# Copie des fichiers de dépendances
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Copie de l'application
COPY app.py .
COPY pages/ ./pages/
COPY api/ ./api/
COPY gcp_key.json .

# Exposer le port 8080 (valeur utilisée par défaut)
EXPOSE 8080

# Lancer Streamlit
CMD ["streamlit", "run", "app.py", "--server.port=8080", "--server.address=0.0.0.0"]