class Hero:
    jumlah = 0
    __jumlahPrivate = 0

    def __init__(self, name, health):
        self.name = name
        self.health = health

        # variabel private
        self.__private = "Private" # tidak bisa diubah dan digunakan diluar class

        # variabel protected
        self._protected = "Protected" # bisa diubah seperti vab public tapi diberi tanda


saitama = Hero("Saitama", 1000)
print(saitama.__dict__)
print(Hero.__dict__)