import math


def calculate_distance(x1, y1, x2, y2):
    """Вычисляет расстояние между двумя точками."""
    a = x2 - x1
    b = y2 - y1

    return math.sqrt(a * a + b * b)


def calculate_triangle_area(a, b, c):
    """Вычисляет площадь треугольника по формуле Герона."""
    p = (a + b + c) / 2

    return math.sqrt(p * (p - a) * (p - b) * (p - c))


print("Введите координаты точки A (x y):")
x1, y1 = map(float, input().split())

print("Введите координаты точки B (x y):")
x2, y2 = map(float, input().split())

print("Введите координаты точки C (x y):")
x3, y3 = map(float, input().split())

side_a = calculate_distance(x1, y1, x2, y2)
side_b = calculate_distance(x2, y2, x3, y3)
side_c = calculate_distance(x3, y3, x1, y1)

area = calculate_triangle_area(side_a, side_b, side_c)

print(f"Площадь треугольника: {area:.2f}")