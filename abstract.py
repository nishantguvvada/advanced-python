# Abstract class = A class that cannot be instantiated on it's own, it is meant to be subclassed
# It contains abstract methods that are declared but have no implementation
# Abstract class prevents instantiation of itself
# It requires the children to declare the abstract methods

from abc import ABC, abstractmethod

# Example 1

class Vehicle(ABC):

    @abstractmethod
    def start(self):
        pass

    @abstractmethod
    def stop(self):
        pass

class Car(Vehicle):
    
    def start(self):
        print("Car started")

    def stop(self):
        print("Car stopped")

# car = Car() # TypeError: Can't instantiate abstract class Car without an implementation for abstract methods 'start', 'stop'

car = Car()
car.start()
car.stop()