s = "abcdef"
n = 3
substrings = [s[i:i+n] for i in range(len(s) - n + 1)]
print(substrings)
