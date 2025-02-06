import random
from string import capwords
from xmlrpc.client import TRANSPORT_ERROR
import Joueur
import Cartes
class Jeu():
    def __init__(self):
        self.running = True
        self.joueur1 = Joueur.Joueur('J')
        self.croupier = Joueur.Croupier()
        self.paquet = Cartes.Paquet()
        
    def afficher_main(self):
        print(self.joueur1.main)
    def choix(self):
        avarice = True
        while avarice:
            choix = input('Voulez-vous tirer une carte de plus ?\nOu bien passer ?\n(Y or N)')
            if choix == 'Y' or 'y':
                self.joueur1.tirer_carte(self.paquet.distribuer_carte())
            if choix == 'N' or 'n':
                print('Très bien Monsieur')
    def end_game(self):
        print('GG')
    def run(self):
        while self.running:            
            self.paquet.melanger_carte()
            self.joueur1.tirer_carte(self.paquet.distribuer_carte())
            self.joueur1.tirer_carte(self.paquet.distribuer_carte())
            self.afficher_main()
            self.choix()
            #rajouter plus de tours et de fonctionnalités
            self.running = False
game = Jeu()
game.run()