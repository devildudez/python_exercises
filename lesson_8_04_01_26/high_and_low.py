import sys

task = '''
https://www.codewars.com/kata/554b4ac871d6813a03000035
7 kyu

Highest and Lowest

В этом небольшом задании вам дана строка с числами, разделёнными пробелами, 
и вы должны вернуть наибольшее и наименьшее число.

Примеры

high_and_low("1 2 3 4 5") # return "5 1"
high_and_low("1 2 -3 4 5") # return "5 -3"
high_and_low("1 9 3 4 -5") # return "9 -5"

Примечания

- Все числа являются валидными Int32, не нужно их проверять.
- Во входной строке всегда будет хотя бы одно число.
- Выходная строка должна содержать два числа, разделённых одним пробелом, 
причём наибольшее число идёт первым.
'''


def high_and_low(numbers: str) -> str:

    max_val = -sys.maxsize - 1
    min_val = sys.maxsize

    vals = numbers.split()
    for elem in vals:
        if int(elem) > max_val:
            max_val = int(elem)
        if int(elem) < min_val:
            min_val = int(elem)

    return f'{max_val} {min_val}'


if __name__ == '__main__':
    print(high_and_low("1 2 3 4 5")) # return "5 1"
    print(high_and_low("1 2 -3 4 5")) # return "5 -3"
    print(high_and_low("1 9 3 4 -5")) # return "9 -5"
