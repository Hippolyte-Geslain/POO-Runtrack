class Rectangle():
    def __init__(self,longueur,largeur):
        self.__longueur = longueur
        self.__largeur = largeur
    def perimetre(self):
        return (f"{2*(self.__largeur+self.__longueur)}cm")
    def surface(self):
        return (f"{self.__largeur*self.__longueur}cm²")
    def get_longueur(self):
        return self.__longueur
    def get_largeur(self):
        return self.__largeur
    def set_longueur(self, longueur):
        self.__longueur = longueur
    def set_largeur(self,largeur):
        self.__largeur = largeur

class Parallelepipede(Rectangle):
    def __init__(self, longueur, largeur,hauteur):
        super().__init__(longueur, largeur)
        self.__longueur = longueur
        self.__largeur = largeur
        self.__hauteur = hauteur
    def volume(self):
        return (self.__longueur*self.__largeur*self.__hauteur)

abcd = Parallelepipede(12,4,3)
print(abcd.perimetre())
print(abcd.surface())
print(abcd.get_largeur())
print(abcd.get_longueur())
abcd.set_largeur(1)
abcd.set_longueur(2)
print(abcd.volume())