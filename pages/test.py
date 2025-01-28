import sys
import os

# Ajouter le chemin du projet pour permettre l'import de `api/`
project_root = os.getcwd()
sys.path.append(project_root)
# Importer BigQueryClient
from api.bigquery_client import BigQueryClient

PROJECT_ID = "vinyl-selector"
DATASET_ID = "vinyl_dataset_dev"
TABLE_ID = "vinyl_collection"

bigquery_client = BigQueryClient(PROJECT_ID, DATASET_ID, TABLE_ID)

print("✅ BigQueryClient importé avec succès !")
