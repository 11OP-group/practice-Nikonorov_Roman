# Задача 3. Шахматная доска

MIN_COORD = 1
MAX_COORD = 8

col1 = int(input("Введите столбец первой клетки (1-8): "))
row1 = int(input("Введите строку первой клетки (1-8): "))
col2 = int(input("Введите столбец второй клетки (1-8): "))
row2 = int(input("Введите строку второй клетки (1-8): "))

# Проверка корректности координат доски 8x8
if not (
    MIN_COORD <= col1 <= MAX_COORD
    and MIN_COORD <= row1 <= MAX_COORD
    and MIN_COORD <= col2 <= MAX_COORD
    and MIN_COORD <= row2 <= MAX_COORD
):
    print("Ошибка ввода: координаты должны быть от 1 до 8.")
else:
    # Клетки одного цвета, если четность суммы их координат совпадает
    if (col1 + row1) % 2 == (col2 + row2) % 2:
        print("YES")
    else:
        print("NO")
