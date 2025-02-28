# List in python
# creating
fruits = ["apple", "banana", "cherry"]
print(fruits)  # Output: ['apple', 'banana', 'cherry']

# accessing
print(fruits[0])   # Output: apple
print(fruits[-1])  # Output: cherry

# modify
fruits[1] = "blueberry"
print(fruits)  # Output: ['apple', 'blueberry', 'cherry']

# methods
fruits.append("mango")  # Adds an element at the end
fruits.insert(1, "orange")  # Inserts at a specific index
fruits.remove("cherry")  # Removes an element
fruits.pop()  # Removes last element
fruits.sort()  # Sorts list
print(fruits)



