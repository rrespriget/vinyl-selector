import streamlit as st
import pandas as pd
from google.cloud import bigquery
import os
import streamlit.web.cli as stcli

# GOOGLE_APPLICATION_CREDENTIALS
credentials_path = os.environ["GOOGLE_APPLICATION_CREDENTIALS"] = "gcp_key.json"

# Fonction pour charger les données
@st.cache_data
def load_data():
    # Vérifie si les credentials sont définis
    #credentials_path = os.getenv("GOOGLE_APPLICATION_CREDENTIALS")
    if not credentials_path or not os.path.exists(credentials_path):
        raise FileNotFoundError(
            f"Le fichier de clé est introuvable. Assurez-vous que GOOGLE_APPLICATION_CREDENTIALS pointe vers un chemin valide. Chemin actuel : {credentials_path}"
        )

    # Charger les données depuis BigQuery
    client = bigquery.Client()
    query = """
    SELECT *
    FROM `vinyl-selector.vinyl_dataset_dev.vinyl_collection`
    """
    return client.query(query).to_dataframe()

# Charger les données et afficher les options utilisateur
st.title("Vinyl Selector")
data = load_data()

artist = st.selectbox("Sélectionner un artiste:", options=[""] + list(data["artiste"].unique()))
genre = st.selectbox("Sélectionner un genre:", options=[""] + list(data["genre"].unique()))

# Filtrer les données
filtered_data = data.copy()
if artist:
    filtered_data = filtered_data[filtered_data["artiste"] == artist]
if genre:
    filtered_data = filtered_data[filtered_data["genre"] == genre]

# Afficher les résultats
st.dataframe(filtered_data)

# Configuration du port
PORT = os.getenv("PORT", "8080")