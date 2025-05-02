# Inheritance = allows a class to inherit the attributes and methods from another class
# helps with code reusability and extensibility
# class Child(Parent) or Sub(Super)

class Animal:

    def __init__(self, name):
        self.name = name
        self.is_alive = True

    def eat(self):
        print(f"{self.name} is eating")

    def sleep(self):
        print(f"{self.name} is sleeping")

class Dog(Animal):
    def speak(self):
        print(f"{self.name} says WOOF")

class Cat(Animal):
    def speak(self):
        print(f"{self.name} says MEOW")

class Mouse(Animal):
    def speak(self):    
        print(f"{self.name} says SQUEEK")

dog = Dog("Scooby")
dog.eat()
dog.speak()