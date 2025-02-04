class Personne():
    def __init__(self, prenom, nom): #constructor
        self.nom = nom
        self.prenom = prenom
    def SePresenter(self): #méthode
        print(f'Je suis {self.prenom} {self.nom}')
    
x = Personne('John','Doe') #initialisation de l'instance/objet
y = Personne('Hippolyte','Geslain')
x.SePresenter() #application de la méthode sur l'objet
y.SePresenter()