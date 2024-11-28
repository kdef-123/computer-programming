#2.Check If a Number Is Even or Odd
#Write a function that checks if a number is even or odd.

def is_even_or_odd(n):
    if n % 2 == 0:
        return "Even"
    else:
        return "Odd"
print(is_even_or_odd(4))
