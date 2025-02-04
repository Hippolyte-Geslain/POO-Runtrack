class Livre():
    def __init__(self,titre,auteur,nombre_de_pages):
        self.__titre = titre
        self.__auteur = auteur
        if nombre_de_pages > 0:
            self.__nombre_de_pages = nombre_de_pages
        else:
            nombre_de_pages = 'Le nombre de pages doit être un entier positif'
            print(nombre_de_pages)
            exit()
    def set_titre(self,titre):
        self.__titre = titre
    def set_auteur(self,auteur):
        self.__auteur = auteur
    def set_nombre_de_pages(self,nombre_de_pages):
        if nombre_de_pages > 0:
            self.__nombre_de_pages = nombre_de_pages
        else:
            print('Le nombre de pages doit être un entier positif')
    def set_livre(self, titre, auteur, nombre_de_pages):
        self.__titre = titre
        self.__auteur = auteur
        self.__nombre_de_pages = nombre_de_pages
    def get_titre(self):
        return self.__titre
    def get_auteur(self):
        return self.__auteur
    def get_nombre_de_pages(self):
        try:
            return self.__nombre_de_pages
        except AttributeError:
            print('Le nombre de pages doit être un entier positif')
    def get_livre(self):
        return self.__titre,self.__auteur,self.get_nombre_de_pages()
sherlock = Livre('Le Chien des Baskerville','Conan Doyle',0)
print(sherlock.get_titre())
print(sherlock.get_auteur())
print(sherlock.get_nombre_de_pages())
print(sherlock.get_livre())
sherlock.set_titre('The Hound of Baskerville')
sherlock.set_auteur('Sir Arthur Conan Doyle')
sherlock.set_nombre_de_pages(212)
print(sherlock.get_livre())
sherlock.set_livre('Oui-oui','Enid Blyton',32)
print(sherlock.get_livre())