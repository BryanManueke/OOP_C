# Single inheritance - Defining parent class
class Parent():
    # Constructor
    def __init__(self):
        self.value = "Inside Parent"

    # Parent's show method
    def show(self):
        print(self.value)

# Defining child class
class Child(Parent):
    # Constructor
    def __init__(self):
        self.value = "Inside Child"

    # Child's show method
    def show(self):
        print(self.value)

# create objects of the class
obj1 = Parent()
obj2 = Child()

obj1.show()
obj2.show()



# Multiple inheritance - Defining parent class 1
class Parent1():
    # Parent's show method
    def show(self):
        print("Inside Parent1")

# Defining Parent class 2
class Parent2():
    # Parent's show method
    def display(self):
        print("Inside Parent2")

# Defining child class
class Child(Parent1, Parent2):
    # Child's show method
    def show(self):
        print("Inside Child")

# create objects of the class
obj = Child()

obj.show()
obj.display()



# Multilevel inheritance - Defining parent class
class Parent():
    # Parent's show method
    def display(self):
        print("Inside Parent")

# Inherited or Sub class
class Child(Parent):
    # Child's show method
    def show(self):
        print("Inside Child")

# Inherited or Sub class
class GrandChild(Child):
    # GrandChild's show method
    def show(self):
        print("Inside GrandChild")

# Create objects of the class
g = GrandChild()
g.show()
g.display()


