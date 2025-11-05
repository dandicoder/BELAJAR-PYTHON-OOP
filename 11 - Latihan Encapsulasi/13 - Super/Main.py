class Hero:
    def __init__(self, name, health):
        self.name = name
        self.health = health

    def showInfo(self):
        print("{} dengan darah sebanyak {}".format(self.name, self.health))

class Hero_inteligent(Hero):
    def __init__(self, name):
        # Hero.__init__(self, name, 100)
        super().__init__(name, 100)
        super().showInfo()

class Hero_strenght(Hero):
    def __init__(self, name):
        super().__init__(name, 200)
        super().showInfo()


lancelot = Hero_inteligent("Lancelot")
alucard = Hero_strenght("Alucard")