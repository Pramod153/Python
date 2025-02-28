# sets in python

numbers = {1, 2, 3, 4, 5}
print(numbers)  # Output: {1, 2, 3, 4, 5}

# set operations

numbers.add(6)  # Adds an element
numbers.remove(3)  # Removes an element
print(3 in numbers)  # Output: False

set1 = {1, 2, 3}
set2 = {3, 4, 5}

print(set1.union(set2))  # {1, 2, 3, 4, 5}
print(set1.intersection(set2))  # {3}
print(set1.difference(set2))  # {1, 2}

