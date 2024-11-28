s = "hello123 world!@#"
cleaned_s = ''.join(c for c in s if c.isalpha())
print(cleaned_s)
