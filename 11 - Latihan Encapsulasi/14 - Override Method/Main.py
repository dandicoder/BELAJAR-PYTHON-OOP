class Hero:
    def __init__(self, name, health):
        self.name = name
        self.health = health

    def showInfo(self):
        print("showInfo dari super Class")
        print("nama hero {} \n\tHealth : {} \n\tTipe : Belum ditentukan \n".format(self.name, self.health))

class Hero_inteligent(Hero):
    def __init__(self, name):
        super().__init__(name, 100)

        # override
    def showInfo(self):
        print("showInfo dari super subClass")
        print("nama hero {} \n\tHealth : {} \n\tTipe : inteligent \n".format(self.name, self.health))

class Hero_strenght(Hero):
    def __init__(self, name):
        super().__init__(name, 350)
       

lancelot = Hero_inteligent("Lancelot")
alucard = Hero_strenght("Alucard")

lancelot.showInfo()
alucard.showInfo()