# Polymorphism is a greek word that means to have many forms
# Two ways to achieve polymorphism: Inheritance and Duck Typing

from abc import ABC, abstractmethod

class Shape(ABC):
    
    @abstractmethod
    def area(self):
        pass

class Circle(Shape): # a circle object is of type Circle and type Shape i.e. has many forms
    
    def __init__(self, radius):
        self.radius = radius

    def area(self):
        return f"{3.14 * self.radius ** 2} cmsq"

class Triangle(Shape): # a triangle object is of type Triangle and type Shape i.e. has many forms
    
    def __init__(self, side):
        self.side = side

    def area(self):
        return f"{0.5 * self.side ** 2} cmsq"

class Square(Shape): # a square object is of type Square and type Shape i.e. has many forms
    
    def __init__(self, side):
        self.side = side

    def area(self):
        return f"{self.side ** 2.0} cmsq"

shapes = [Circle(3), Triangle(4), Square(5)]

for shape in shapes:
    print(shape.area())

