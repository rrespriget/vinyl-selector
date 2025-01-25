import sys
import os
import streamlit as st
project_root = os.getcwd()
sys.path.append(project_root)
from api.discogs_wrapper import DiscogsClient

# Initialisation du client Discogs
discogs = DiscogsClient()

st.title("🔍 Recherche de Vinyles sur Discogs")

# Barre de recherche
query = st.text_input("Entrez le nom d’un vinyle ou d’un artiste")

if st.button("Rechercher"):
    if query:
        results = discogs.search_vinyl(query)
        if results:
            for r in results:
                st.subheader(r["title"])
                st.write(f"**Artiste(s) :** {r['artist']}")
                st.write(f"**Année :** {r['year']}")
                st.write(f"**Label :** {r['label']}")
                st.write(f"**Pays :** {r['country']}")
                if r["cover"]:
                    st.image(r["cover"], width=200)
        else:
            st.error("Aucun vinyle trouvé.")
    else:
        st.warning("Veuillez entrer un nom de vinyle ou d'artiste.")
