CORRECT_PIN = "4590"

while True:
    pin = input("Введите пин-код: ")
    if pin == CORRECT_PIN:
        print("Доступ разрешен")
        break
    else:
        print("Ошибка. Попробуйте еще раз")
