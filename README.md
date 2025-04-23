# Advanced Python Concepts with examples

## 1. @property

- Decorator used to define a method as a property i.e. can be accessed like an attribute
- Additional logic can be added when reading, writing or deleting attributes
- Decorator provides getter, setter and deleter method

## 2. Decorators

- Decorator is a function that extends the behavior of another function without modifying the base function
- Pass the function as an argument to the decorator

## 3. Context Manager

- Context Manager defines runtime context of an executed code, it has ** enter** and ** exit** methods, it is invoked using WITH statement
- Context Managers can be implemented as a class and as a generator

## 4. Abstract Class

- A class that cannot be instantiated on it's own, it is meant to be subclassed i.e. prevents instantiation of the class itself
- Abstract class contain abstract methods, which are declared but have not implementation, requires children subclassing the abstract class to declare the abstract methods

## 5. Super method

- Function used in the child class to call the methods of the parent
- It extends the functionality of the parent/inherited methods

## 6. Static method

- methods that belong to the class rather than any object of the class, used for general utility functions
- instance methods are best for operations on instances of the class
