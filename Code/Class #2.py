
# Membuat Class Employee 
class Employee:
    def __init__(self, name, age):
        # Atribut nama dan umur
        self.name = name
        self.age = age

    def show(self):
        # Method untuk menampilkan informasi Employee
        return f"Name: {self.name}, Age: {self.age}"


# Kelas PermanentEmployee 
class PermanentEmployee(Employee):
    def __init__(self, name, age, salary):
        # Memanggil constructor kelas induk
        super().__init__(name, age)
        # Menambahkan atribut salary khusus untuk karyawan tetap
        self.salary = salary

    def show(self):
        # Menampilkan informasi Employee dan salary
        return super().show() + f", Salary: Rp. {self.salary}"


# Kelas ContractEmployee yang mewarisi Employee
class ContractEmployee(Employee):
    def __init__(self, name, age, hourly_pay):
        # Memanggil constructor kelas induk
        super().__init__(name, age)
        # Menambahkan atribut hourly_pay khusus untuk karyawan kontrak
        self.hourly_pay = hourly_pay

    def show(self):
        # Menampilkan informasi Employee dan hourly pay
        return super().show() + f", Hourly Pay: Rp. {self.hourly_pay}"


# Membuat objek dari masing-masing kelas
manager = Employee("Semmy Taju", 30)  # Objek dari kelas Employee
developer = PermanentEmployee("Edwin Padu", 26, 3000)  # Objek dari kelas PermanentEmployee
freelancer = ContractEmployee("Reza Haeres", 35, 5000)  # Objek dari kelas ContractEmployee

# Menampilkan informasi masing-masing objek
print(manager.show())     # Menampilkan data Employee
print(developer.show())   # Menampilkan data PermanentEmployee
print(freelancer.show())  # Menampilkan data ContractEmployee
