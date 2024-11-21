# Utiliser le module *requests* et afficher les donnees

import requests


url = "https://exemple.com/api/donnees"


response = requests.get(url)


if response.status_code == 200:
    
    print(response.json())
else:
    print(f"Erreur {response.status_code} : Impossible de récupérer les données.")
