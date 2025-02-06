class Vehicule():
    def __init__(self,marque,modele,annee,prix):
        self.__marque = marque
        self.__modele = modele
        self.__annee = annee
        self.__prix = prix
    def InformationsVehicule(self):
        return f"La marque du véhicule : {self.__marque}\nLe modèle du véhicule{self.__modele}\nL'année de construction du véhicule : {self.__annee}\nLe prix du véhicule : {self.__prix}€"

class Voiture(Vehicule):
    def __init__(self, marque, modele, annee, prix):
        super().__init__(marque, modele, annee, prix)
        self.__portes = 4
    def InformationsVehicule(self):
        return f"{super().InformationsVehicule()}\nLe véhicule a {self.__portes} portes"

axel = Voiture('Renault','Rs Line',2023,22501)
print(axel.InformationsVehicule())

class Moto(Vehicule):
    def __init__(self, marque, modele, annee, prix):
        super().__init__(marque, modele, annee, prix)
        self.__roues = 2
    def InformationsVehicule(self):
        return f"{super().InformationsVehicule()}\nLe véhicule a {self.__roues} roues"

thibault = Moto('Ducatti','sr700',2024,5000)
print(thibault.InformationsVehicule())