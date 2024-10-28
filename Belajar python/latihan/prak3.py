class Persegi_Panjang:
    def __init__(self, panjang, lebar):
        self.panjang = panjang
        self.lebar = lebar

    def hitung_keliling(self):
        return 2 * (self.panjang + self.lebar)

    def hitung_luas(self):
        return self.panjang * self.lebar

    def __str__(self):
        return f"Persegi Panjang, Panjang {self.panjang} cm, dan Lebar {self.lebar} cm"


pp = Persegi_Panjang(5, 2)
print(pp)
print("Keliling:", pp.hitung_keliling()) 
print("Luas:", pp.hitung_luas())          
