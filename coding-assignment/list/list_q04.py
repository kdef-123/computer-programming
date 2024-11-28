ls = [1,3,3,2,3,4,5,3]
target = 3
count = ls.count(target)
for i in range(count):
    ls.remove(3)
print(ls)
