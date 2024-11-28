st = 'abc'
n = len(st)
for i in range(2 ** n):
    comb = ''
    for j in range(n):
        if i  & (2**j):
            comb += st[j]
        else:
            comb += "0"
    print(comb[::-1])
