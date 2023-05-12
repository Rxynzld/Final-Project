import math


#perimeter of circle
def circle(first_num):
    #2*pi*r
    radius = float(first_num)
    if radius <= 0:
        raise TypeError
    else:
        return 2 * math.pi * radius


#perimeter of square
def square(first_num):
    #4*a
    side1 = float(first_num)
    if side1 <= 0:
        raise TypeError
    else:
        return side1 * 4


#perimeter of rectangle
def rectangle(first_num, second_num):
    #2 (l + w)
    width = float(first_num)
    length = float(second_num)
    if width <= 0 or length <= 0:
        raise TypeError
    else:
        return 2 * (width + length)


#perimeter of triangle
def triangle(first_num, second_num, third_num):
    #a+b+c
    a = float(first_num)
    b = float(second_num)
    c = float(third_num)
    if base1 <= 0 or base2 <= 0 or height <= 0:
        raise TypeError
    else:
        return a + b + c
