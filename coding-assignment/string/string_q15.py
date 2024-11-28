import re
s = "abc123def456ghi789"
numbers = re.findall(r'\d+', s)
print(numbers)
