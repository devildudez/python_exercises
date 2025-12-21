
def count_Range(n,small,big)->int:
        for i in range(len(n)):
            if n[i]>=0:
                return n[i]
            elif n[i]<=small or n[i]==small:
                small=n[i]
                return small
            elif n[i]>=big:
                big=n[i]
                return big



n=[float(i) for i in input().split()]
small=-2000
big=1000
x=count_Range(n,small,big)
print(x)


