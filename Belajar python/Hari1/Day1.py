class Mahasiswa:
    def __init__(self, Nama, nilaiUcp):
        self.nama = Nama
        self.nilaiUcp = nilaiUcp
    

    def kelulusan (self):
        if self.nilaiUcp >= 80:
            print("SELAMT ANDA LULUS")
        else:
            print("Anda tidak lulus ")    

m1 = Mahasiswa ("azkal", 90);

print(m1.nama)
print(m1.nilaiUcp)
print(m1.kelulusan())