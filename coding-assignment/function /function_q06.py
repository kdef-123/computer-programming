#5. Check if a String is Palindrome
#Write a function that checks if a given string is a palindrome.

def is_palindrome(s):
    return s == s[::-1]
print(is_palindrome("madam"))
