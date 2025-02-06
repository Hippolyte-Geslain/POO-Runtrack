import math
class Forme():
    def __init__(self):
        pass
    def aire(self):
        return 0

class Cercle(Forme):
    def __init__(self,radius):
        super().__init__()
        self.__radius = radius
    def aire(self):
        return self.__radius*self.__radius*math.pi
    def get_aire(self):
        return f"{self.aire()}cm²"

o = Cercle(3)
print(o.get_aire())