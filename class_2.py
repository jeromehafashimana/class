class Personne:
    def __init__(self, nom, age):
        self.nom = nom
        self.age = age

    def afficher_informations(self):
        print(f"Nom: {self.nom}, Âge: {self.age}")


personne1 = Personne("Alice", 30)


personne1.afficher_informations()
