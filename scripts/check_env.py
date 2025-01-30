import os

def check_env_variables():
    print("\n🔍 Vérification des variables d'environnement :\n")
    
    # Liste des variables à vérifier
    env_vars = {
        "GOOGLE_APPLICATION_CREDENTIALS": "Chemin vers les credentials Google",
        "DISCOGS_API_TOKEN": "Token Discogs"  # Modifié ici
    }
    
    all_good = True
    
    for var, description in env_vars.items():
        value = os.getenv(var)
        if value:
            masked_value = value[:5] + "..." + value[-5:] if len(value) > 10 else "***"
            print(f"✅ {var} : {masked_value}")
        else:
            print(f"❌ {var} non défini")
            print(f"   Description : {description}")
            all_good = False
    
    if all_good:
        print("\n✨ Toutes les variables d'environnement sont correctement définies!")
    else:
        print("\n⚠️ Certaines variables d'environnement sont manquantes!")

if __name__ == "__main__":
    check_env_variables() 