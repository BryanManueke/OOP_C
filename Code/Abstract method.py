# import module
from abc import ABC, abstractclassmethod

# abstract class
class Absclass(ABC):
    # normal method
    def print(self, X):
        print("Passed value:", X)

@abstractclassmethod
def task(self):
    print("Ada di dalam structure test_class. ")

class test_class(Absclass): # normal class
    def task(self):
        print("Ada di dalam structure test_class. ")

class example_class(Absclass):
    def task(self):
        print("Ada di dalam structure example_class. ")

# object of test_class created
test_obj = test_class()
test_obj.task()                     # abstact method
test_obj.print(100)                 # normal method

# obeject of example_class created
example_obj = test_class()          
example_obj.task()                  # abstract method
example_obj.print(200)              # normal method

print("test_obj is instance of Absclass?", isinstance(test_obj, Absclass))
print("example is instance of Absclass?", isinstance(example_obj, Absclass))
