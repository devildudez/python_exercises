def bubble(a: list) -> list:
    n = len(a)
    while True:
        sorted = True
        for i in range(n - 1):
            if a[i] > a[i + 1]:
                sorted = False
                a[i], a[i + 1] = a[i + 1], a[i]
        if sorted:
            break
    return a

print(bubble([4,6,8,3,2,5,7,8,9]))

