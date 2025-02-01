import streamlit as st
from api.discogs_wrapper import DiscogsClient
from api.bigquery_client import BigQueryClient

# 🔹 Configuration de BigQuery
PROJECT_ID = "vinyl-selector"
DATASET_ID = "vinyl_dataset_dev"
TABLE_ID = "vinyl_collection"

# 🔹 Initialisation des clients Discogs et BigQuery
discogs = DiscogsClient()
bigquery_client = BigQueryClient(PROJECT_ID, DATASET_ID, TABLE_ID)

# Initialisation des états de session
if "search_results" not in st.session_state:
    st.session_state.search_results = []
if "added_vinyls" not in st.session_state:
    st.session_state.added_vinyls = set()
if "query" not in st.session_state:
    st.session_state.query = ""

# 🔍 Titre de la page
st.title("🔍 Recherche de Vinyles sur Discogs")

# Fonction de callback pour la recherche
def on_search():
    if st.session_state.query:
        st.session_state.search_results = discogs.search_release(st.session_state.query)

# Fonction de callback pour l'ajout d'un vinyle
def add_vinyl(vinyl_data, vinyl_id):
    formatted_data = None
    try:
        # Debug: afficher les données reçues
        st.write("Données reçues:", vinyl_data)
        
        # Formatage des données selon la structure exacte de la table BigQuery
        formatted_data = {
            "album": vinyl_data.get("album", "Inconnu"),
            "artiste": vinyl_data.get("artiste", "Inconnu"),
            "annee_sortie": int(vinyl_data.get("annee_sortie", 0)),
            "genre": "Inconnu",
            "label": vinyl_data.get("label", "Inconnu")
        }
        
        # Debug: afficher les données formatées
        st.write("Données formatées:", formatted_data)
        
        success = bigquery_client.add_vinyl(formatted_data)
        if success:
            st.session_state.added_vinyls.add(vinyl_id)
            return True
        return False
    except Exception as e:
        st.error(f"Erreur lors de l'ajout : {str(e)}")
        if formatted_data:
            st.write("Données problématiques:", formatted_data)
        else:
            st.write("Erreur avant le formatage des données")
        return False

# Barre de recherche utilisateur
st.text_input("Entrez le nom d'un vinyle ou d'un artiste", 
              key="query", 
              on_change=on_search)

# Bouton de recherche
if st.button("Rechercher"):
    on_search()

# Affichage des résultats
if st.session_state.search_results:
    st.subheader(f"📄 Résultats pour : {st.session_state.query}")

    for r in st.session_state.search_results:
        with st.container():
            st.markdown("---")

            st.subheader(r["title"])
            st.write(f"🎤 **Artiste(s) :** {r['artist']}")
            if r['genres']:
                st.write(f"🎵 **Genre(s) :** {', '.join(r['genres'])}")
            if r.get('styles'):
                st.write(f"🎨 **Style(s) :** {', '.join(r['styles'])}")
            st.write(f"📅 **Année :** {r['year']}")
            st.write(f"🏷 **Label :** {r['label']}")
            st.write(f"🌍 **Pays :** {r['country']}")


            if r["cover"]:
                st.image(r["cover"], width=200)

            vinyl_id = str(r['id'])
            if vinyl_id not in st.session_state.added_vinyls:
                vinyl_data = {
                    "artiste": r.get("artist", "Inconnu"),
                    "album": r.get("title", "Inconnu"),
                    "annee_sortie": r.get("year", "0"),      # Sera converti en INT64
                    "genre": "Inconnu",
                    "label": r.get("label", "Inconnu")
                }
                
                col1, col2 = st.columns([1, 4])
                with col1:
                    if st.button("➕ Ajouter", key=f"add_{vinyl_id}"):
                        if add_vinyl(vinyl_data, vinyl_id):
                            st.success("✅ Ajouté !")
                        else:
                            st.error("❌ Erreur")
            else:
                st.info("✓ Déjà dans votre collection")