import math
class Cercle(): 
    def __init__(self, rayon): #constructor avec valeur de base
        self.rayon = rayon
    def changerRayon(self, rayon):
        self.rayon = rayon
    def afficherInfos(self):
        print(f"Circonférence = {self.circonférence}\nAire = {self.aire}\nDiamètre = {self.diametre}") #utilisation des méthodes créées pour l'affichage de toutes les infos
    def circonférence(self):
        print(f"La circonférence du cercle est de : {math.pi*2*self.rayon} cacahuètes")
    def aire(self):
        print(f"L'aire du cercle est de : {math.pi*self.rayon*self.rayon} cacahuètes")
    def diametre(self):
        print(f"Le diamètre du cercle est de : {2*self.rayon} cacahuètes")

o = Cercle(4)
b = Cercle(7)

o.afficherInfos()
o.circonférence()
o.diametre()
o.aire()

b.afficherInfos()
b.circonférence()
b.diametre()
b.aire()