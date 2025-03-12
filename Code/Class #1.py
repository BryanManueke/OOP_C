
# Membuat Class Vehicle
class Vehicle:
    def __init__(self, max_speed, gears):
        self.max_speed = max_speed  # Kecepatan maksimum kendaraan
        self.gears = gears  # Jumlah gigi kendaraan
    
    def speed(self):  # Method untuk mengembalikan informasi kecepatan maksimum kendaraan
        return f"Max speed: {self.max_speed} km/h"
    
    def change_gear(self):   # Method untuk mengembalikan jumlah gigi kendaraan
        return f"Number of gears: {self.gears}"
    
    def show(self):  # Method untuk menampilkan informasi umum kendaraan (bisa dioverride oleh subclass)
        return "Display Vehicle"

# Kelas Car sebagai turunan dari Vehicle
class Car(Vehicle):
    def __init__(self):
        super().__init__(max_speed=240, gears=6)  # Nilai khusus untuk mobil

    def show(self):  # Override method show()
        return "Display Car"

# Kelas Truck sebagai turunan dari Vehicle
class Truck(Vehicle):
    def __init__(self):
        super().__init__(max_speed=200, gears=8)  # Nilai khusus untuk truk

    def show(self):  # Override method show()
        return "Display Truck"

# Membuat objek dari masing-masing kelas
vehicle = Vehicle(max_speed=150, gears=5)
car = Car()
truck = Truck()

# Menampilkan informasi dari objek Vehicle
print(vehicle.show())  
print(vehicle.speed())  
print(vehicle.change_gear())  

# Menampilkan informasi dari objek Car
print(car.show())  
print(car.speed())  
print(car.change_gear())  

# Menampilkan informasi dari objek Truck
print(truck.show())  
print(truck.speed())  
print(truck.change_gear())  
