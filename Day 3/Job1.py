class Ville():
    def __init__(self,nom,nombre):
        self.__nom = nom
        self.__nombre = nombre
    def get_villev(self):
        return self.__nom
    def get_nombrev(self):
        return self.__nombre
    def ajouterPopulationv(self):
        self.__nombre = self.__nombre +1

class Personne():
    def __init__(self, prenom, age, ville):
        self.__prenom = prenom
        self.__age = age
        self.__ville = ville
    def ajouterPopulation(self):
        self.__ville.ajouterPopulationv()
    def afficher_prenom(self):
        return self.__prenom
    def afficher_age(self):
        return self.__age
    def afficher_ville(self):
        return self.__ville.get_villev()
    def afficher_nombre(self):
        return self.__ville.get_nombrev()

a = Ville('Paris',1000000)
b = Ville('Marseille',861635)
print(f"La ville de {a.get_villev()} a {a.get_nombrev()} habitants")
print(f"La ville de {b.get_villev()} a {b.get_nombrev()} habitants")
c = Personne('John',45,a)
c.ajouterPopulation()
d = Personne('Myrtille',4,a)
d.ajouterPopulation()
e = Personne('Chloé',18,b)
e.ajouterPopulation()
print(f"Mise à jour de la population de {a.get_villev()}, {a.get_nombrev()}")
print(f"Mise à jour de la population de {b.get_villev()}, {b.get_nombrev()}")