task = '''
1498.Given an array 
In one operation, you can increase any element by 1.
Find min operations to make all elements equal
'''


def min_moves(arr: list) -> int:

    if not arr:
        return 0

    # кол во действий (moves)
    x: int = 0
    max_val = max(arr)

    for i in range(len(arr)):

        while arr[i] != max_val:
            arr[i] += 1
            x += 1

    return x


if __name__ == '__main__':
    # lst = [1, 2, 3]
    lst = []
    res = min_moves(lst)
    print(res)
