import math


def solve_triangle(alpha=20.0, beta=20.0, gamma=20.0, b_side=50.0):
    a_side = b_side * math.sin(math.radians(alpha)) / math.sin(math.radians(beta))
    c_side = b_side * math.sin(math.radians(gamma)) / math.sin(math.radians(beta))

    return [a_side, c_side]


def get_side(pos_a, pos_b):
    side = math.sqrt((pos_a[0] - pos_b[0]) ** 2 + (pos_a[1] - pos_b[1]) ** 2)

    return side


def get_angle(a_side, c_side, b_angle):
    b_side = math.sqrt(a_side ** 2 + c_side ** 2 - 2 * a_side * c_side * math.cos(math.radians(b_angle)))
    # print('b_side', b_side)
    c_angle = math.degrees(math.acos((a_side ** 2 + b_side ** 2 - c_side ** 2) / (2 * a_side * b_side)))

    return c_angle