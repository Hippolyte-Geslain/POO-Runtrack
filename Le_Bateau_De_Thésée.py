class Part():
    def __init__(self,name,material):
        self.name = name
        self.material = material
    def change_material(self,new_material):
        self.material = new_material
    def __str__(self):
        return f"La pièce {self.name} est faite de {self.material}"

mat = Part('mat','bouleau')
voile = Part('voile','chambre')
coque = Part('coque','chene')

class Ship():
    def __init__(self,name):
        self.name = name
        self.__parts = {
            'mat': mat,
            'voile': voile,
            'coque': coque
        }
    def display_state(self):
        print(f"La liste des pièces du bateau '{self.name}' :\n")
        for name, part in self.__parts.items():
            print(f"La pièce : {name} est faite de : {part.material}")
        print()
    def replace_part(self,part_name,new_part):
        if part_name in self.__parts:
            self.__parts[new_part] = self.__parts.pop(part_name)
        return self.display_state()
    def replace_material(self,part_name,part_material):
        if part_name in self.__parts:
            self.__parts[part_name].change_material(part_material)
        return self.display_state()
thesee = Ship('La pourfendeuse')
thesee.display_state()
thesee.replace_part('mat','mat2')
thesee.replace_material('mat2','plastique')


class RacingShip(Ship):
    def __init__(self):
        super().__init__()
        self.__max_speed = 12
    def display_speed(self):
        return self.__max_speed