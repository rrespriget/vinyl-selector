import sys
import os
#from dotenv import load_dotenv
project_root = os.getcwd()
sys.path.append(project_root)
from api.discogs_wrapper import DiscogsClient

print(f"🔍 DEBUG: DISCOGS_API_TOKEN = {repr(os.getenv('DISCOGS_API_TOKEN'))}")

# Initialisation du client Discogs
discogs = DiscogsClient()
results = discogs.search_vinyl("slipknot")
print(results)
