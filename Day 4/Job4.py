class Forme():
    def __init__(self):
        pass
    def aire(self):
        return 0

class Rectangle(Forme):
    def __init__(self,largeur,longueur):
        super().__init__()
        self.__largeur = largeur
        self.__longueur = longueur
    def aire(self):
        return self.__longueur*self.__largeur
    def get_aire(self):
        return f"{self.aire()}cm²"

abcd = Rectangle(3,2)
print(abcd.get_aire())