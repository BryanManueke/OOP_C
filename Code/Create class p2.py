class Produk():
    # variable
    Jumlah_produk = 0

    # Method constructor (default method)
    def __init__ (self, nama, harga):
        self.nama = nama;
        self.harga = harga;

    # Method #1
    def view_jum_produk(self, jumlah):
        Produk.Jumlah_produk = jumlah;
        print('Total Produk: ', Produk.Jumlah_produk);

    # Method #2
    def detail_produk(self):
        print("Nama : ", self.nama);
        print("Harga : ", self.harga);

# Membuat objek pertama (object Instantiantion)
produk1 = Produk('kripik', 5000)

# Membuat objek Kedua (object Instantiantion)
produk2 = Produk('Taro',  3000)

# Membuat objek Ketiga (object Instantiantion)
produk3 = Produk('Astor', 4000)

# Mengakses atribut objek (Accessing class attributes)
produk1.detail_produk()
produk1.view_jum_produk(5)
print("Jumlah produk adalah {}".format(produk1.__class__.Jumlah_produk));
print("Nama produk adalah {}".format(produk1.nama))
print()

produk2.detail_produk()
produk2.view_jum_produk(10)
print("Jumlah produk adalah {}".format(produk2.__class__.Jumlah_produk));
print("Nama produk adalah {}".format(produk2.nama))
print()

produk3.detail_produk()
produk3.view_jum_produk(15)
print("Jumlah produk adalah {}".format(produk3.__class__.Jumlah_produk));
print("Nama produk adalah {}".format(produk3.nama))
print()





class name():
    def __init__(self):
        print("Bryan Manueke")

    def detail_product(self):
        print("Method Product")

main = name()
main.detail_product()

    