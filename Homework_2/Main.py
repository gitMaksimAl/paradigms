"""
На вход подается число n.
Написать скрипт в любой парадигме, который выводит на экран таблицу умножения
всех чисел от 1 до n. Обоснуйте выбор парадигм.
"""
from sys import stderr


# Для вывовда таблицы умножения выбрана структурная функциональная парадигма
# для дальнейшего переиспользования блоков кода и оперирования параметрами
# функций
def print_mult_table_from_one(end: int = 1) -> None:
    """
    Print multiplication table of all positive decimal numbers from 1
    to end(default = 1)
    :param end: positive number
    :return: no return
    """
    end += 1
    for i in range(1, end):
        for j in range(i, end):
            print(f"{i} * {j} = {i * j}", end='\t')
        print()


# adapter
def get_positive() -> int:
    number = 1
    try:
        number = int(input('Please enter positive decimal number: '))
    except ValueError:
        print('Wrong input.', file=stderr)
    return abs(number)


print_mult_table_from_one(get_positive())
