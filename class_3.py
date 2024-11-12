class Rectangle:
    def __init__(self, largeur, longueur):
        self.largeur = largeur
        self.longueur = longueur

    def perimetre(self):
        return 2 * (self.largeur + self.longueur)

    def aire(self):
        return self.largeur * self.longueur