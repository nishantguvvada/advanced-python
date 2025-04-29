# reduce function reduces a list of elements in a collection to a single value
# for loops are better in most cases
# reduce function is better for functional approach and readability

from functools import reduce

prices = [9.99, 5.99, 5.75, 2.00, 3.95, 4.50]

total_price = reduce(lambda x, y: x + y, prices)

print(total_price)