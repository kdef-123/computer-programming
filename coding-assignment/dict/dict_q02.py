#2. Find the Key with the Maximum Value
#Problem: Find the key with the maximum value in a dictionary.


d = {'a': 1, 'b': 5, 'c': 3}
max_key = max(d, key=d.get)
print(max_key)
