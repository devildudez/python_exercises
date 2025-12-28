def some_nested_stuff(lst: list) -> list:

    for i in range(len(lst)):
        print(lst[i])

        for j in range(0, i):
            print(f'ищо раз элементы все после i: {lst[j]}')

    return lst

some_nested_stuff([1, 2, 3])