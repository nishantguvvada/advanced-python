# Iterable - any object in python which has __iter__ or __getitem__ methods defined, returns an iterator
# Iterator - any object in python which has __next__ or next() methods defined
# Generators are iterators, can only be iterated over once, do not store any values in memory, generate values on the fly
# Generators are implemented as functions, they do not return a value, they yield
# Unlike return, which exits a function and returns a single value, yield pauses the function's execution, returns the yielded value
# and saves the function's state
# When a generator function is called, it returns a generator object (an iterator). The code within the generator function only executes
# when next() is called on this object.

def fibbon(n):
    a = 1
    b = 1
    for i in range(n):
        yield a
        a, b = b, a + b

for x in fibbon(10):
    print(x)