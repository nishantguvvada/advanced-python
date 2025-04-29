# Lambda function is a small anonymous function for a one time use 
# They take any number of arguments, have only 1 expression
# Helps to keep the namespace clean
# Used with higher order functions such as sort(), map(), filter(), reduce()

# Example 1

# square = lambda x: x ** 2
# print(square(4))
# add = lambda x, y: x + y
# print(add(2, 34))
# max_value = lambda x, y: x if x > y else y
# print(max_value(3, 5))
# min_value = lambda x, y: x if x < y else y
# print(min_value(4, 6))
# full_name = lambda first, last: first + " " + last
# print(full_name("John", "Doe"))
# is_even = lambda x: x % 2 == 0
# print(is_even(5))
# age_check = lambda age: True if age > 18 else False
# print(age_check(14))

# Example 2

items = [1,2,3,4,5]
squared = list(map(lambda x: x**2, items))
print(squared)