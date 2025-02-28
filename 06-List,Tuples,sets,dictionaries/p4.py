# Dictionaries in python

student = {
    "name": "Pramod",
    "age": 25,
    "city": "Mumbai"
}
print(student["name"])  # Output: Pramod

# Modifying dictionary

student["age"] = 26
student["gender"] = "Male"  # Adds a new key-value pair

# Dictionary methods

print(student.keys())   # dict_keys(['name', 'age', 'city', 'gender'])
print(student.values())  # dict_values(['Pramod', 26, 'Mumbai', 'Male'])
print(student.items())   # dict_items([('name', 'Pramod'), ('age', 26), ...])

student.pop("city")  # Removes a key-value pair
