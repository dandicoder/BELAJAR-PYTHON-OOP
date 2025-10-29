class Hero:

    # private variabel
    __jumlah = 0

    def __init__(self, name, health, atttackPower, armor):
        self.__name = name
        self.__healthStandar = health
        self.__attStandar = atttackPower
        self.__armorStandar = armor

        self.__level = 1
        self.__exp = 0

        self.__healthMax = self.__healthStandar * self.__level
        self.__attMax = self.__attStandar * self.__level
        self.__armorMax = self.__armorStandar * self.__level

        Hero.__jumlah += 1

    @property
    def info(self):
        return "Nama : {} level {}\n\tHealth : {}\n\tAttack : {}\n\tArmor : {}".format(self.__name,self.__level, self.__healthMax, self.__attMax, self.__armorMax)
    
    @property
    def gainExp(self):
        pass

    @gainExp.setter
    def gainExp(self, exp):
        self.__exp += exp
        if self.__exp >= 100:
            print("Level Up +++")
            self.__level += 1
            self.__exp -= 100

            self.__healthMax = self.__healthStandar * self.__level
            self.__attMax = self.__attStandar * self.__level
            self.__armorMax = self.__armorStandar * self.__level
    
    def attack(self, lawan):
        print(f"{self.__name} menyerang {lawan.__name}")
        self.gainExp = 50

lancelot = Hero("Lancelot", 100, 40, 5)
helcut = Hero("Helcut", 100, 40, 5)

print(lancelot.info)
lancelot.attack(helcut)
lancelot.attack(helcut)
print(lancelot.info)