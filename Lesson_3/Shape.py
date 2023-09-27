from abc import ABC
import math


class Shape(ABC):

    def get_perimeter(self):
        pass

    def get_area(self):
        pass


class Circle(Shape):

    _radius: float

    def __init__(self, radius: float):
        self._radius = radius

    def get_perimeter(self) -> float:
        return 2 * math.pi * self._radius

    def get_area(self) -> float:
        return math.pi * math.pow(self._radius, 2)


class Triangle(Shape):

    _a: float
    _b: float
    _c: float

    def __init__(self, a: float, b: float, c: float):
        if (a > b + c) or (b > a + c) or (c > a + b):
            raise ValueError
        self._a = a
        self._b = b
        self._c = c

    def get_perimeter(self) -> float:
        return self._a + self._b + self._c

    def get_area(self) -> float:
        _half_perimeter = self.get_perimeter() / 2
        return math.sqrt(_half_perimeter
                         * (_half_perimeter - self._a)
                         * (_half_perimeter - self._b)
                         * (_half_perimeter - self._c))
