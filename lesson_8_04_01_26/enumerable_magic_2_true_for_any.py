from typing import Callable

task = '''
https://www.codewars.com/kata/54598e89cbae2ac001001135

Enumerable Magic #2 - True for Any?

Нужно написать функцию, которая проверяет: 
возвращает ли callback-функция true хотя бы для одного элемента массива.
'''

class CallableExmpl:
    def __call__(self, *args, **kwargs):
        print('я вызвал')


def any_(lst: list, cb: Callable[[int], bool]) -> bool:

    for elem in lst:

        if cb(elem):
            return True

    return False


if __name__ == '__main__':

    # эквивалентно lambda x: x % 2 == 0
    def is_delimiter_2(x) -> bool:
        return x % 2 == 0

    # Пример 1: Проверка на чётные числа
    numbers = [1, 3, 5, 8, 9]
    result = any_(numbers, lambda x: x % 2 == 0)
    print(f"Есть ли чётные числа в {numbers}? {result}")  # True (есть 8)

    # Пример 2: Проверка на отрицательные числа
    numbers2 = [1, 2, 3, 4]
    result2 = any_(numbers2, lambda x: x < 0)
    print(f"Есть ли отрицательные числа в {numbers2}? {result2}")  # False

    # Пример 3: Пустой массив
    empty = []
    result3 = any_(empty, lambda x: x > 0)
    print(f"Есть ли положительные числа в пустом массиве? {result3}")  # False

    # Пример 4: Строки длиннее 5 символов
    words = ["hi", "hello", "world"]
    result4 = any_(words, lambda s: len(s) > 5)
    print(f"Есть ли слова длиннее 5 символов? {result4}")  # False

    # Пример 5: Со своей функцией (не lambda)
    def is_long_word(word):
        """Проверяет, длиннее ли слово 4 символов"""
        return len(word) > 4

    words2 = ["cat", "dog", "elephant"]
    result5 = any_(words2, is_long_word)
    print(f"Есть ли длинные слова в {words2}? {result5}")  # True (elephant)