class Point():
    def __init__(self,x,y): #constructor
        self.x = x
        self.y = y
    def afficherLesPoints(self): #méthodes
        print(f'x = {self.x} y = {self.y}')
    def afficherX(self):
        print(f'x = {self.x}')
    def afficherY(self):
        print(f'y = {self.y}')
    def changerX(self,new_x):
        self.x = new_x
    def changerY(self,new_y):
        self.y = new_y

a = Point(1,1) #initialisation
a.afficherLesPoints()
a.afficherX()
a.afficherY()
a.changerX(4)
a.changerY(3)
a.afficherX()
a.afficherY()
a.afficherLesPoints() #appel méthodes de l'objet 'a'