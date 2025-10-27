class Hero:
    # varibel static/ class

    def __init__(self, inputName, inputHealth, inputAttack, inputArmor):
        self.name = inputName
        self.health = inputHealth
        self.attack =- inputAttack
        self.armor = inputArmor

    # void function, function tanpa return
    def siapa(self):
        print(f"Hero ini adalah {self.name}")

    # method dengan argument
    def healthUp(self, up):
        self.health += up

    # method dengan return
    def getHealt(self):
        return self.health

hero1 = Hero("Fanny", 100, 240, 210)
hero2 = Hero("Lancelot", 100, 220, 270)


hero1.siapa()
hero1.healthUp(10)

print(hero1.getHealt())