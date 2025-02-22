# Using Built-in Modules

import math

print(math.sqrt(16))   # Output: 4.0
print(math.pi)         # Output: 3.141592653589793

# Use the module in main.py:


import mymodule

print(mymodule.greet("Pramod"))   # Output: Hello, Pramod!
print(mymodule.add(5, 7))       # Output: 12
# Import Specific Functions


from mymodule import greet

print(greet("Pramod"))  # Output: Hello, Pramod!

#Using __name__ == "__main__"
# This lets you control how your Python files run.


# mymodule.py
def greet(name):
    return f"Hello, {name}!"

if __name__ == "__main__":
    print(greet("Pramod"))  # Only runs if this file is executed directly
