# Iterable - any object in python which has __iter__ or __getitem__ methods defined, returns an iterator
# Iterator - any object in python which has __next__ or next() methods defined
# Generators are iterators, can only be iterated over once, do not store any values in memory, generate values on the fly
# Generators are implemented as functions, they do not return a value, they yield
# How generators work: Unlike return, which exits a function and returns a single value, 
# yield pauses the function's execution, returns the yielded value and saves the function's state
# Lazy evaluation: When a generator function is called, it returns a generator object (an iterator). 
# The code within the generator function only executes when next() is called on this object.
# Each time next() is called, the generator function resumes execution from where it last paused,
# continuing until it encounters another yield statement of the end of the function.

def fibbon(n):
    a = 1
    b = 1
    for i in range(n):
        yield a
        a, b = b, a + b

for x in fibbon(10):
    print(x)

def generator_function():
    yield 5
    yield 3
    yield 4

generator_object = generator_function()
print(generator_object)
print(generator_object.__next__())
print(generator_object.__next__())
print(generator_object.__next__())