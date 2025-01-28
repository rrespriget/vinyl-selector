import os
from google.cloud import bigquery

# Charger les credentials si la variable d'environnement n'est pas définie
if not os.getenv("GOOGLE_APPLICATION_CREDENTIALS"):
    os.environ["GOOGLE_APPLICATION_CREDENTIALS"] = os.path.abspath("../credentials.json")

class BigQueryClient:
    def __init__(self, project_id, dataset_id, table_id):
        self.client = bigquery.Client() 
        self.project_id = project_id
        self.dataset_id = dataset_id
        self.table_id = table_id
        self.table_ref = f"{self.project_id}.{self.dataset_id}.{self.table_id}"

    def add_vinyl(self, vinyl_data):
        try:
            table = self.client.get_table(self.table_ref)
            rows_to_insert = [vinyl_data]
            errors = self.client.insert_rows_json(table, rows_to_insert)
            if errors:
                print(f"❌ Erreur lors de l'insertion : {errors}")
                return False
            else:
                print(f"✅ Vinyle ajouté : {vinyl_data['title']}")
                return True
        except Exception as e:
            print(f"❌ Erreur BigQuery : {e}")
            return False