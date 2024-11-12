class RechercheBinaire:
    
    def rechercher(liste, cible):
        gauche, droite = 0, len(liste) - 1
        while gauche <= droite:
            milieu = (gauche + droite) // 2
            if liste[milieu] == cible:
                return milieu
            elif liste[milieu] < cible:
                gauche = milieu + 1
            else:
                droite = milieu - 1
        return -1
