# Magic methods are also called Dunder methods (double underscore)
# They are automatically called by Python's built-in operations such as +, -, >, < and so on
# They allow to define or customize the behavior of operations

class Book:

    def __init__(self, title, author, num_pages):
        self.title = title
        self.author = author
        self.num_pages = num_pages

    def __str__(self): # The __str__ method in Python is called when a string representation of an object is needed. 
        return f"'{self.title}' by {self.author}"
    
    def __eq__(self, other):
        return self.author == other.author

    def __gt__(self, other):
        return self.num_pages > other.num_pages
    
    def __getitem__(self, key):
        if key.lower() == "author":
            return self.author
        elif key.lower() == "title":
            return self.title
        elif key.lower() == "num_pages":
            return self.num_pages
        else:
            print(f"Key '{key}' not found in {self.title}")
    
book1 = Book("The Da Vinci Code", "Dan Brown", 435)
book2 = Book("A Thousand Splendid Suns", "Khaled Hosseini", 354)
book3 = Book("Midnight's Children", "Salman Rushdie", 250)

print(book1)
print(book2 == book1)
print(book1 > book2)
print(book1["author"])