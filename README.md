# 🎵 Vinyl Selector

## 📝 Description
Vinyl Selector est une application web développée avec Streamlit qui permet de gérer une collection de vinyles. Elle offre une interface utilisateur intuitive pour rechercher des vinyles sur Discogs et les ajouter à votre collection personnelle stockée dans Google BigQuery.

## 🚀 Fonctionnalités

- 🔍 Recherche de vinyles sur Discogs
- ➕ Ajout de vinyles à votre collection
- 📊 Visualisation de votre collection
- 🏷️ Filtrage par artiste, genre, année
- 💾 Stockage des données sur Google BigQuery

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

4. Configurez vos variables d'environnement
```bash
# Créez un fichier .env à la racine du projet
GOOGLE_APPLICATION_CREDENTIALS=path/to/your/credentials.json
DISCOGS_TOKEN=your_discogs_token
```

## 🔧 Configuration

### Google Cloud Platform
1. Créez un projet sur Google Cloud Platform
2. Activez l'API BigQuery
3. Créez un compte de service et téléchargez les credentials JSON
4. Configurez la variable d'environnement GOOGLE_APPLICATION_CREDENTIALS

### Discogs
1. Créez un compte sur Discogs
2. Générez un token d'accès personnel
3. Ajoutez le token dans votre fichier .env

## 🚀 Lancement

```bash
streamlit run app.py
```

L'application sera accessible à l'adresse : http://localhost:8501

## 📁 Structure du Projet

```
vinyl-selector/
├── app.py                 # Point d'entrée de l'application
├── pages/                 # Pages Streamlit
│   └── Recherche_Discogs.py
├── api/                   # Wrappers API
│   ├── discogs_wrapper.py
│   └── bigquery_client.py
├── requirements.txt       # Dépendances
└── README.md
```

## 🛠️ Technologies Utilisées

- Python 3.8+
- Streamlit
- Google BigQuery
- Discogs API
- Pandas

## 📝 TODO

- [ ] Ajouter des tests unitaires
- [ ] Implémenter la modification des vinyles
- [ ] Ajouter des statistiques sur la collection
- [ ] Améliorer la gestion des erreurs
- [ ] Ajouter une fonction d'export

## 👥 Contribution

Les contributions sont les bienvenues ! N'hésitez pas à ouvrir une issue ou à soumettre une pull request.

## 📄 Licence

Ce projet est sous licence MIT. Voir le fichier `LICENSE` pour plus de détails. 