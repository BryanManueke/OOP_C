class student:
    def __init__(self, nama):
        print('Inside Constructor')
        self.nama = nama
        print("ALL variables initialized")
    
    def __del__(self):
        print('Inside destructor')
        print('Object destroyed')

    def show(self):
        print('Hello, my name is', self.nama)

s1 = student('Bryan Miracles Manueke')
s2 = student('Starlie Dorangie')
s3 = student('Relandy Liwe')

s1.show()
s2.show()
