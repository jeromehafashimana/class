class Produit:
    def __init__(self, prix):
        self._prix = prix
    
    @property
    def prix(self):
        return self._prix
    
    @prix.setter
    def prix(self, nouveau_prix):
        if nouveau_prix > 0:
            self._prix = nouveau_prix
        else:
            raise ValueError("Le prix doit être positif")
