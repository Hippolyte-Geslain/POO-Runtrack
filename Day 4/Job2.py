class Personne():
    def __init__(self):
        self.age = 14
    def afficherAge(self):
        print(self.age)
    def bonjour(self):
        print('Hello')
    def modifierAge(self,age):
        try:
            int(age)
            self.age = age
        except ValueError:
            print("Utiliser un nombre entier pour modifier l'age")

class Eleve(Personne):
    def __init__(self):
        super().__init__()
    def aller_en_cours(self):
        print("Je vais en cours")
    def afficherAge(self):
        print(f"J'ai {self.age} ans")

class Professeur(Personne):
    def __init__(self, matiereEnseignee):
        super().__init__()
        self.__matiereEnseignee = matiereEnseignee
    def enseigner(self):
        print("Le cours va commencer")

hippo = Eleve()
hippo.afficherAge()
hippo.bonjour()
hippo.aller_en_cours()
hippo.modifierAge(15)
hippo.afficherAge()
akram = Professeur('IA')
akram.modifierAge(40)
akram.afficherAge()
akram.bonjour()
akram.enseigner()