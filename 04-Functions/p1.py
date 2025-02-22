# functions
def greet(name):
    print(f"Hello, {name}!")
greet("Pramod")  # Output: Hello, Pramod!

# functions with return value
def add(a, b):
    return a + b

result = add(5, 3)
print(result)  # Output: 8

# default arguements
def greet(name="Guest"):
    print(f"Hello, {name}!")

greet()             # Output: Hello, Guest!
greet("Pramod")     # Output: Hello, Pramod!

# Keyword Arguements
def info(name, age):
    print(f"{name} is {age} years old.")

info(age=25, name="Pramod") 

# Positional Variable Arguments (*args)

def sum_all(*numbers):
    return sum(numbers)

print(sum_all(1, 2, 3, 4))  # Output: 10

# Keyword Variable Arguments (**kwargs)

def print_info(**details):
    for key, value in details.items():
        print(f"{key}: {value}")

print_info(name="Pramod", age=25, city="Mumbai")
# Output: # name: Pramod # age: 25 # city: Mumbai