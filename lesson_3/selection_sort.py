"""
Selection Sort — Сортировка выбором

Идея: На каждом шаге находим минимальный элемент в неотсортированной части
и ставим его на своё место.

Сложность:
    - Время: O(n²) — всегда
    - Память: O(1) — in-place
    - Стабильность: НЕТ
"""


def selection_sort(arr: list) -> list:
    """
    Классическая реализация Selection Sort.
    Сортирует список на месте (in-place).
    """
    n = len(arr)

    for i in range(n):
        # Предполагаем, что минимум — текущий элемент
        min_index = i

        # Ищем настоящий минимум в оставшейся части
        for j in range(i + 1, n):
            if arr[j] < arr[min_index]:
                min_index = j

        # Меняем местами, если нашли меньший элемент
        if min_index != i:
            arr[i], arr[min_index] = arr[min_index], arr[i]

    return arr


def selection_sort_with_steps(arr: list) -> list:
    """
    Версия с выводом каждого шага — для демонстрации на уроке.
    """
    a = arr.copy()  # Не портим оригинал
    n = len(a)

    print(f"Исходный массив: {a}")
    print("-" * 40)

    for i in range(n):
        min_index = i

        # Поиск минимума
        for j in range(i + 1, n):
            if a[j] < a[min_index]:
                min_index = j

        # Показываем что нашли
        print(f"Шаг {i + 1}: ищем минимум в {a[i:]}")
        print(f"         минимум = {a[min_index]} (индекс {min_index})")

        # Swap
        if min_index != i:
            a[i], a[min_index] = a[min_index], a[i]
            print(f"         меняем местами: {a[i]} ↔ позиция {i}")
        else:
            print(f"         уже на месте")

        print(f"         результат: {a}")
        print()

    print(f"Отсортировано: {a}")
    return a


# ============================================================
# ДЕМОНСТРАЦИЯ
# ============================================================

if __name__ == "__main__":
    # Пример 1: Базовое использование
    # print("=" * 50)
    # print("ПРИМЕР 1: Базовая сортировка")
    # print("=" * 50)
    #
    # numbers = [64, 25, 12, 22, 11]
    # print(f"До:    {numbers}")
    # selection_sort(numbers)
    # print(f"После: {numbers}")

    # Пример 2: Пошаговая демонстрация
    # print("\n" + "=" * 50)
    # print("ПРИМЕР 2: Пошаговая демонстрация")
    # print("=" * 50 + "\n")
    #
    # demo = [29, 10, 14, 37, 13]
    # selection_sort_with_steps(demo)

    # Пример 3: Уже отсортированный (всё равно O(n²)!)
    print("\n" + "=" * 50)
    print("ПРИМЕР 3: Уже отсортированный массив")
    print("=" * 50)

    sorted_arr = [1, 2, 3, 4, 5]
    print(f"До:    {sorted_arr}")
    selection_sort_with_steps(sorted_arr)
    print(f"После: {sorted_arr}")
    print("⚠️  Даже для отсортированного — всё равно O(n²) сравнений!")
