import numpy as np

# Structure paradigm
# След матрицы
array_2d = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9]])
matrix_trace = 0
for i in range(0, len(array_2d)):
    matrix_trace += array_2d[i][i]


# Procedure paradigm
# matrix trace
def get_trace(array: np.array) -> int:
    trace = 0
    for i in range(0, len(array)):
        trace += array[i][i]
    return trace


# To binary in structure-procedure paradigm
def to_binary(number: int) -> str:
    binary = ''
    while number > 0:
        binary = '{}{}'.format(str(number % 2), binary)
        number //= 2
    return binary


print(matrix_trace)
print(get_trace(array_2d))
num = 15
print(f"{num} to binary: {to_binary(num)}")
