class Animal:
    def speak(self):
        print("This animal makes a sound")

# Dog class inherits from Animal
class Dog(Animal):
    def speak(self):
        print("Dog barks")

d = Dog()
d.speak()  # Output: Dog barks
