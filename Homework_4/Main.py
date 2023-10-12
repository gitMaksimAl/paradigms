from math import sqrt, pow


# Написать скрипт для расчета корреляции Пирсона между двумя величинами
# (массивами).
def num_correlation(ls1: list, ls2: list) -> float:
    mean1: float = sum(ls1) / len(ls1)
    mean2: float = sum(ls2) / len(ls2)

    def covariant() -> list:
        return list(map(lambda x1, y1: (x1 - mean1) * (y1 - mean2),
                        ls1, ls2))

    def disp(ls: list, mean: float) -> list:
        return list(map(lambda x1: pow(x1 - mean, 2), ls))

    return sum(covariant()) \
           / sqrt(sum(disp(ls1, mean1)) * sum(disp(ls2, mean2)))


x = [3.63, 3.02, 3.82, 3.42, 3.59, 2.87, 3.03, 3.46, 3.36, 3.3]
y = [53.1, 49.7, 48.4, 54.2, 54.9, 43.7, 47.2, 45.2, 54.4, 50.4]

print(num_correlation(x, y))
