# Decorator = a function that extends the behavior of another function without modifying the base function
# Decorators allow code execution before and after a function
# Decorators wrap a function and modify it's behavior

# Example 1

def a_new_decorator(func):

    def wrapTheFunction():
        print("Working before executing func")
        func()
        print("Working after executing func")
    
    return wrapTheFunction

def a_function_requiring_decoration():
    print("A function which needs some decoration to remove it's foul smell")

a_function_requiring_decoration() # Output: A function which needs some decoration to remove it's foul smell

# @a_new_decorator is just a shorthand for
a_function_requiring_decoration = a_new_decorator(a_function_requiring_decoration)

a_function_requiring_decoration() 

# Output: 
# Working before executing func
# A function which needs some decoration to remove it's foul smell
# Working after executing func

# Using @
@a_new_decorator
def a_function_using_decorator():
    print("**** A function using some decoration ****")

a_function_using_decorator()

# our function is replaced by wrapTheFunction after decoration
# a_function_using_decorator.__name__ outputs wrapTheFunction

print(a_function_using_decorator.__name__) # Output: wrapTheFunction

# @wraps takes a function to be decorated 
# and adds the functionality of copying over the function name, docstring, arguments list, etc. 
# This allows us to access the pre-decorated function’s properties in the decorator.

from functools import wraps

def a_new_decorator(func):

    @wraps(func)
    def wrapper():
        print("I am doing some boring work before executing func()")
        func()
        print("I am doing some boring work after executing func()")

    return wrapper

@a_new_decorator
def a_function_with_wraps():
    print("Function with wraps")

print(a_function_with_wraps.__name__)

# Example 2
def add_sprinkles(func):
    def wrapper(*args, **kwargs): # wrapper function is required to avoid calling the decorated function at @add_sprinkles
        print("You add sprinkles")
        func(*args, **kwargs)
    return wrapper

def add_fudge(func):
    def wrapper(*args, **kwargs):
        print("You add fudge")
        func(*args, **kwargs)
    return wrapper

@add_sprinkles
@add_fudge
def get_ice_cream(flavor):
    print(f"Here is your {flavor} ice cream")

# Example 3

class Logit:
    _logfile = "out.log"

    def __init__(self, func):
        self.func = func

    def __call__(self, *args):
        print("Additional logic start: \n")
        # Additional Functionality start
        log_string = self.func.__name__ + " was called"
        print(log_string)
        
        with open(self._logfile, "a") as opened_file:
            opened_file.write(log_string + "\n")
        # Additional Functionality end

        print("Additional logic end \n")

        print("Base function start: \n")
        
        self.func(*args)

        print("Base function end: \n")

        print("Additional logic start: \n")

        print(f"Logging complete at {self._logfile}")

        print("Additional logic end \n")

        return 
    
# @Logit
# def logging_function(service):
#     print(f"Logging for {service}")

# logging_function("AWS")

def any_function(service):
    print(f"Function logged for {service}")

logit = Logit(any_function)
logit("AWS")