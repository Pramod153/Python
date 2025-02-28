# all in one example

# Lists
numbers = [10, 20, 30, 40, 50]
print("Sum of all elements:", sum(numbers))

names = ["John", "Alice", "Bob", "Charlie"]
names.sort()
print("Sorted names:", names)

# Tuples
cities = ("New York", "London", "Paris", "Tokyo", "Sydney")
print("Second city:", cities[1])

a, b = 5, 10
a, b = b, a  # Swapping using tuple unpacking
print("Swapped values:", a, b)

# Sets
set1 = {1, 2, 3, 4}
set2 = {3, 4, 5, 6}
print("Common elements:", set1.intersection(set2))

num_list = [1, 2, 2, 3, 4, 4, 5]
unique_nums = list(set(num_list))
print("List after removing duplicates:", unique_nums)

# Dictionaries
student = {"name": "Pramod", "age": 25, "marks": 85}
print("Student dictionary:", student)

student["marks"] = 90  # Updating marks
print("Updated student dictionary:", student)
