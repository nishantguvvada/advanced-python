# Context Manager defines runtime context of an executed code
# It handles entry into and exit from a runtime context of an executed code
# Context Manager object has an __enter__ and __exit__ method defined
# It allows to allocate and release resources
# Context Managers are invoked using the WITH statement

# Example 

with open("out.log", "r") as opened_file:
    logs = opened_file.read()

print(logs)

# Above code is equivalent to

file = open("out.log", "r")
try:
    output = file.read()
finally:
    file.close()

print(output)

# The main advantage of using a WITH statement is that it makes sure our file is closed 
# irrespective of the following operations or in the above example, success or failure of reading the file

# IMPLEMENTING A CONTEXT MANAGER AS A CLASS:

class File:
    def __init__(self, file_name, method):
        self.file_obj = open(file_name, method)
    
    def __enter__(self):
        return self.file_obj
    
    def __exit__(self, type, value, traceback):
        self.file_obj.close()
        if value:
            print("Exception handled gracefully")
            return True
        else:
            return False

with File("out.log", "r") as log_file:
    logged_activity = log_file.read()

print(logged_activity)

# Under the hood: with statement stores __exit__ method of the File class
# Under the hood: with statement calls __enter__ method of the File class
# Under the hood: __enter__ method opens the file and returns to log_file
# Under the hood: We read the log_file and store it in logged_activity variable
# Under the hood: with statement calls __exit__ method
# Under the hood: __exit__ method closes the file

# WHAT HAPPENS DURING ERROR, steps taken by the with statement when an error is encountered

# with statement passes type, value and traceback of the error to __exit__ method which handles the exception
# if __exit__ method return True, then the exception was handled gracefully
# if anything other than True is returned by the __exit__ method, exception is raised by the with statement

with File("out.log", "r") as log_file:
    logged_activity = log_file.undefined_function()

# IMPLEMENTING A CONTEXT MANAGER AS A GENERATOR:

from contextlib import contextmanager

@contextmanager
def open_file(file_name):
    f = open(file_name, "r")
    try:
        yield f
    finally:
        f.close()

with open_file("out.log") as file:
    output = file.read()

print("Output from GeneratorContextManager: ", output)