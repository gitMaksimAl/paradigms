# реализовать с использованием функциональной парадигмы процедуру normalization
# которая выполняет нормализацию полученного массива по формуле
def normalization(ls: list) -> list:
    min_value = min(ls)
    max_value = max(ls)

    def normalize_element(x):
        return (x - min_value) / (max_value - min_value)

    return list(map(normalize_element, ls))


def normalization_lambda(ls: list) -> list:
    min_value = min(ls)
    max_value = max(ls)

    return list(map(lambda x: (x - min_value) / (max_value - min_value), ls))


# Написать скрипт принимающий на вход массив с данными о людях и число - возраст
# возвращающий число - количество людей старше указанного возраста
def older_than_count(people: list, age: int) -> int:
    return len(list(filter(lambda x: x["age"] > age, people)))


# Реализовать с использованием функциональной парадигмы процедуру поиска
# дубликатов. Дубликаты должны быть выведены на экран в виде списка.
def get_doubles(ls: list) -> list:
    uniqs = set()
    # сравнение с пустым множеством, если элемент присутствует ЗНАЧИТ ЭТО
    # ЭТО ДУБЛИКАТ, если нет добавляем.
    return list(filter(lambda x: x in uniqs or uniqs.add(x), ls))


nums = [12, 5, 20, 6, 1, 9, 17, 5, 22, 15, 20, 31, 1, 7, 27, 15]
for _ in normalization_lambda(nums):
    print(f"{_:.2},", end=' ')
print()
employees = [{'name': 'Elizaveta', 'age': 25},
            {'name': 'Andrey', 'age': 30},
            {'name': 'Sergey', 'age': 35},
            {'name': 'Ivan', 'age': 40}]
print(older_than_count(employees, 30))
print(get_doubles(nums))
