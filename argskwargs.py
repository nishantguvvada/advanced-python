# Arbitrary = varying amounts of arguments
# *args = arguments - allows you to use multiple non-key arguments
# *kwargs = keyword arguments - allows you to use mutlple keyword arguments
# Prefix each with an unpacking operator (*)
# All the non-key arguments are packed in a tuple
# All the keyword arguments are packed in a dictionary

def add(*args):
    print("Type of *args: ",type(args))
    total = 0
    for arg in args:
        total += arg
    return total

# print(add(1,2,3))

def print_address(*args, **kwargs):
    print("Type of *args: ",type(args))
    for arg in args:
        print(arg, end=" ")
    print()
    print("Type of **kwargs: ", type(kwargs))
    for key, value in kwargs.items():
        print(f"{key}:{value}")

print_address("Spongebob", "Squarepants",
    street="Fake St. 21",
    apt="21 Apt.",
    city="New York",
    zip="54213"
)