max_number = None

while True:
    num = int(input("Введите натуральное число (0 для выхода): "))

    if num == 0:
        break

    if max_number is None or num > max_number:
        max_number = num

if max_number is not None:
    print(f"Самое большое число: {max_number}")
else:
    print("Не было введено ни одного числа.")