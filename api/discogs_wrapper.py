import os
import discogs_client
from dotenv import load_dotenv

# Charger les variables d’environnement (fichier .env à la racine du projet)
load_dotenv(dotenv_path=os.path.join(os.path.dirname(__file__), '../.env'))
print("🔑 DEBUG: DISCOGS_API_TOKEN =", os.getenv("DISCOGS_API_TOKEN"))

class DiscogsClient:
    """
    Client pour interagir avec l'API de Discogs.
    Permet la recherche de vinyles et la récupération des détails d’un album.
    """

    def __init__(self):
        self.token = os.getenv("DISCOGS_API_TOKEN")
        if not self.token:
            raise ValueError("⚠️ Le token Discogs n'est pas défini ! Ajoutez-le dans l'environnement.")

        # Initialiser le client Discogs
        self.client = discogs_client.Client('VinylSelector/1.0', user_token=self.token)

    def search_vinyl(self, query, limit=5):
        """
        Recherche un vinyle sur Discogs.

        :param query: Nom de l’album ou de l’artiste.
        :param limit: Nombre de résultats à afficher (par défaut : 5).
        :return: Liste des résultats sous forme de dictionnaires.
        """
        try:
            results = list(self.client.search(query, type='release', format='vinyl'))[:limit]
            return [
                {
                    "id": release.id,
                    "title": release.title,
                    "year": release.year,
                    "artist": ", ".join(artist.name for artist in release.artists),
                    "label": ", ".join(label.name for label in release.labels),
                    "country": release.country,
                    "cover": release.images[0]['uri'] if release.images else None
                }
                for release in results
            ]
        except Exception as e:
            print(f"❌ Erreur lors de la recherche de vinyles : {e}")
            return []

    def get_release_details(self, release_id):
        """
        Récupère les détails d’un vinyle en fonction de son ID Discogs.

        :param release_id: ID de la sortie Discogs.
        :return: Dictionnaire contenant les détails de l’album.
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
            print(f"❌ Erreur lors de la récupération des détails de l’album : {e}")
            return None

# Test rapide
if __name__ == "__main__":
    discogs = DiscogsClient()
    
    # Test de la recherche
    results = discogs.search_vinyl("Abbey Road Beatles")
    if results:
        print("✅ Résultats de la recherche :")
        for r in results:
            print(f"- {r['title']} ({r['year']}) - {r['artist']}")

    # Test des détails d’un album
    if results:
        release_id = results[0]["id"]
        details = discogs.get_release_details(release_id)
        print("\n🎵 Détails du premier vinyle trouvé :")
        print(details)