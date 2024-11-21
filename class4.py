import requests

url = "https://jsonplaceholder.typicode.com/posts"

try:
 
    response = requests.get(url)
    
    
    if response.status_code == 200:
        
        data = response.json()
        
        
        print("Voici les données récupérées :")
        for i, post in enumerate(data[:5]):  # Limite aux 5 premiers résultats
            print(f"Post {i + 1}:")
            print(f"  Titre: {post['title']}")
            print(f"  Contenu: {post['body']}")
            print()
    else:
        print(f"Erreur: Statut {response.status_code}")

except requests.exceptions.RequestException as e:
    print(f"Une erreur s'est produite : {e}")
