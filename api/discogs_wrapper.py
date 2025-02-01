import os
import discogs_client
from dotenv import load_dotenv
import streamlit as st
import time
from functools import lru_cache

# Charger les variables d'environnement (fichier .env à la racine du projet)
load_dotenv(dotenv_path=os.path.join(os.path.dirname(__file__), '../.env'))
print("🔑 DEBUG: DISCOGS_API_TOKEN =", os.getenv("DISCOGS_API_TOKEN"))

class DiscogsClient:
    """
    Client pour interagir avec l'API de Discogs.
    Permet la recherche de vinyles et la récupération des détails d'un album.
    """

    def __init__(self):
        # Essayer de récupérer le token dans cet ordre :
        # 1. Variable d'environnement directe
        # 2. Fichier .env (développement local)
        # 3. Secrets Streamlit (déploiement GCP)
        
        self.token = os.getenv('DISCOGS_API_TOKEN')
        
        if not self.token:
            load_dotenv()
            self.token = os.getenv('DISCOGS_API_TOKEN')
            
        if not self.token:
            try:
                self.token = st.secrets["DISCOGS_API_TOKEN"]
            except:
                raise ValueError("❌ Token Discogs non trouvé dans les variables d'environnement")
        
        self.client = discogs_client.Client('VinylSelector/1.0', 
                                          user_token=self.token)

    @lru_cache(maxsize=100)  # Cache les 100 dernières recherches
    def search_release(self, query):
        """
        Recherche un vinyle sur Discogs.

        :param query: Nom de l'album ou de l'artiste.
        :return: Liste des résultats sous forme de dictionnaires.
        """
        try:
            time.sleep(1)  # Ajoute un délai d'1 seconde entre chaque requête
            print(f"Recherche de: {query}")
            
            # Récupérer les résultats sans slice
            results = self.client.search(query, type='release', format='Vinyl')
            
            # Convertir l'itérateur en liste et limiter à 10 résultats
            results_list = list(results)[:10]
            
            print(f"Nombre de résultats trouvés: {len(results_list) if results_list else 0}")
            
            formatted_results = []
            for r in results_list:
                try:
                    formatted_result = {
                        'id': r.id,
                        'title': r.title,
                        'artist': r.artists[0].name if r.artists else "Artiste inconnu",
                        'year': r.year,
                        'label': r.labels[0].name if r.labels else "Label inconnu",
                        'country': getattr(r, 'country', "Pays inconnu"),
                        'genres': getattr(r, 'genres', []),
                        'cover': getattr(r, 'thumb', None)
                    }
                    formatted_results.append(formatted_result)
                    print(f"Résultat formaté ajouté: {formatted_result['title']}")
                except Exception as e:
                    print(f"Erreur lors du formatage d'un résultat: {str(e)}")
                    continue
                    
            print(f"Nombre total de résultats formatés: {len(formatted_results)}")
            return formatted_results
            
        except Exception as e:
            print(f"Erreur lors de la recherche Discogs: {str(e)}")
            return []

    def get_release_details(self, release_id):
        """
        Récupère les détails d'un vinyle en fonction de son ID Discogs.

        :param release_id: ID de la sortie Discogs.
        :return: Dictionnaire contenant les détails de l'album.
        """
        try:
            release = self.client.release(release_id)
            return {
                "title": release.title,
                "year": release.year,
                "artists": [artist.name for artist in release.artists],
                "labels": [label.name for label in release.labels],
                "genres": release.genres,
                "styles": release.styles,
                "country": release.country,
                "tracklist": [track.title for track in release.tracklist],
                "cover": release.images[0]['uri'] if release.images else None
            }
        except Exception as e:
            print(f"❌ Erreur lors de la récupération des détails de l'album : {e}")
            return None

# Test rapide
if __name__ == "__main__":
    discogs = DiscogsClient()
    
    # Test de la recherche
    results = discogs.search_release("Abbey Road Beatles")
    if results:
        print("✅ Résultats de la recherche :")
        for r in results:
            print(f"- {r['title']} ({r['year']}) - {r['artist']}")

    # Test des détails d'un album
    if results:
        release_id = results[0]["id"]
        details = discogs.get_release_details(release_id)
        print("\n🎵 Détails du premier vinyle trouvé :")
        print(details)