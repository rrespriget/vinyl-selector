# 🎵 Vinyl Selector

## 📝 Description
Vinyl Selector est une application web développée avec Streamlit qui permet de gérer une collection de vinyles. Elle offre une interface utilisateur intuitive pour rechercher des vinyles sur Discogs et les ajouter à votre collection personnelle stockée dans Google BigQuery.

## 🚀 Fonctionnalités

- 🔍 Recherche de vinyles sur Discogs avec gestion du rate limiting
- ➕ Ajout de vinyles à votre collection
- 📊 Visualisation de votre collection
- 🏷️ Filtrage par artiste, genre, année
- 💾 Stockage des données sur Google BigQuery
- 🔄 Mise en cache des recherches pour optimiser les performances

## 🛠️ Installation

1. Clonez le repository
```bash
git clone https://github.com/votre-username/vinyl-selector.git
cd vinyl-selector
```

2. Créez un environnement virtuel
```bash
python -m venv env
source env/bin/activate  # Sur Unix/MacOS
env\Scripts\activate     # Sur Windows
```

3. Installez les dépendances
```bash
pip install -r requirements.txt
```

## 🔧 Configuration

### Méthode 1 : Utilisation de secrets.toml (Recommandée)
1. Créez un dossier `.streamlit` à la racine du projet
2. Créez un fichier `secrets.toml` dans ce dossier avec :
```toml
DISCOGS_API_TOKEN = "votre_token_ici"
GOOGLE_APPLICATION_CREDENTIALS = "path/to/your/credentials.json"
```

### Méthode 2 : Variables d'environnement Docker
Lancez le container avec les variables d'environnement :
```bash
docker run -p 8080:8080 \
    -e PORT=8080 \
    -e DISCOGS_API_TOKEN=votre_token_discogs \
    -e GOOGLE_APPLICATION_CREDENTIALS=path/to/credentials.json \
    vinyl-selector
```

### Configuration des APIs

#### Google Cloud Platform
1. Créez un projet sur Google Cloud Platform
2. Activez l'API BigQuery
3. Créez un compte de service et téléchargez les credentials JSON
4. Configurez le chemin vers les credentials dans votre configuration

#### Discogs
1. Créez un compte sur [Discogs](https://www.discogs.com/)
2. Allez dans [Paramètres > Développeurs](https://www.discogs.com/settings/developers)
3. Générez un token d'accès personnel
4. Ajoutez le token dans votre configuration

## 🚀 Lancement

### En local
```bash
streamlit run app.py
```

### Avec Docker
```bash
# Build de l'image
docker build -t vinyl-selector .

# Lancement du container
docker run -p 8080:8080 vinyl-selector
```

L'application sera accessible à l'adresse : http://localhost:8080

## 📁 Structure du Projet

```
vinyl-selector/
├── .streamlit/           # Configuration Streamlit
│   └── secrets.toml
├── app.py               # Point d'entrée de l'application
├── pages/              # Pages Streamlit
│   └── Recherche_Discogs.py
├── api/                # Wrappers API
│   ├── discogs_wrapper.py
│   └── bigquery_client.py
├── Dockerfile          # Configuration Docker
├── requirements.txt    # Dépendances
└── README.md
```

## 🛠️ Technologies Utilisées

- Python 3.8+
- Streamlit
- Google BigQuery
- Discogs API
- Pandas
- Docker

## ⚠️ Limitations Connues

- Rate limiting Discogs : 60 requêtes/minute (authentifié)
- Mise en cache des recherches limitée aux 100 dernières requêtes

## 📝 TODO

- [ ] Ajouter des tests unitaires
- [ ] Implémenter la modification des vinyles
- [ ] Ajouter des statistiques sur la collection
- [ ] Améliorer la gestion des erreurs
- [ ] Ajouter une fonction d'export
- [ ] Implémenter un système de cache plus robuste (Redis)