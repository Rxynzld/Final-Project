import math


def circle(first_num):
    # pi * radius ** 2
    radius = float(first_num)
    if radius <= 0:
        raise TypeError
    else:
        return math.pi * math.pow(radius, 2)


def square(first_num):
    # side1 ** 2
    side1 = float(first_num)
    if side1 <= 0:
        raise TypeError
    else:
        return side1 ** 2


def rectangle(first_num, second_num):
    # width * length
    width = float(first_num)
    length = float(second_num)
    if width <= 0 or length <= 0:
        raise TypeError
    else:
        return width * length


def triangle(first_num, second_num):
    # 1/2 * base * height
    base = float(first_num)
    height = float(second_num)
    if base <= 0 or height <= 0:
        raise TypeError
    else:
        return base * height * 0.5


def trapezoid(height, first_num, second_num, third_num):
    # A = b1 + b2 / 2 * h
    base1 = float(first_num)
    base2 = float(second_num)
    height = float(third_num)
    if base1 <= 0 or base2 <= 0 or height <= 0:
        raise TypeError
    else:
        return base1 + base2 / 2 * height


