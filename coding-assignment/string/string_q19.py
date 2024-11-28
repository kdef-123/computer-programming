from collections import Counter
s = "aabbbccccd"
count = Counter(s)
print(count.most_common(1)[0][0])
