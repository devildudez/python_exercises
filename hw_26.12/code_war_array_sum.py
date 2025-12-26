def array_plus_array(arr1, arr2) -> int:
    sm1 = 0
    sm2 = 0

    for i in range(len(arr1)):
        sm1 += arr1[i]

    for j in range(len(arr2)):
        sm2 += arr2[j]

    return sm1 + sm2


a = [2, 4, 3, 1, 5]
b = [1, 5, 10, 2, 3]
print(array_plus_array(a, b))
