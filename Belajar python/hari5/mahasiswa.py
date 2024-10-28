class mahasiswa:
    def __init__(self, Nama, Nim):
        self.Nama = Nama
        self.Nim = Nim
        self.kehadiran = 0
        self.ucp = 0
        self.nilaiAkhir = 0
        self.luls_Tidak = ''



    def data_nilai(self):
        self.kehadiran = float(input("masukkan nilai kehadiran mahasiswa: "))
        self.ucp = float(input("masukkan nilai ucp mahasiswa: "))

    def proses_nilai(self):
        self.nilaiAkhir = (self.kehadiran * 0.4) + (self.ucp * 0.6)

    def kelulusan (self):   
        if self.nilaiAkhir >= 78:
            print("lulus")
        else:
            print("gagal")
        
    def display (self):
        print(f"Nama mahasiswa:{self.Nama}")
        print(f"Nilai ucp: {self.ucp}")
        print(f"Nail kehadiran: {self.kehadiran}")
        print(f"Nilai akhir:{self.nilaiAkhir}")
        print(f"Kamu dinyatakan:{self.luls_Tidak}")

def main():
    mahasiswa1 = mahasiswa("azkal", 20232)

    while True:
        print("\n===== Program Kasir =====")
        print("1. imput nilai")
        print("2. Tampilkan hasil ")
        print("3. Keluar")

        pilihan = input("Pilih menu (1/2/3): ")

        if pilihan == '1':
            mahasiswa1.data_nilai()
            mahasiswa1.proses_nilai()
            mahasiswa1.kelulusan()
        elif pilihan == '2':
            mahasiswa1.display()
        elif pilihan == '3':
            break
        else:
            print("Pilihan tidak valid. Silakan pilih 1, 2, atau 3.")

if __name__ == "__main__":                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                      
    main()



