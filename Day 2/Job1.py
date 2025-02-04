class Rectangle():
    def __init__(self,longueur,largeur):
        self.__longueur = longueur
        self.__largeur = largeur
    def changer_dimensions(self,longueur,largeur):
        self.__longueur = longueur
        self.__largeur = largeur
    def afficher_dimensions(self):
        return self.__longueur,self.__largeur
    
abcd = Rectangle(10,5)
print(abcd.afficher_dimensions())
abcd.changer_dimensions(2,4)
print(abcd.afficher_dimensions())