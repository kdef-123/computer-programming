s = "this is a test, is it working?"
substring = "is"
indices = [i for i in range(len(s)) if s.startswith(substring, i)]
print(indices)
