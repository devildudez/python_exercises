"""
Упражнение 111. Обратный порядок

Напишите программу, которая, как и в предыдущем случае, будет за-
прашивать у пользователя целые числа и сохранять их в виде списка.
Индикатором окончания ввода значений также должен служить ноль. На
этот раз необходимо вывести на экран введенные значения в порядке
убывания.
"""


def solution_1():

    a: list[int] = []
    n = int(input())

    while n != 0:
        a.append(n)
        n = int(input())

    a.sort(reverse=True)

    return a


def solution_2():

    a: list[int] = []
    n = int(input())

    while n != 0:
        a.append(n)
        n = int(input())

    # O(n^2), где n - длина массива a

    # binary search (бинарный поиск) - работает посредством деления
    # массива точно по середине
    for j in range(len(a) - 1):

        for i in range(len(a) - 1):
            if a[i + 1] > a[i]:
                h = a[i]
                a[i] = a[i + 1]
                a[i + 1] = h

    return a


if __name__ == '__main__':

    # r_1 = solution_1()
    # print(r_1)

    r_2 = solution_2()
    print(r_2)


