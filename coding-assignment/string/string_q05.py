s = "The quick brown fox jumped over the lazy dog"
words = s.split()
longest_word = max(words, key=len)
print(longest_word)
