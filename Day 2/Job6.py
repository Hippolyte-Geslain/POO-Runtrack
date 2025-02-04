commandes = [0]
class Commande():
    def __init__(self):
        self.__numero_de_commande = commandes[-1] +1
        self.__plats = {}
        self.__statut = 'En cours'
    def add_plat(self,nom,prix,quantite):
        self.__plats.update({nom :{"Prix":prix,"Quantite":quantite}})
    def annuler_commande(self):
        self.__statut = 'Annulée'

    def __calculer_prix_HTC(self):
        prix_HTC = 0
        for plat in self.__plats.values():
            prix_HTC += plat["Prix"] * plat["Quantite"]        
        self.__prix_HTC = prix_HTC
        return self.__prix_HTC
    def afficher_prix_HTC(self):
        total_HTC = self.__calculer_prix_HTC()
        return(f"Le prix HTC est de {total_HTC}€")
    
    def __calculer_tva(self):
        self.__tva = (self.__calculer_prix_HTC() * 0.05)
        return self.__tva
    def afficher_tva(self):
        tva = self.__calculer_tva()
        return(f"La TVA est de {tva}€")
    
    def __calculer_prix_total(self):
        self.__prix_total = self.__calculer_prix_HTC() * 1.05
        return self.__prix_total    
    def afficher_prix_total(self):
        total = self.__calculer_prix_total()
        return(f"Le prix total est de {total}€")

    def afficher_infos(self):
        return self.__numero_de_commande,self.__plats, self.__statut

table1 = Commande()
table1.add_plat('Escalope de Poulet',15,2)
table1.add_plat('Burger Berger',12,1)
table1.annuler_commande()
print(table1.afficher_infos())
print(table1.afficher_prix_HTC())
print(table1.afficher_tva())
print(table1.afficher_prix_total())