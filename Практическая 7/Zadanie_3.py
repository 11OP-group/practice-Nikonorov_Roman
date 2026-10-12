
# Цены напитков (рублей за порцию)
COFFEE_PRICE = 120
TEA_PRICE = 80
JUICE_PRICE = 100
WATER_PRICE = 50
LEMONADE_PRICE = 90

# Скидка 10% применяется по коду CAFE10
DISCOUNT_CODE = "CAFE10"
DISCOUNT_RATE = 0.10

print("╔══════════════════════════════════════╗")
print("║          ☕ МЕНЮ НАШЕГО КАФЕ         ║")
print("╚══════════════════════════════════════╝")
print(f"1. Кофе ☕       — {COFFEE_PRICE} руб.")
print(f"2. Чай 🍵        — {TEA_PRICE} руб.")
print(f"3. Сок 🧃        — {JUICE_PRICE} руб.")
print(f"4. Вода 💧       — {WATER_PRICE} руб.")
print(f"5. Лимонад 🥤    — {LEMONADE_PRICE} руб.")

choice = input("\nВыберите напиток (номер или название): ").strip().lower()

match choice:
    case "1" | "кофе":
        drink = "Кофе ☕"
        price = COFFEE_PRICE
    case "2" | "чай":
        drink = "Чай 🍵"
        price = TEA_PRICE
    case "3" | "сок":
        drink = "Сок 🧃"
        price = JUICE_PRICE
    case "4" | "вода":
        drink = "Вода 💧"
        price = WATER_PRICE
    case "5" | "лимонад":
        drink = "Лимонад 🥤"
        price = LEMONADE_PRICE
    case _:
        drink = None

if drink is None:
    print("❌ Ошибка: выберите напиток из меню (1–5 или название).")
else:
    try:
        quantity = int(input("Введите количество порций: "))

        if quantity <= 0:
            print("❌ Количество порций должно быть больше нуля.")
        else:
            # Выбираем правильную форму слова «порция».
            last_two = quantity % 100
            last_digit = quantity % 10

            match last_two:
                case 11 | 12 | 13 | 14:
                    portion_word = "порций"
                case _:
                    match last_digit:
                        case 1:
                            portion_word = "порция"
                        case 2 | 3 | 4:
                            portion_word = "порции"
                        case _:
                            portion_word = "порций"

            subtotal = price * quantity
            discount_code = input(
                f"Введите код скидки (или нажмите Enter, если его нет): "
            ).strip().upper()

            match discount_code:
                case "CAFE10":
                    discount = subtotal * DISCOUNT_RATE
                    discount_message = "Скидка 10% применена."
                case "":
                    discount = 0
                    discount_message = "Скидка не применялась."
                case _:
                    discount = 0
                    discount_message = "Код не распознан, скидка не применена."

            total = subtotal - discount

            print("\n" + "═" * 42)
            print("             🧾 КВИТАНЦИЯ")
            print("═" * 42)
            print(f"Напиток:              {drink}")
            print(f"Цена за порцию:       {price:.2f} руб.")
            print(f"Количество:           {quantity} {portion_word}")
            print(f"Сумма до скидки:      {subtotal:.2f} руб.")
            print(f"Скидка:               {discount:.2f} руб.")
            print(f"Статус скидки:        {discount_message}")
            print("─" * 42)
            print(f"ИТОГО К ОПЛАТЕ:       {total:.2f} руб.")
            print("Спасибо за заказ! ☺️")
            print("═" * 42)

    except ValueError:
        print("❌ Ошибка: количество порций нужно ввести целым числом.")

