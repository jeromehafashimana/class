class CompteBancaire:
    def __init__(self, titulaire, solde=0.0):
        self.titulaire = titulaire
        self.__solde = solde  

    def deposer(self, montant):
        if montant > 0:
            self.__solde += montant
            print(f"Déposé: {montant}€. Nouveau solde: {self.__solde}€")
        else:
            print("Le montant à déposer doit être positif.")

    def retirer(self, montant):
        if 0 < montant <= self.__solde:
            self.__solde -= montant
            print(f"Retiré: {montant}€. Nouveau solde: {self.__solde}€")
        else:
            print("Montant invalide ou fonds insuffisants.")

    def afficher_solde(self):
        print(f"Solde actuel de {self.titulaire}: {self.__solde}€")


compte1 = CompteBancaire("Alice", 100.0)
compte1.afficher_solde()
compte1.deposer(50)
compte1.retirer(30)
compte1.afficher_solde()
