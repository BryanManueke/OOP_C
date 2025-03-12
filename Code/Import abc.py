#import abc module
from abc import ABC

class type_shape(ABC): # abstract class
    def area(self):
        # abstract method
        pass

class Rectangle(type_shape):
    length = 6
    breadth = 4
    def area(self):
        return self.length * self.breadth
    
class Circle(type_shape): # normal class
    radius = 7
    def area(self):
        return 3.14 * self.radius *self.radius
    
class Square(type_shape): # normal class
    length = 4
    def area(self):
        return self.length*self.length
    
class triangle: # normal class
    length = 5
    width = 4
    def area(self):
        return 0.5 * self.length * self.width

r = Rectangle() # object created for the class 'rectangle'
c = Circle() # object created for the class 'Circel'
s = Square() # obejct created for the class 'Square'
t = triangle() # object created for the class 'triangle'
print("Area of a rectangle:", r.area()) # call to 'area' method defind inside the class
print("Area of a circle:", c.area()) 
print("Area of a square:", c.area()) 
print("Area of a triangle:", t.area())
