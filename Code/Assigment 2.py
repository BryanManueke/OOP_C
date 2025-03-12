from abc import ABC, abstractmethod

# Kelas Abstrak Kendaraan
class Kendaraan(ABC):

    @abstractmethod
    def jumlah_roda(self):
        pass

    @abstractmethod
    def bahan_bakar(self):
        pass

# Kelas Motor (Turunan dari Kendaraan)
class Motor(Kendaraan):
    def jumlah_roda(self):
        return 2

    def bahan_bakar(self):
        return "Bensin"

# Kelas Mobil (Turunan dari Kendaraan)
class Mobil(Kendaraan):
    def jumlah_roda(self):
        return 4

    def bahan_bakar(self):
        return "Solar"

# Program Utama
def main():
    # Membuat objek dari Motor dan Mobil
    motor = Motor()
    mobil = Mobil()

    # Memanggil method dan menampilkan hasil
    print("Informasi Kendaraan:")
    print(f"Motor memiliki {motor.jumlah_roda()} roda dan menggunakan bahan bakar {motor.bahan_bakar()}.")
    print(f"Mobil memiliki {mobil.jumlah_roda()} roda dan menggunakan bahan bakar {mobil.bahan_bakar()}.")

# Menjalankan program utama
if __name__ == "__main__":
    main()



# Membuat kelas induk Hewan
class Hewan:
    def suara(self):
        pass  # Akan di-override oleh turunan

# Membuat turunan Kucing
class Kucing(Hewan):
    def suara(self):
        return "Meong"

# Membuat turunan Anjing
class Anjing(Hewan):
    def suara(self):
        return "Guk guk"

# Membuat turunan Ayam
class Ayam(Hewan):
    def suara(self):
        return "Kukuruyuk"

# Fungsi untuk memanggil suara hewan
def bunyi_hewan(hewan):
    print(hewan.suara())

# Program utama
kucing = Kucing()
anjing = Anjing()
ayam = Ayam()

bunyi_hewan(kucing)  # Output: Meong
bunyi_hewan(anjing)  # Output: Guk guk
bunyi_hewan(ayam)    # Output: Kukuruyuk


class BankAccount:
    def __init__(self, saldo_awal):
        self.__saldo = saldo_awal  # Atribut saldo bersifat privat

    def deposit(self, jumlah):
        if jumlah > 0:
            self.__saldo += jumlah
            print(f"Deposit sebesar Rp {jumlah} berhasil.")
        else:
            print("Jumlah deposit harus lebih dari 0.")

    def withdraw(self, jumlah):
        if jumlah > self.__saldo:
            print("Penarikan gagal. Saldo tidak mencukupi.")
        elif jumlah > 0:
            self.__saldo -= jumlah
            print(f"Penarikan sebesar Rp {jumlah} berhasil.")
        else:
            print("Jumlah penarikan harus lebih dari 0.")

    def tampilkan_saldo(self):
        print(f"Saldo saat ini: Rp {self.__saldo}")

# Program utama
akun = BankAccount(1000000)  # Saldo awal Rp 1.000.000
akun.tampilkan_saldo()

akun.deposit(500000)  # Deposit Rp 500.000
akun.tampilkan_saldo()

akun.withdraw(2000000)  # Gagal tarik Rp 2.000.000 (saldo kurang)
akun.tampilkan_saldo()

akun.withdraw(700000)  # Berhasil tarik Rp 700.000
akun.tampilkan_saldo()

class BankAccount:
    def __init__(self, saldo_awal):
        if saldo_awal < 0:
            print("Saldo awal tidak boleh negatif. Saldo diatur ke 0.")
            self.__saldo = 0
        else:
            self.__saldo = saldo_awal

    def deposit(self, jumlah):
        if jumlah > 0:
            self.__saldo += jumlah
            print(f"Deposit sebesar Rp {jumlah} berhasil.")
        else:
            print("Jumlah deposit harus lebih dari 0.")

    def withdraw(self, jumlah):
        if jumlah > self.__saldo:
            print("Penarikan gagal. Saldo tidak mencukupi.")
        elif jumlah > 0:
            self.__saldo -= jumlah
            print(f"Penarikan sebesar Rp {jumlah} berhasil.")
        else:
            print("Jumlah penarikan harus lebih dari 0.")

    def tampilkan_saldo(self):
        print(f"Saldo saat ini: Rp {self.__saldo}")

# Program utama
saldo_awal = float(input("Masukkan saldo awal Anda: Rp "))
akun = BankAccount(saldo_awal)

while True:
    print("\nMenu Bank:")
    print("1. Cek Saldo")
    print("2. Deposit")
    print("3. Tarik Tunai")
    print("4. Keluar")

    pilihan = input("Pilih menu (1/2/3/4): ")

    if pilihan == "1":
        akun.tampilkan_saldo()
    elif pilihan == "2":
        jumlah = float(input("Masukkan jumlah deposit: Rp "))
        akun.deposit(jumlah)
    elif pilihan == "3":
        jumlah = float(input("Masukkan jumlah penarikan: Rp "))
        akun.withdraw(jumlah)
    elif pilihan == "4":
        print("Terima kasih telah menggunakan layanan kami.")
        break
    else:
        print("Pilihan tidak valid. Silakan coba lagi.")

# Membuat class hewan
class Hewan:
    def __init__(self, nama):
        self.nama = nama

    def bersuara(self):
        return "Suara hewan umum"

class Kucing(Hewan):
    def bersuara(self):
        return "Meong"
    

# Membuat objek Kucing dengan nama "Kitty"
kitty = Kucing("Kitty")

# Memanggil method bersuara() dari objek tersebut dan menampilkan hasilnya
print(f"{kitty.nama} bersuara: {kitty.bersuara()}")


# Membuat class Mamalia
class Mamalia:
    def melahirkan(self):
        return "Mamalia melahirkan anaknya."

class HewanAir:
    def berenang(self):
        return "Hewan ini bisa berenang."

class LumbaLumba(Mamalia, HewanAir):
    pass  # Tidak menambahkan method baru

# Membuat objek LumbaLumba
lumba_lumba = LumbaLumba()

# Memanggil method melahirkan() dan berenang() dari objek tersebut
print("Lumba-lumba:", lumba_lumba.melahirkan())
print("Lumba-lumba:", lumba_lumba.berenang())


