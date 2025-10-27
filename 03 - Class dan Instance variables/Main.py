class Hero:
    # class variabel/ static variabel
    jumlah = 0

    def __init__(self, inputName, inputHealt, inputAttack): # self = hero1
        # variabel instaance
        self.name = inputName
        self.healt = inputHealt
        self.attack = inputAttack
        Hero.jumlah += 1
        print(f"Nomor {Hero.jumlah} adalah {inputName} ")


# sayHello = Hero("Selamat Datang", " Dandi")
hero1 = Hero("Naruto", 2300, 5000)
hero2 = Hero("Sasuke", 3300, 4800)

print(Hero.__dict__)

