from math import pow


# Реализовать процедуру для вычисления MSE в любой парадигме. Программа
# получает на вход два вектора и возвращает число - оценку MSE.
def get_mse(true: list, be: list) -> float:
    result = list(map(lambda x, y: (x - y) ** 2, true, be))
    # return 1 / len(true) * sum(result)
    return sum(result) / len(true)


# Реализовать сортировку слиянием.
def compare(left: list, right: list) -> list:
    i = 0
    j = 0
    result = list()
    while i < len(left) and j < len(right):
        if left[i] < right[j]:
            result.append(left[i])
            i += 1
        else:
            result.append(right[j])
            j += 1
    while i < len(left):
        result.append(left[i])
        i += 1
    while j < len(right):
        result.append(right[j])
        j += 1
    return result


def merge(array: list) -> list:

    if len(array) > 1:
        first = array[:len(array) // 2]
        second = array[len(array) // 2:]
        first = merge(first)
        second = merge(second)
        return compare(first, second)
    return array


print(get_mse([1, 2, 3, 4, 5], [2, 2, 3, 4, 3]))
print(merge([9, 3, 6, 7, 1, 8, 2, 4, 10, 5]))
