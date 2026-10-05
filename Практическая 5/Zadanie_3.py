USD_TO_RUB = 95.50


def convert_usd_to_rub(amount_usd):
    """Переводит сумму из долларов в рубли."""
    return amount_usd * USD_TO_RUB


print("Введите сумму в долларах:")
amount_usd = float(input())

amount_rub = convert_usd_to_rub(amount_usd)

print(f"Сумма в рублях: {amount_rub:.2f} руб.")