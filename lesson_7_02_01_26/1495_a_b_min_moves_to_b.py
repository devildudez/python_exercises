task = '''
1495.Given a and b, in one move you can add +1, +2, or +5 to a.
Find minimum moves to reach b
'''

def min_moves(a: int, b: int) -> int:

    if a >= b:
        return 0

    # кол во действий (moves)
    x: int = 0

    while a < b:

        if a + 5 <= b:
            a = a + 5
            x += 1
            continue

        if a + 2 <= b:
            a = a + 2
            x += 1
            continue

        if a + 1 <= b:
            a = a + 1
            x += 1
            continue

    return x


def min_moves_2(a: int, b: int) -> int:

    if a >= b:
        return 0

    # кол во действий (moves)
    x: int = 0
    diff: int = b - a

    x += diff // 5
    diff = diff % 5

    x += diff // 2
    diff = diff % 2

    x += diff

    return x


if __name__ == '__main__':

    number_a = 1
    number_b = 24

    # res = min_moves(number_a, number_b)
    res = min_moves_2(number_a, number_b)
    print(res)


