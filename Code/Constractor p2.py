class Mobil:
    def __init__(self, nama_mobil, kecepatan):
        self.nama_mobil = nama_mobil
        self.kecepatan = kecepatan

    def print_nama_mobil(self):
        print("Nama mobil:", self.nama_mobil)
        print("Kecepatan:", self.kecepatan)

ferari = Mobil("Ferari", "150 km/jam")
ferari.print_nama_mobil()

bmw = Mobil("BMW", "100 km/jam")
bmw.print_nama_mobil()

class Main:
    def __init__(self, angka1, angka2):
        self.angka1 = angka1
        self.angka2 = angka2
        print("Ini method constructor")

    def penjumlahan(self):
        result = self.angka1 + self.angka2
        print("Hasil penjumlahan:", result)

main = Main(10, 2)
main.penjumlahan()



# objek lain
class HP:

    def __init__(self, nama):
        self.nama = nama

    def get_nama(self):
        print("Nama HP:", self.nama)

Iphone = HP("Iphone")
Iphone.get_nama()

Samsung = HP("Samsung")
Samsung.get_nama()

Xiaomi = HP("Xiaomi")
Xiaomi.get_nama()

Infinix = HP("Infinix")
Infinix.get_nama()


# Objek lain
class mahasiswa:
    def __init__(self, nama, nim):
        self.nama = nama
        self.nim = nim

    def show(self):
        print(f"nama : {self.nama}")
        print(f"nim : {self.nim}")

# Pembuatan objek di luar kelas
mhs1 = mahasiswa("Bryan Manueke", "10502221")
mhs2 = mahasiswa("Venalveol Manampiring", "105022310043")

# Memanggil method
mhs1.show()
mhs2.show()
