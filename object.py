# Every class inherits from `object`
# Every class is an instance of `type`

class A(object):
    pass

print(isinstance(A, type)) # True: A is an instance of type
print(issubclass(A, object)) # True: A inherits from object