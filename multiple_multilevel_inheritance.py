class Animal:
    def eat(self):
        print("Eating")

    def sleep(self):
        print("Sleeping")

class Prey(Animal):
    def flee(self):
        print("Fleeing")

class Predator(Animal):
    def hunt(self):
        print("Hunting")

class Rabbit(Prey):
    pass

class Hawk(Predator):
    pass

class Fish(Prey, Predator):
    pass

rabbit = Rabbit()
hawk = Hawk()
fish = Fish()

fish.flee()
fish.hunt()
fish.eat()