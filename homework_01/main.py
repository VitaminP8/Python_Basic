"""
Домашнее задание №1
Функции и структуры данных
"""


def power_numbers(*numbers):
    """
    функция, которая принимает N целых чисел,
    и возвращает список квадратов этих чисел
    >>> power_numbers(1, 2, 5, 7)
    <<< [1, 4, 25, 49]
    """
    return [num ** 2 for num in numbers]


# filter types
ODD = "odd"
EVEN = "even"
PRIME = "prime"


def filter_numbers(numbers_list, filter_type):
    if filter_type == ODD:
        return [num for num in numbers_list if num % 2 != 0]
    if filter_type == EVEN:
        return [num for num in numbers_list if num % 2 == 0]
    if filter_type == PRIME:
        ans = []
        for num in numbers_list:
            x = 0
            if num == 0 or num == 1:
                continue
            for i in range(2, num // 2+1):
                if num % i == 0:
                    x = x + 1
            if x == 0:
                ans.append(num)
        return ans
