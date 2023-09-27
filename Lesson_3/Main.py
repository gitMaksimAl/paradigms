import sys

from Shape import Circle, Triangle

try:
    circle = Circle(2)
    triangle = Triangle(3, 4, 5)
except ValueError:
    print('Can`t create triangle', file=sys.stderr)
    exit(1)

if __name__ == "__main__":
    print(f"circle perimeter: {circle.get_perimeter():.2f}")
    print(f"circle area: {circle.get_area():.2f}")
    print(f"triangle perimeter: {triangle.get_perimeter():.2f}")
    print(f"triangle area: {triangle.get_area():.2f}")
