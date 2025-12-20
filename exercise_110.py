"""
Exercise 110.
Read integers until the user enters 0, then output the numbers in sorted order
on separate lines.
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
