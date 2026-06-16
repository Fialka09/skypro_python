import math


def square(side: float) -> int:
    """Вычисляет площадь квадрата. Если сторона не целая, округляет вверх."""
    area = side * side
    return math.ceil(area)


side_length = 25.8
result = square(side_length)
print(f"Площадь квадрата равна: {result}")
