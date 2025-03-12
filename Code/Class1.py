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

# objek lain
class Animal:
    color = "Black"
    species = "Dog"

    def __init__(self, species, color):
        self.species = species
        self.color = color

    def func(self):
        print("After calling func() method..")
        print("Species type is", self.species)
        print("Its color is", self.color)

obj_cat = Animal('Cat', 'White')
obj_dong = Animal('Dog', 'Black')
obj_bird = Animal('Bird', 'Red')

print("/Direct access of attributes using object..")
print(obj_cat.species)
print(obj_dong.species)
print(obj_bird.species)
