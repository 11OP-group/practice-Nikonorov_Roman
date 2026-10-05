import math


def calculate_rectangle_area(width, height):
    """Вычисляет площадь прямоугольника."""
    return width * height


def calculate_circle_area(radius):
    """Вычисляет площадь круга."""
    return math.pi * radius * radius


print("Введите ширину и высоту прямоугольника через пробел:")
width, height = map(float, input().split())

rectangle_area = calculate_rectangle_area(width, height)

print(f"Площадь прямоугольника: {rectangle_area:.2f}")


print("Введите радиус круга:")
radius = float(input())

circle_area = calculate_circle_area(radius)

print(f"Площадь круга: {circle_area:.2f}")