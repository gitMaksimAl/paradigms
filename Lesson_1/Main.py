# Предположим, что нам хочется для любого массива чисел array и любого числа
# target узнать содержится ли target в array. Такую процедуру будем
# называть поиском.

# Задача
# Реализовать императивную функцию поиска элементов на языке Python.

def search_imperative(target: int, array: []) -> bool:
    for i in range(len(array)):
        if array[i] == target:
            return True
    return False


def search_declarative(target: int, array: []) -> bool:
    return target in array

# На вход подается: список целых чисел arr

# Задача
# Реализовать императивную функцию, которая возвращает три числа:
# Долю позитивных чисел
# Долю нулей
# Долю отрицательных чисел


def portion_imperative(array: list) -> dict:
    portions = {"positive": 0, "negative": 0, "zero": 0}
    for i in array:
        if i > 0:
            portions["positive"] += 1
        elif i < 0:
            portions["negative"] += 1
        else:
            portions["zero"] += 1
    portions["positive"] /= len(array)
    portions["negative"] /= len(array)
    portions["zero"] /= len(array)
    return portions


def portion_declarative(array: list) -> dict:
    portions = {
        "positive": len(list(filter(lambda x: x > 0, array))) / len(array),
        "negative": len(list(filter(lambda x: x < 0, array))) / len(array),
        "zero": len(list(filter(lambda x: x == 0, array))) / len(array)}
    return portions


print(portion_imperative([3, 0, -12, 1, -7, 4, 6, 0, -3, -13]))
print(portion_declarative([3, 0, -12, 1, -7, 4, 6, 0, -3, -13]))
