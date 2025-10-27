class Hero:

    def __init__(self, name, health, armor):
        self.__name = name
        self.__health = health
        self.__armor = armor
        # self.info = "Nama : {}\n\tHealth : {}".format(self.__name, self.__health)

    def info(self):
        return "Nama : {}\n\tHealth : {}".format(self.__name, self.__health)
    
    @property
    def info(self):
        return  "Nama : {}\n\tHealth : {}".format(self.__name, self.__health) # menggunkan ini biar data bisa diubah realtime

    @property # menggunakan dummy property
    def armor():
        pass

    @armor.getter
    def armor(self):
        return self.__armor
    
    @armor.setter
    def armor(self, input):
         self.__armor = input

    @armor.deleter
    def armor(self):
        print("delete armor")
        self.__armor = None     

kagura = Hero("Kagura", 100, 30)
hayabusa = Hero("Hayabusa", 100, 60)
        

print(kagura.info) # menjadikan method menjadi object

print("\n getter dan setter")
print(kagura.armor)
kagura.armor = 109
print(kagura.armor)

del kagura.armor
print(kagura.__dict__)
print(hayabusa.__dict__)

