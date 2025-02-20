class BankAccount:
    def __init__(self, owner, balance=0):
        self.owner = owner
        self.balance = balance

    def deposit(self, amount):
        self.balance += amount
        return f"Deposited {amount}, New Balance: {self.balance}"

    def withdraw(self, amount):
        if amount > self.balance:
            return "Insufficient funds"
        self.balance -= amount
        return f"Withdrew {amount}, New Balance: {self.balance}"

# Creating an object
account = BankAccount("Pramod", 1000)
print(account.deposit(500))  # Output: Deposited 500, New Balance: 1500
print(account.withdraw(2000))  # Output: Insufficient funds
