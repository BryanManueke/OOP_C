# Kelas Induk (Super Class)
class Hewan:
    def bersuara(self):
        print("Hewan bisa bersuara.")

# Kelas Anak (Sub Class) yang mewarisi dari Hewan
class Kucing(Hewan):
    def suara_khas(self):
        print("Meong... Meong...")

# Membuat objek kucing
kucing = Kucing()
kucing.bersuara()     # Warisan dari kelas Hewan
kucing.suara_khas()   # Fitur khusus dari Kucing



# Kelas Induk 1 (Ayah)
class Ayah:
    def sifat_ayah(self):
        print("Saya tegas dan disiplin.")
+6
# Kelas Induk 2 (Ibu)
class Ibu:
    def sifat_ibu(self):
        print("Saya penyayang dan sabar.")

# Kelas Anak yang mewarisi dari Ayah dan Ibu
class Anak(Ayah, Ibu):
    def sifat_anak(self):
        print("Saya adalah kombinasi dari kedua orang tua saya.")

# Membuat objek anak
anak = Anak()
anak.sifat_ayah()  # Dari kelas Ayah
anak.sifat_ibu()   # Dari kelas Ibu
anak.sifat_anak()  # Dari kelas Anak