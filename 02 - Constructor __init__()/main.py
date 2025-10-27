class Hero:
    def __init__(self, inputName, inputHealt, inputAttack): # self = hero1
        self.name = inputName
        self.healt = inputHealt
        self.attack = inputAttack
        


# sayHello = Hero("Selamat Datang", " Dandi")
hero1 = Hero("Naruto", 2300, 5000)
hero2 = Hero("Sasuke", 3300, 4800)

print(hero1.__dict__)
print(hero2.__dict__)
print(hero1.name)