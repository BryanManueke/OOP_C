class Mobil:
    def __init__(self, merk, tahun, harga_sewa, status):
        self.merk = merk
        self.tahun = tahun
        self.harga_sewa = harga_sewa
        self.status = status

    def info(self):
        print(f"Mobil {self.merk} tahun {self.tahun} dengan harga sewa per hari {self.harga_sewa}")

    def sewa(self):
        if self.status == "tersedia":
            self.status = "disewa"
            print("Mobil berhasil disewa!")
        else:
            print("Maaf, mobil tidak tersedia untuk disewa.")

    def kembali(self):
        if self.status == "disewa":
            self.status = "tersedia"
            print("Mobil telah dikembalikan.")
        else:
            print("Mobil belum disewa atau sudah dikembalikan!")


class MobilSUV(Mobil):
    def __init__(self, merk, tahun, harga_sewa, status, kapasitas):
        super().__init__(merk, tahun, harga_sewa, status)
        self.kapasitas = kapasitas

    def info(self):
        print(f"Mobil SUV {self.merk} tahun {self.tahun} dengan kapasitas {self.kapasitas} penumpang dan")
        print(f"harga sewa per hari {self.harga_sewa}")


class MobilPickup(Mobil):
    def __init__(self, merk, tahun, harga_sewa, status, kapasitas, muatan_maksimal):
        super().__init__(merk, tahun, harga_sewa, status)
        self.kapasitas = kapasitas
        self.muatan_maksimal = muatan_maksimal

    def info(self):
        print(f"Mobil pickup {self.merk} tahun {self.tahun} dengan kapasitas {self.kapasitas} penumpang dan")
        print(f"muatan maksimal {self.muatan_maksimal} kg, dan harga sewa per hari {self.harga_sewa}")


# Program Utama
mobil1 = Mobil("Honda Jazz", 2020, 300000, "tersedia")
mobil2 = MobilSUV("Toyota Fortuner", 2019, 500000, "tersedia", 7)
mobil3 = MobilPickup("Mitsubishi Triton", 2018, 700000, "tidak tersedia", 5, 1000)

mobil1.info()
mobil2.info()
mobil3.info()

mobil1.sewa()
mobil1.kembali()
mobil1.sewa()
mobil1.kembali()

mobil2.info()
mobil2.sewa()
mobil2.kembali()

mobil3.info()
mobil3.sewa()
mobil3.kembali()
mobil3.sewa()
