class Hero :

    # private variable class
    __jumlah = 0

    def __init__(self, name):
        self.__name = name
        Hero.__jumlah += 1

    def getName(self):
        return self.__name

    def getJumlah(self):
        return self.__jumlah
    
    # method ini hanya berlaku untuk object
    def getJumlah2(self):
        return Hero.__jumlah
    
    # method ini tidak berlaku untuk object 
    def getJumlah3():
        return Hero.__jumlah
    
    # method static (decorator) nempel ke object dan class
    @staticmethod
    def getJumlah4():
        return Hero.__jumlah
    
    @classmethod
    def getJumlah5(cls): # classmethod menggunakan argument
        return cls.__jumlah


naruto = Hero("naruto")
sasuke = Hero("sasuke")
sakura = Hero("sakura")

print(naruto.getName())

print(naruto.getJumlah2())

print(Hero.getJumlah3())

print(naruto.getJumlah4())

print(sakura.getJumlah5())