class Hero:
    def __init__(self, name, healt, attack):
        self.name = name
        self.healt = healt
        self.attack = attack

class hero_warrior(Hero):
    pass


hero1 = Hero("naruto", 100, 200)
hero2 = hero_warrior("Dandi", 1500, 2000)

print(hero1.name)
print(hero1.healt)
print(hero1.attack)


print(hero2.name)
print(hero2.healt)
print(hero2.attack)

print(help(hero_warrior))