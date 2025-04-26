# Exception = An event that interrupts the flow of a program
# try except else finally
# Code that can cause an exception is put in the try block, handling of exception is implemented in except block
# Code in except block will only execute if try block runs into exception
# Code in the finally block will run whether or not an exception occurred

# Example 1
try:
    number = int(input("Enter a number\n"))
    print(1 / number)
except ZeroDivisionError:
    print("Input a number greater than 0")
except ValueError:
    print("Input takes numbers only")
except Exception:
    print("Something went wrong!")
finally:
    print(f"Completed")


# Example 2
try:
    file = open("test.txt", "rb")
except IOError as e:
    print("An IOError occurred. {}".format(e.args[-1]))


# Example 3
try:
    print("I'm sure no exception is going to occur!")
except Exception:
    print("exception")
else:
    # Code that should run only if no exception occurs in try but for which exceptions should not be caught
    print('This would only run if no exception occurs. And an error here '
          'would NOT be caught.')
finally:
    print("This would be printed in every case")