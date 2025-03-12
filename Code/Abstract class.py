from abc import ABC, abstractmethodfrom abc import ABC, abstractmethod
from math import pi

class BangunDatar(ABC):
    @abstractmethod
    def luas(self):
        pass

    @abstractmethod
    def keliling(self):
        pass

class Persegi(BangunDatar):
    def __init__(self, sisi):
        if sisi <= 0:
            raise ValueError("Sisi harus lebih besar dari 0")
        self.sisi = sisi

    def luas(self):
        return self.sisi ** 2

    def keliling(self):
        return 4 * self.sisi


class Lingkaran(BangunDatar):
    def __init__(self, jari_jari):
        if jari_jari <= 0:
            raise ValueError("Jari-jari harus lebih besar dari 0")
        self.jari_jari = jari_jari

    def luas(self):
        return pi * (self.jari_jari ** 2)

    def keliling(self):
        return 2 * pi * self.jari_jari


def main():
    p = Persegi(5)
    k = Lingkaran(5)

    print("Luas Persegi :", p.luas())
    print("Keliling Persegi :", p.keliling())
    print("Luas Lingkaran :", k.luas())
    print("Keliling Lingkaran :", k.keliling())


if __name__ == "__main__":
    main()

class BangunDatar(ABC):
    @abstractmethod
    def luas(self):
        pass

    @abstractmethod
    def keliling(self):
        pass

class Persegi(BangunDatar):
    def __init__(self, sisi):
        self.sisi = sisi

    def luas(self):
        return self.sisi * self.sisi

    def keliling(self):
        return 4 * self.sisi


class Lingkaran(BangunDatar):
    def __init__(self, jari_jari):
        self.jari_jari = jari_jari

    def luas(self):
        return 3.14 * (self.jari_jari ** 2)

    def keliling(self):
        return 2 * 3.14 * self.jari_jari
1
p = Persegi(5)
k = Lingkaran(5)

print("Luas Persegi :", p.luas())
print("Keliling Persegi :", p.keliling())
print("Luas Lingkaran :", k.luas())
print("Keliling Lingkaran :", k.keliling())
