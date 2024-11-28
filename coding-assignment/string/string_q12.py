s = "The quick brown fox"
print(len([word for word in s.split() if word.lower().startswith('t')]))
