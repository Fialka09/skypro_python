import math


def square(side):
    area = side * side
    if isinstance(side, int):
        return area
    else:
        return math.ceil(area)


side_length = 25.8
result = square(side_length)
print(f"Площадь квадрата равна: {result}")
