# @property decorator allows to define a method as a property i.e. attribute
# allows to add additional logic when reading, writing and deleting attributes
# Be sure to give the additional functions (setter and deleter) the same name as the original attribute name

class Rectangle:

    def __init__(self, width, height):
        self._width = width
        self._height = height

    @property
    def width(self): # width method is turned into an attribute i.e. width can be accessed via rectangle.width
        return f"You have accessed the width : {self._width:.1f} cm"
    
    @property
    def height(self):
        return f"You have accessed the height : {self._height:.1f} cm"
    
    @width.setter
    def width(self, new_width):
        if new_width > 0:
            self._width = new_width
        else:
            print("Width must be greater than 0")

    @height.setter
    def height(self, new_height):
        if new_height > 0:
            self._height = new_height
        else:
            print("Height must be greater than 0")

    @width.deleter
    def width(self):
        del self._width
        print("Width has been deleted.")

    @height.deleter
    def height(self):
        del self._height
        print("Height has been deleted.")

rectangle = Rectangle(3, 4)
rectangle.width = 15
print(rectangle.width)
print(rectangle.height)
del rectangle.width

# get, set and delete attributes using methods
