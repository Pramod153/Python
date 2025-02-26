class Bird:
    def fly(self):
        print("Bird can fly")

class Penguin(Bird):
    def fly(self):
        print("Penguins cannot fly")

b = Bird()
b.fly()  # Output: Bird can fly

p = Penguin()
p.fly()  # Output: Penguins cannot fly
