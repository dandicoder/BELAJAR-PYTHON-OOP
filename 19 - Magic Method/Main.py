class Buah:

    # megic method
    def __init__(self, nama, jumlah):
        self.nama = nama
        self.jumlah = jumlah

    def __repr__(self): #biasa digunakan untuk debugging
        return "Debugging - Buah {} dengan Jumlah {}".format(self.nama, self.jumlah)

    def __str__(self):
        return "Buah {} dengan Jumlah {}".format(self.nama, self.jumlah)        
    
    def __add__(self, buah):
        return self.jumlah + buah.jumlah

    @property    
    def __dict__(self):
        return "ini adalah Buah dan Jumlah"
    
mangga = Buah("mangga", 10)
pisang = Buah("pisang", 20)

print(mangga)
print(repr(pisang))

print(mangga + pisang)

print(mangga.__dict__)