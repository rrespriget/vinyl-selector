import os
from google.cloud import bigquery
import pandas as pd

# Charger les credentials si la variable d'environnement n'est pas définie
if not os.getenv("GOOGLE_APPLICATION_CREDENTIALS"):
    os.environ["GOOGLE_APPLICATION_CREDENTIALS"] = os.path.abspath("../credentials.json")

class BigQueryClient:
    def __init__(self, project_id, dataset_id, table_id):
        self.client = bigquery.Client()
        self.project_id = project_id
        self.dataset_id = dataset_id
        self.table_id = table_id
        self.table_ref = f"{project_id}.{dataset_id}.{table_id}"

    def add_vinyl(self, vinyl_data):
        try:
            # Assurez-vous que les clés correspondent exactement à la structure de la table
            row_to_insert = {
                "album": vinyl_data["album"],
                "artiste": vinyl_data["artiste"],
                "annee_sortie": vinyl_data["annee_sortie"],
                "genre": vinyl_data["genre"],
                "label": vinyl_data["label"]
            }

            # Créer un objet table
            table = self.client.get_table(self.table_ref)
            
            # Insérer les données
            errors = self.client.insert_rows_json(table, [row_to_insert])
            
            if errors == []:
                return True
            else:
                print("Erreurs lors de l'insertion :", errors)
                return False

        except Exception as e:
            print(f"Erreur lors de l'insertion : {str(e)}")
            return False

    def get_all_vinyls(self):
        query = f"""
        SELECT 
            artiste,
            album,
            annee_sortie,
            genre,
            label
        FROM {self.table_ref}
        """
        return self.client.query(query).to_dataframe()