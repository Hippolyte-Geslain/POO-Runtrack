from Job2 import Livre

class Livre():
    def __init__(self):
        self.__disponible = True
    def verification(self):
        if self.__disponible == True:
            return True
        else:
            return False
    def emprunter(self):
        if self.verification() == True:
            self.disponible = False
    def rendre(self):
        if self.verification() == False:
            self.disponible = True