# @property decorator allows to define a method as a property i.e. attribute
# allows to add additional logic when reading, writing and deleting attributes
# Be sure to give the additional functions (setter and deleter) the same name as the original attribute name
# If an object defines __set__() or __delete__(), it is considered a data descriptor, @property is a succinct way of building a data descriptor

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

# EXTRA: HOW TO HIDE CLASS OR INSTANCE VARIABLES

# 1. Prefix with _ or __

class MyClass:

    def __init__(self):
        self._semi_private = "Not recommended to access"
        self.__private = "Name mangled"

    __class_var = "Hidden class var"

obj = MyClass()
print(obj._semi_private) # No error, by convention don't use
# print(obj.__private) # AttributeError: 'MyClass' object has no attribute '__private'.
print(obj._MyClass__private)
print(MyClass._MyClass__class_var)

# Double underscore (__var) triggers name mangling in Python
# Python internally renames __var to _ClassName__var to avoid accidental access or override, especially in subclasses.


# 2. Use properties for controlled access

class ControlledAccess:

    def __init__(self):
        self._private = "Private"

    @property
    def private(self): # using @property to restrict access
        print(f"Access to private variable is restricted")

    @private.setter
    def private(self, value: str):
        self._private = value
        print(f"Private variable set to: {self._private}")

obj = ControlledAccess()
print(obj._private)
obj.private # Output: Access to private variable is restricted
obj.private = "Modified Private"