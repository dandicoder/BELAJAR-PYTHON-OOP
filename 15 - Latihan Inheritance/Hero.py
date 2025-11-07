class Hero:
    def __init__(self, name):
        self.__name = name
        self.__healthPoor = [0,100,200,300,400,500]
        self.__attackPowerPoor = [0,10,20,30,40,50]
        self.__armorPoor = [0,1,2,3,4,5,6,7,8,9,10]

        self.__exp = 0
        self.__level = 0
        
    def show_info(self):
        print("{} \n\tLevel : {} \n\tHealt : {} \n\tDemage : {} \n\tArmor : {}".format(
                self.__name,
                self.__level,
                self.__health,
                self.__attackPower,
                self.__armor,
            )
        )

    @property
    def healthPoor(self):
        pass

    @property
    def attackPowerPoor(self):
        pass
    
    @property
    def armorPoor(self):
        pass

    @property
    def levelUp(self):
        pass

    @property
    def gainExp(self):
        pass

    @healthPoor.setter
    def healthPoor(self, input):
        self.__healthPoor = input

    @attackPowerPoor.setter
    def attackPowerPoor(self, input):
        self.__attackPowerPoor = input

    @armorPoor.setter
    def armorPoor(self, input):
        self.__armorPoor = input

    @gainExp.setter
    def gainExp(self, input):
        self.__exp += input
        if(self.__exp >= 100):
            self.levelUp = self.__exp // 100 
            self.__exp %= 100
    
    @levelUp.setter
    def levelUp(self, input):
        self.__level += input
        self.__health = self.__healthPoor[self.__level]
        self.__attackPower = self.__attackPowerPoor[self.__level]
        self.__armor = self.__armorPoor[self.__level]
            

class HeroInteligent(Hero):
    def __init__(self, name):
        super().__init__(name)
        self.healthPoor = [0,50,150,200,250,300]
        self.armorPoor = [0,1.5,2,2.5]
        self.attackPowerPoor = [0,5,10,20,25,30]
        self.levelUp = 1

class HeroStrenght(Hero):
    def __init__(self, name):
        super().__init__(name)
        self.healthPoor = [0,10,200,300,400,500]
        self.armorPoor = [0,2,4,8, 10]
        self.attackPowerPoor = [0,10,20,30,40,50]
        self.levelUp = 1