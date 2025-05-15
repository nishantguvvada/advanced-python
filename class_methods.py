# Class methods = allow operations related to the class
# takes class (cls) as the first parameter

class Student:

    count = 0
    total_gpa = 0

    def __init__(self, name, gpa):
        self.name = name
        self.gpa = gpa
        Student.count += 1
        Student.total_gpa += gpa

    @classmethod
    def get_student_count(cls):
        print(f"Total students: {cls.count}")

    @classmethod
    def get_average_gpa(cls):
        print(f"Average GPA: {cls.total_gpa / cls.count:.2f}")

bob = Student("Bob", 4.5)
sam = Student("Sam", 2.5)
mike = Student("Mike", 1.4)

Student.get_student_count()
Student.get_average_gpa()

bob.get_student_count() # Instance can access the class method

# EXTRA: HOW TO MAKE A METHOD INACCESSIBLE TO INSTANCES
class MyClass:

    @classmethod
    def class_only(cls):
        if not isinstance(cls, type):
            raise TypeError("Use the method on the class, cannot be called by an instance")
        print("Class-only method")

my_instance = MyClass()

MyClass.class_only() # Output: Class-only method

my_instance.class_only() # TypeError: Use the method on the class, cannot be called by an instance