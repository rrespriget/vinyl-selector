# Utiliser une image Python légère comme base
FROM python:3.13-slim

# Définir le répertoire de travail
WORKDIR /vinyl-selector

# Credentials Google
ENV GOOGLE_APPLICATION_CREDENTIALS="gcp_key.json"

# Ajout de la variable d'environnement
ENV DISCOGS_API_TOKEN="yRlbZhZoVdAMNBxuKLiEhcUuNAisqqLwjNHUrBxc"


# Copier les fichiers nécessaires
COPY requirements.txt requirements.txt
COPY app.py app.py
COPY gcp_key.json gcp_key.json

# Installer les dépendances
RUN pip install --no-cache-dir -r requirements.txt

# Exposer le port 8080 (valeur utilisée par défaut)
EXPOSE 8080

# Lancer Streamlit
CMD ["streamlit", "run", "app.py", "--server.port=8080", "--server.address=0.0.0.0"]