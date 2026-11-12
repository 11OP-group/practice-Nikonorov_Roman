# Задача 2. Цвета колеса рулетки

MIN_POCKET = 0
MAX_POCKET = 36

pocket = int(input("Введите номер кармана (0-36): "))

# Проверка диапазона от 0 до 36
if not (MIN_POCKET <= pocket <= MAX_POCKET):
    print("ошибка ввода")
else:
    if pocket == 0:
        color = "зеленый"
    elif 1 <= pocket <= 10 or 19 <= pocket <= 28:
        # В этих диапазонах нечетные — красные, четные — черные
        if pocket % 2 != 0:
            color = "красный"
        else:
            color = "черный"
    else:
        # В диапазонах 11-18 и 29-36 нечетные — черные, четные — красные
        if pocket % 2 != 0:
            color = "черный"
        else:
            color = "красный"

    print(f"Цвет кармана {pocket}: {color}")
