# Super() is a function used in the child class to call the methods of the parent class
# It allows to extend or modify the functionality of the inherited methods from the parent class

# Example

class Shape:

    def __init__(self, color, filled):
        self.color = color
        self.filled = filled

    def describe(self):
        print(f"It is a shape with color {self.color} and is {self.filled}")

class Circle(Shape):

    def __init__(self, color, filled, radius):
        super().__init__(color, filled)
        self.radius = radius

    def describe(self): # overrides the same name method in the parent class
        super().describe()
        print(f"It is a shape with area {3.14 * self.radius} cm squared")

class Square(Shape):

    def __init__(self, color, filled, side):
        super().__init__(color, filled)
        self.side = side

    def describe(self): # overrides the same name method in the parent class
        super().describe()
        print(f"It is a shape with area {self.side * self.side} cm squared")

class Rectangle(Shape):

    def __init__(self, color, filled, length, breadth):
        super().__init__(color, filled)
        self.length = length
        self.breadth = breadth

    def describe(self): # overrides the same name method in the parent class
        super().describe()
        print(f"It is a shape with area {self.length * self.breadth} cm squared")


circle = Circle("red", True, 3)
square = Square("blue", False, 5)
rectangle = Rectangle("yellow", True, 4, 6)

circle.describe()
square.describe()
rectangle.describe()