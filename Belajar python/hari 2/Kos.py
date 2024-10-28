class Kamar:
    def __init__(self,id_kamar,nomor_kamar,harga,status):
        self.id_kamar = id_kamar
        self.nomor_kamar = nomor_kamar
        self.harga = harga
        self.status = status

    def tampilkanInfo(self):
        print(f"ID kamar:{self.id_kamar}")
        print(f"Nomor kamar:{self.nomor_kamar}")
        print(f"Harga kamar:{self.harga}")
        print(f"Status kamar:{self.status}")
        
    def ubahStatus(self):
        pass



class Penyewa:
    def __init__(self,Nama,nomor_telpon):
        self.Nama = Nama
        self.nomor_telpon = nomor_telpon    

    def tampilkanInfo(self):
        pass



class pemilikKos:
    def __init__(self,nama,):
        pass

    def tambahKamar(self):
        pass

    def hapusKamar(self):
        pass



class laporan:
    def __init__(self) -> None:
        pass

    def generateLaporan(self):
        pass
