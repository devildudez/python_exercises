task = """
отсортировать массив [12, 6, 3, 12, 7] метдом selection sort 
и сказать почему это не лучший метод сортировки для данного массива
"""


def selection(arr: list) -> list:

    n = len(arr)

    for i in range(n):
        min_index = i

        for j in range(i + 1, n):
            if arr[j] < arr[min_index]:
                min_index = j
        if min_index != i:
            arr[i], arr[min_index] = arr[min_index], arr[i]

    return arr


a = [12, 6, 3, 12, 7]
print(selection(a))
