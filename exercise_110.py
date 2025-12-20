"""
Exercise 110.
Read integers until the user enters 0, then output the numbers in sorted order
on separate lines.
"""

"""
Упражнение 110. Порядок сортировки

Напишите программу, которая будет запрашивать у пользователя цело-
численные значения и сохранять их в виде списка. Индикатором оконча-
ния ввода значений должен служить ноль. Затем программа должна вы-
вести на экран все введенные пользователем числа (кроме нуля) в порядке
возрастания – по одному значению в строке. Используйте для сортировки
либо метод sort, либо функцию sorted.
"""


def main() -> None:
    numbers: list[int] = []

    while True:
        value = int(input())
        if value == 0:
            break
        numbers.append(value)

    numbers.sort()

    for number in numbers:
        print(number)


if __name__ == "__main__":
    main()
