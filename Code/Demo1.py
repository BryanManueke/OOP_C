class Cat:
    # Constractor (Intialize Instance Variables)
    def __init__(self, nama, umur):
        self.nama = nama
        self.umur = umur

    def speak(self):
        print("Cat speaks Meow Meow")

# Crate class 2
class Dog:
    # Constractor (Intialize Instance variable)
    def __init__(self, nama, umur):
        self.nama = nama
        self.umur = umur

    def speak(self):
        print("Dog speaks Guk Guk Guk")

#  Object class for create
kucing1 = Cat("Catty", 5)
# Object of dog crate
anjing1 = Dog("Doggy", 4)


kucing1.speak()
anjing1.speak()

for hewan in (kucing1, anjing1):
    hewan.speak()
