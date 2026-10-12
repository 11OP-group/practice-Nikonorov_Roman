import random

print("╔══════════════════════════════════════╗")
print("║        📦 ОТСЛЕЖИВАНИЕ ЗАКАЗА        ║")
print("╚══════════════════════════════════════╝")
print("Доступные статусы: pending, processing, shipped, delivered, cancelled")

status = input("Введите код статуса заказа: ").strip().lower()

match status:
    case "pending":
        title = "В ожидании"
        description = "Заказ создан и ожидает начала обработки."
        emoji = "⏳"
        waiting_time = random.randint(10, 60)
        time_unit = "мин."
    case "processing":
        title = "В обработке"
        description = "Заказ собирают и подготавливают к отправке."
        emoji = "⚙️"
        waiting_time = random.randint(1, 24)
        time_unit = "ч."
    case "shipped":
        title = "Отправлено"
        description = "Заказ передан службе доставки."
        emoji = "🚚"
        waiting_time = random.randint(1, 5)
        time_unit = "дн."
    case "delivered":
        title = "Доставлено"
        description = "Заказ доставлен получателю."
        emoji = "✅"
        waiting_time = 0
        time_unit = "ч."
    case "cancelled":
        title = "Отменено"
        description = "Заказ отменён. Дальнейшая обработка не выполняется."
        emoji = "❌"
        waiting_time = 0
        time_unit = "ч."
    case _:
        title = None

if title is None:
    print("❌ Неизвестный статус. Проверьте написание и попробуйте снова.")
else:
    print("\n" + "─" * 48)
    print(f"📦 Статус: {title} {emoji}")
    print(f"📝 Описание: {description}")
    if waiting_time == 0:
        print("⏱️ Время ожидания: не требуется.")
    else:
        print(f"⏱️ Примерное время: {waiting_time} {time_unit}")
    print("─" * 48)
