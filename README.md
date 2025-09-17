# Advanced Python Concepts with examples

## 1. @property

- Decorator used to define a method as a property i.e. can be accessed like an attribute
- Additional logic can be added when reading, writing or deleting attributes
- Decorator provides getter, setter and deleter method
- If an object defines \_\_set\_\_() or \_\_delete\_\_(), it is considered a data descriptor, @property is a succinct way of building a data descriptor
- EXTRA: HOW TO HIDE CLASS OR INSTANCE VARIABLES: Use \_ or \_\_ prefix or use @property to restrict access

## 2. Decorators

- Decorator is a function that extends the behavior of another function without modifying the base function
- Pass the function as an argument to the decorator

## 3. Context Manager

- Context Manager defines runtime context of an executed code, it has \_\_enter\_\_ and \_\_exit\_\_ methods, it is invoked using WITH statement
- Context Managers can be implemented as a class and as a generator

## 4. Abstract Class

- A class that cannot be instantiated on it's own, it is meant to be subclassed i.e. prevents instantiation of the class itself
- Abstract class contains abstract methods, which are declared but have no implementation, requires children subclassing the abstract class to declare the abstract methods

## 5. Super method

- Function used in the child class to call the methods of the parent
- It extends the functionality of the parent/inherited methods

## 6. Static method

- Methods that belong to the class rather than any object of the class, used for general utility functions
- Static methods are regular functions defined within the scope of a class. They are used for utility functions that are logically related to the class but do not require access to either instance-specific data or class-specific data. They operate purely on the arguments passed to them.
- Instance methods are best for operations on instances of the class
- Static method can be accessed by the instance

## 7. Class method

- Class methods allow operations related to the class, takes class (cls) as the first parameter instead of self
- Best for class level data
- Class method can be accessed by the instance
- EXTRA: HOW TO MAKE A METHOD INACCESSIBLE TO INSTANCES: Use `if not isinstance(cls, type): raise TypeError`

## 8. Magic method

- Magic methods are also called Dunder methods (double underscore example: \_\_init\_\_, \_\_str\_\_, \_\_eq\_\_)
- They are automatically called by Python's built-in operations
- They allow to define or customize behavior of operations

## 9. Lambda function

- Lambda function is a small anonymous function for a one time use (throw away function)
- They take any number of arguments, have only 1 expression
- Helps to keep the namespace clean
- Used with higher order functions sort(), map(), reduce(), filter()

## 10. map function

- map function applies a given function to all items in a collection

## 11. filter function

- filter function returns all elements of a collection that pass a condition

## 12. reduce function

- reduce function reduces all the elements of a collection to a single value
- for loops are better in most cases
- reduce function is better for a functional approach and readability

## 13. \_\_name\_\_ == "\_\_main\_\_"

- It allows the script to be imported or run standalone
- Functions and classes in the module can be reused without the main block of code executing

## 14. Inheritance

- Inheritance allows a class to inherit the attributes and methods from another class
- helps in code reusability and extensibility
- class Child(Parent) or class Sub(Super)

## 15. Multiple and Multi-level inheritance

- Mulitple inheritance = inherit from more than one parent class
- Multi-level inheritance = inherit from a parent which inherits from another parent

## 16. Polymorphism

- Polymorphism is a greek word that means to have many forms
- Two ways to achieve polymorphism: Inheritance and Duck Typing

## 17. Duck Typing

- Duck typing is another way to achieve polymorphism besides inheritance
- Objects must have minimum necessary attributes/methods
- "If it looks like a duck and quack like a duck, it must be a duck"

## 18. Exception

- Exception is an event that interrupts the flow of a program
- try: Code that can cause an exception is put in the try block
- except: handling of exception is implemented in except block
- else: Code that should run only if no exception occurs in try but for which exceptions should not be caught is put in else block
- finally: Code in the finally block will run whether or not an exception occurred

# 19. Generators

- Iterable - any object in python which has \_\_iter\_\_ or \_\_getitem\_\_ method defined, returns an iterator
- Iterator - any object in python which has \_\_next\_\_ or next() method defined
- Generators are iterators, can only be iterated over once, do not store values in memory, generate values on the fly
- Generators are implemented as function, they do not return a value, they yield

# 20. Multi-threading

- Used to perform multiple tasks concurrently (multitasking)
- Good for I/O bound tasks like reading files or fetching data from APIs
- threading.Thread(target=my_function)

# 21. Arbitrary arguments and keyword arguments

- Arbitrary = varying amounts of arguments
- To accept varying amounts of arguments, we can use \*args or \*\*kwargs
- \*args = arguments - allows you to pass multiple non-key arguments
- \*\*kwargs = keyword arguments - allows you to pass multiple keyword arguments
- Prefix each with an unpacking operator (\*)
- All the non-key arguments are packed in a tuple for \*args
- All the keyword arguments are packed in a dictionary for \*\*kwargs

# 22. \_\_slots\_\_

- By default, Python uses a dict to store an object's instance attributes.
- The dict wastes a lot of RAM.
- Usage of \_\_slots\_\_ tells Python not to use a dict, and only allocate space for a fixed set of attributes.

# 23. The root base class: `object`

- Every class inherits from `object`
- Every class is an instance of `type`
