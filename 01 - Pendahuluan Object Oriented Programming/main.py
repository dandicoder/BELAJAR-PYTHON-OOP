class Hero:
    pass


hero1 = Hero()

hero1.name = "Dandi"
hero1.health = 1500
hero1.attack = 2000

print(hero1.name)
print(hero1.health)
print(hero1.attack)

print(hero1.__dict__)