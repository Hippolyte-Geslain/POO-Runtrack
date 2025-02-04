class Produit():
    def __init__(self,nom,prixHT,TVA):
        self.nom = nom
        self.prixHT = prixHT
        self.TVA = TVA
    def CalculerPrixTTC(self):
        self.prixTTC = self.prixHT * (1+(self.TVA/100))
        return self.prixTTC
    def afficher(self):
        return (f"Fiche produit : {self.nom}\nPrix HT : {self.prixHT}\nTVA : {self.TVA}%\nPrix TTC : {self.CalculerPrixTTC()}€\n")
    def modifier_nom(self,nom):
        self.nom = nom
    def modifier_prix(self,prix):
        self.prixHT = prix
    def afficher_nom(self):
        return self.nom
    def afficher_prixHT(self):
        return self.prixHT
    def afficher_TVA(self):
        return self.TVA
    def afficher_prixTTC(self):
        return (f"Le prix TTC est de : {self.CalculerPrixTTC()}€")
    
shokobons = Produit('Shokobons',3,5)
chocolat = Produit('Chocolat',4,5)
pastis = Produit('Pastis',15,20)

print(shokobons.afficher(),chocolat.afficher(),pastis.afficher())
shokobons.modifier_nom('Kinder Shokolate')
shokobons.modifier_prix(5)
chocolat.modifier_nom('Lindt')
chocolat.modifier_prix(6)
pastis.modifier_nom('Ricard')
pastis.modifier_prix(18)

print(shokobons.afficher(),chocolat.afficher(),pastis.afficher())