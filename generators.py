# Iterable - any object in python which has __iter__ or __getitem__ methods defined, returns an iterator
# Iterator - any object in python which has __next__ or next() methods defined
# Generators are iterators, can only be iterated over once, do not store any values in memory, generate values on the fly
# Generators are implemented as functions, they do not return a value, they yield

def fibbon(n):
    a = 1
    b = 1
    for i in range(n):
        yield a
        a, b = b, a + b

for x in fibbon(10):
    print(x)