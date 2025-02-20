# Write a function to check if a number is prime.
def prime(num):
    if(num%2==0):
        return f"the given number {num} is prime"
    else:
        return f"the given number {num} is  not prime"
print(prime(2))

