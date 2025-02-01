from api.discogs_wrapper import DiscogsClient
from api.bigquery_client import BigQueryClient
import time

# 🔹 Configuration de BigQuery
PROJECT_ID = "vinyl-selector"
DATASET_ID = "vinyl_dataset_dev"
TABLE_ID = "vinyl_collection"

# 🔹 Initialisation des clients Discogs et BigQuery
discogs = DiscogsClient()
bigquery_client = BigQueryClient(PROJECT_ID, DATASET_ID, TABLE_ID)

# Test de la recherche
try:
    query = "Jackson 5"
    print(f"🔍 Recherche en cours pour : '{query}'")
    
    results = discogs.search_release(query)
    
    if results:
        # Afficher les 5 premiers résultats
        for i, release in enumerate(results[:5], 1):
            print(f"\n📀 Résultat {i}:")
            print(f"Titre: {release.title}")
            print(f"Année: {release.year}")
            print(f"Label: {release.label}")
    else:
        print("❌ Aucun résultat trouvé")
        
except Exception as e:
    print(f"❌ Erreur lors de la recherche: {e}")
