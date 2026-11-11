import math


def area(r):
    """
    Вычисляет площадь круга.

    Пример вызова:
        >>> area(2)
        12.566370614359172
    """
    return math.pi * r * r


def perimeter(r):
    """
    Вычисляет периметр круга.

    Пример вызова:
        >>> perimeter(2)
        12.566370614359172
    """
    return 2 * math.pi * r
