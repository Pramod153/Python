# Lambda to add two numbers
add = lambda a, b: a + b
print(add(3, 5))  # Output: 8

# Lambda with map(), filter(), reduce()

# map() – Apply a function to all items in a list:

numbers = [1, 2, 3, 4]
squared = list(map(lambda x: x**2, numbers))
print(squared)  # Output: [1, 4, 9, 16]

# filter() – Filter elements based on a condition:

numbers = [1, 2, 3, 4, 5, 6]
even = list(filter(lambda x: x % 2 == 0, numbers))
print(even)  # Output: [2, 4, 6]

# reduce() – Apply a rolling computation:

from functools import reduce

numbers = [1, 2, 3, 4]
product = reduce(lambda x, y: x * y, numbers)
print(product)  # Output: 24

