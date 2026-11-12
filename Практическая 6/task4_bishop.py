# Задача 4. Ход слона

MIN_COORD = 1
MAX_COORD = 8

col1 = int(input("Введите столбец первой клетки (1-8): "))
row1 = int(input("Введите строку первой клетки (1-8): "))
col2 = int(input("Введите столбец второй клетки (1-8): "))
row2 = int(input("Введите строку второй клетки (1-8): "))

if not (
    MIN_COORD <= col1 <= MAX_COORD
    and MIN_COORD <= row1 <= MAX_COORD
    and MIN_COORD <= col2 <= MAX_COORD
    and MIN_COORD <= row2 <= MAX_COORD
):
    print("Ошибка ввода: координаты должны быть от 1 до 8.")
elif col1 == col2 and row1 == row2:
    print("Ошибка ввода: клетки должны быть различными.")
else:
    # Слон ходит по диагонали: смещение по столбцам равно смещению по строкам
    if abs(col1 - col2) == abs(row1 - row2):
        print("YES")
    else:
        print("NO")
