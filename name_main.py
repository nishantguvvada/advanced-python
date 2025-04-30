# __name__ == "__main__" allows the script to be imported or run standalone
# Functions and classes can be reused without executing the main block of code

def extra_function():
    print(f"Function can be executed with executing the main block of code in {__name__}")

def main():
    print(f"Executing the script {__name__}")

if __name__ == "__main__":
    main()