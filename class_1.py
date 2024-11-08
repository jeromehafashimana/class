class Employe:
    def __init__(self, nom, salaire):
        self.nom = nom
        self.salaire = salaire

    def afficher_informations(self):
        print(f"Nom : {self.nom}, Salaire : {self.salaire}")

class Manager(Employe):
    def __init__(self, nom, salaire, equipe=None):
        super().__init__(nom, salaire)
        self.equipe = equipe if equipe else []

    def ajouter_membre(self, employe):
        self.equipe.append(employe)

    def afficher_equipe(self):
        print(f"Équipe de {self.nom}:")
        for employe in self.equipe:
            print(f"- {employe.nom}")


manager = Manager("Claire", 5000)
employe1 = Employe("Alice", 3000)
employe2 = Employe("John", 3200)

manager.ajouter_membre(employe1)
manager.ajouter_membre(employe2)

manager.afficher_informations()
manager.afficher_equipe()
