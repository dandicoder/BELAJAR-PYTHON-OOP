class Hero:

    def __init__(self, name, health, attackPower):
        self.__name = name
        self.__health = health
        self.__attPwr = attackPower

    # getter
    def getName(self):
        return self.__name
    
    # setter
    def setdiserang(self, demage):
        self.__health -= demage
        return self.__health
        

alucard = Hero("Alucard", 100, 34)

print(alucard.__dict__)

print(alucard.getName())

print(alucard.setdiserang(20))