def subs(a: list, b: list) -> bool:
        for i in range(len(a)):
            for j in range(i + 1, len(a) + 1):
                if a[i:j] == b:
                    return True
        return False

a = [int(i) for i in input().split()]
b = [int(j) for j in input().split()]
print(subs(a, b))