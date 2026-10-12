
print("Введите рейтинг продукта от 1 до 10:")
rating = int(input())

match rating:
    case 9 | 10:
        description = "Отличный"
        emoji = "🌟"
        recommendation = "Рекомендую"
    case 7 | 8:
        description = "Хороший"
        emoji = "😊"
        recommendation = "Рекомендую"
    case 5 | 6:
        description = "Средний"
        emoji = "😐"
        recommendation = "Можно попробовать"
    case 1 | 2 | 3 | 4:
        description = "Плохой"
        emoji = "👎"
        recommendation = "Не рекомендую"
    case _:
        description = "Некорректный рейтинг"
        emoji = "❓"
        recommendation = "Введите число от 1 до 10"

print(f"Оценка: {description} {emoji}")
print(f"Рекомендация: {recommendation}")
