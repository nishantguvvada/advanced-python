# Duck typing is another way to achieve polymorphism besides inheritance
# Objects must have minimum necesssary attributes/methods
# If it looks like a duck and quacks like a duck, it must be a duck

class Animal:
    is_alive = True

class Dog(Animal):
    def speak(self):
        print("WOOF")

class Cat(Animal):
    def speak(self):
        print("MEOW")

class Car:
    def speak(self): # Car object has minimum necessary attribute/method (speak) to be Animal
        print("VROOM")

animals = [Dog(), Cat(), Car()]
for animal in animals:
    animal.speak()