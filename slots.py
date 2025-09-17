# By default, Python uses a dict to store an object's instance attributes
# The dict wastes a lot of RAM.
# Usage of __slots__ tell Python not to use a dict, only allocate space for a fixed set of attributes.

# without __slots__

class MyClass(object):
    def __init__(self, name, identifier):
        self.name = name
        self.identifier = identifier

# with __slots__

class MyClass(object):
    __slots__ = ['name','identifier']
    def __init__(self, name, identifier):
        self.name = name
        self.identifier = identifier