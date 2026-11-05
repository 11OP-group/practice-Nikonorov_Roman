total_sum = 0

while True:
    price = int(input("Введите цену товара (0 для завершения): "))

    if price == 0:
        break

    if price < 0:
        print("Ошибка цены")
        continue

    total_sum += price

# Применение скидки 10%, если сумма больше 1000
if total_sum > 1000:
    total_sum *= 0.9
    print(f"Итоговая сумма к оплате (со скидкой 10%): {total_sum}")
else:
    print(f"Итоговая сумма к оплате: {total_sum}")