# List kosong
my_list = []

# List dengan elemen
numbers = [1, 2, 3, 4, 5]
mixed = [1, "Python", 3.14, True]

# List bersarang (nested list)
nested_list = [[1, 2, 3], [4, 5, 6]]

# Akses Elemen (Indexing)
print(numbers[0])  # Output: 1
print(numbers[-1]) # Output: 5

# Slicing (Mengambil sebagian elemen)
print(numbers[1:4])  # Output: [2, 3, 4]

# Menambahkan Elemen
numbers.append(6)      # Menambahkan di akhir
numbers.insert(2, 10)  # Menyisipkan di indeks tertentu

# Menghapus Elemen
numbers.remove(10)  # Menghapus berdasarkan nilai
del numbers[0]      # Menghapus berdasarkan indeks
numbers.pop()       # Menghapus elemen terakhir

# Mengurutkan List
numbers.sort()      # Ascending
numbers.reverse()   # Membalikkan urutan

# List Comprehension
squares = [x**2 for x in range(1, 6)]
print(squares)  # Output: [1, 4, 9, 16, 25]