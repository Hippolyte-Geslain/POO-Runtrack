from ast import mod
from xmlrpc.client import TRANSPORT_ERROR


class Voiture():
    def __init__(self, marque, modele, annee, kilometrage):
        self.__marque = marque
        self.__modele = modele
        self.__annee = annee
        self.__kilometrage = kilometrage
        self.__en_marche = False
        self.__reservoir = 50
    def get_marque(self):
        return self.__marque
    def get_modele(self):
        return self.__modele
    def get_annee(self):
        return self.__annee
    def get_kilometrage(self):
        return self.__kilometrage
    def get_en_marche(self):
        return self.__en_marche
    def get_reservoir(self):
        return self.__reservoir
    def set_marque(self,marque):
        self.__marque = marque
    def set_modele(self,modele):
        self.__modele = modele
    def set_annee(self,annee):
        self.__annee = annee
    def set_kilometrage(self,kilometrage):
        self.__kilometrage = kilometrage
    def set_reservoir(self,reservoir):
        self.__reservoir = reservoir
    def demarrer(self):
        if self.verifier_plein():
            self.__en_marche = True
    def arreter(self):
        self.__en_marche = False
    def verifier_plein(self):
        if self.__reservoir > 5:
            return True
        else:
            return False