# Static methods = methods that belong to the class rather than any object of the class
# Used for general utilitiy functions that don't require object-specific state or need access to any information
# Instance methods are best for operations on instances of the class

# Example

class Employee:

    def __init__(self, name, position):
        self.name = name
        self.position = position

    def get_information(self):
        print(f"{self.name} is a {self.position}")

    @staticmethod
    def is_valid_position(position):
        valid_positions = ["Cook", "Janitor", "Engineer", "Manager"]
        return position in valid_positions
    
cook = Employee("Alex","Cook")
janitor = Employee("David","Janitor")

cook.get_information()
janitor.get_information()

print(Employee.is_valid_position("Engineer"))
print(cook.is_valid_position("Scientist")) # a static method can be called by an instance of the class