class Student():
    def __init__(self,nom,prenom,numero_d_etudiant):
        self.__nom = nom
        self.__prenom = prenom
        self.__numero_d_etudiant = numero_d_etudiant
        self.__credits = 0
        self.__eval = self.student_eval()
    def add_credits(self,credits):
        if credits > 0:
            self.__credits = self.__credits + credits
            self.__eval = self.student_eval()
    def get_student_name(self):
        return self.__prenom, self.__nom
    def get_credits(self):
        return self.__credits
    def student_info(self):
        return self.__nom, self.__prenom,self.__numero_d_etudiant,self.__eval
    def student_eval(self):
        if self.__credits < 60:
            return 'insuffisant'
        if 60 <= self.__credits < 70:
            return 'passable'
        if 70 <= self.__credits < 80:
            return 'bien'
        if 80 <= self.__credits < 90:
            return 'très bien'
        if self.__credits >= 90:
            return 'excellent'

john = Student('Doe','John',145)
john.add_credits(10)
john.add_credits(10)
john.add_credits(10)
print(f"Le nombre de crédits de {john.get_student_name()} est de {john.get_credits()} crédits")
print(john.student_info())
john.add_credits(70)
print(john.student_info())
john.add_credits(10)
print(john.student_info())