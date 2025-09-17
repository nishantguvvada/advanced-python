# Singleton pattern in python is a design pattern to create just one instance of a class throughout the entire lifetime of a program
# Singleton pattern has many benefits:
# - To limit concurrent access to a shared resource
# - To create a global point of access for a resource
# - To create just one instance of a class

class Singleton(object):

    _instance = None

    def __init__(self):
        raise "Use get_instance() instead."
    
    @classmethod
    def get_instance(cls):
        if cls._instance is None:
            cls._instance = super().__new__(cls) # super() is used and it calls __new__ of the parent class, but what parent?
            # Every class implicitly inherits from object.
            # __new__() is used for creating a new instance of a class (before __init__ initializes it)
            # By calling super()__new__(cls), we are delegating instance creating to the object class's __new__ method
            # It allocates memory and returns a new instance of the class
            cls._instance.model = "openai" # attribute of the instance
        return cls._instance
    
if __name__ == "__main__":
    singleton1 = Singleton.get_instance()
    singleton2 = Singleton.get_instance()

    if singleton1 == singleton2:
        print("Both instances are the same Singleton object.")
    else:
        print("Not a singleton.")

    print(singleton1.model)