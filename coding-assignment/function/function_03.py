#3. Factorial of a Number
#Write a function that calculates the factorial of a given number.

def factorial(n):
    if n == 0 or n == 1:
        return 1
    else:
        return n * factorial(n - 1)
print(factorial(5))
