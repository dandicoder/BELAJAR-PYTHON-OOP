class Hero:

    def __init__(self, name, healt, attackPower, armorDefense):
        self.name = name
        self.healt = healt
        self.attack = attackPower
        self.armor = armorDefense

    def serang(self, lawan):
        print(f"{self.name} menyerang {lawan.name}")
        lawan.diserang(self)
        

    def diserang(self, lawan):
        print(f"{self.name} diserang {lawan.name}")
        demage = lawan.attack/self.armor
        print(f"Demage yang diterima {self.name} adalah {demage}")
        self.healt -= demage
        print(f"Darah {self.name} tersisa {self.healt}")


naruto = Hero("Naruto", 100, 35, 15)
sasuke = Hero("Sasuke", 100, 40, 10)
        
naruto.serang(sasuke)
print("\n")
sasuke.serang(naruto)