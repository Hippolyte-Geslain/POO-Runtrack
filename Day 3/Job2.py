class CompteBancaire():
    def __init__(self,numero_de_compte,prenom,nom,solde,decouvert):
        self.__numero_de_compte = numero_de_compte
        self.__prenom = prenom
        self.__nom = nom
        self.__solde = solde
        self.__decouvert = decouvert
    def afficher(self):
        return (f"Le compte {self.__numero_de_compte} appartenant à {self.__prenom} {self.__nom} a pour solde {self.__solde}€")
    def afficher_solde(self):
        return (f"Le solde du compte est de {self.__solde}€")
    def versement(self, montant):
        try:
            int(montant)
            self.__solde = self.__solde + montant
            return self.afficher_solde()
        except ValueError:
            return("Le montant du versement doit être un entier")
    def retrait(self, montant):
        try:
            int(montant)
            if montant>self.__solde:
                if self.__decouvert:
                    self.__solde = self.__solde - montant
                    return self.afficher_solde()
                else:
                    return("Vous n'avez pas les fonds nécessaires")
            else:
                self.__solde = self.__solde - montant
                return self.afficher_solde()
        except ValueError:
            print("Le montant du retrait doit être un entier")
        
            

axel = CompteBancaire(1415,'Axel','Achart',-10,False)
print(axel.afficher())
print(axel.afficher_solde())
print(axel.versement(12))
print(axel.retrait(10))