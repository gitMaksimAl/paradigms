# Дан список целых чисел numbers. Необходимо написать в императивном стиле
# процедуру для сортировки в порядке убывания. Можно использовать любой алгоритм


def quicksort_imperative(target: list) -> list:
    if len(target) < 2:
        return target
    low, same, high = [], [], []
    pivot = target[int(len(target) / 2)]
    for item in target:
        if item < pivot:
            low.append(item)
        elif item == pivot:
            same.append(item)
        else:
            high.append(item)
    return quicksort_imperative(high) + same + quicksort_imperative(low)


numbers = [1, 11, 21, 19, 23, -3, 7, 13, -1, 5, 17, 3, 9, 5, 15]

# imperative decision
print(quicksort_imperative(numbers))

# declarative decision
print(sorted(numbers, reverse=True))
