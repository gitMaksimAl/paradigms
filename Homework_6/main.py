"""
GeekBrains. Paradigms seminar 6. Homework.
Task:
    Write script in any paradigm for binary search items in array.
Description:
    Для бинарного поиска выбрана структурная функциональная парадигма.
    Для сортировки списка данных выбрана функциональная парадигма. Используется
    встроенная функция списка в языке Python.
"""
import random
from typing import Any


# Написать программу в любой парадигме для бинарного поиска. На вход подается
# массив, выход - индекс элемента или -1 при отсутствии.
def bin_search(target: list, value: Any) -> int:
    """
    Binary search. Sorts the target array by built-in sorting and searches for
    the desired value in it. If no value is found, returns -1.
    :param target: mutable list
    :param value: Any comparable object contained in the target
    :return: index of value
    """

    def _search(ls: list, val: Any, left: int = 0,
                right: int = len(target) - 1) -> int:
        if left > right:
            return -1
        else:
            middle = (right - left) // 2 + left
            if ls[middle] == val:
                return middle
            elif ls[middle] > val:
                return _search(ls, val, left, middle - 1)
            else:
                return _search(ls, val, middle + 1, right)

    target.sort()
    return _search(target, value)


if __name__ == "__main__":
    names = ['Fedor', 'Sergey', 'Andrey',
             'Rostislav', 'Boris', 'Inokenti', 'Artem']
    nums = [random.randint(7, 33) for i in range(9)]
    print(f"11 index: {bin_search(nums, 11)}")
    print(nums)
    print(f"Boris index: {bin_search(names, 'Boris')}")
    print(names)
