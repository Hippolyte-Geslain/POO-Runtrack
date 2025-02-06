import random
class Cartes():
    def __init__(self, valeur, couleur):
        self.couleur = couleur
        self.valeur = valeur
    def __str__(self):
        return f"{self.valeur} de {self.couleur}"

    def __repr__(self):
        return self.__str__()

class Paquet():
    def __init__(self):
        self.cartes = []
        valeurs = ["As", "2", "3", "4", "5", "6", "7", "8", "9", "10", "Valet", "Dame", "Roi"]
        couleurs = ["Cœur", "Carreau", "Trèfle", "Pique"]

        for valeur in valeurs:
            for couleur in couleurs:
                self.cartes.append(Cartes(valeur,couleur))
    
    def melanger_carte(self):
        random.shuffle(self.cartes)
    
    def distribuer_carte(self):
        return self.cartes.pop()