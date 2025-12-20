"""""
def a(x):
    small: int = -20340134
    big: int = 203059
    pos: int = 0
    pos1: int = 0
    for i in range(len(x)):
        if x[i] < small:
            pos=i
        elif x[i] > big:
            pos1 = i
        if x[i] == big or x[i] == small:
            del x[i]
            continue

f=[int(i) for i in input().split()]
print(a(f))
"""""
"""""
a:list=[i for i in input().split()]
b:list=[]
for i in range(len(a)):
    if a[i] not in b:
        b.append(a[i])
for i in range(len(b)):
    print(b[i])

"""""
