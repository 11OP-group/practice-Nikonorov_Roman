FUEL_PRICE = 49.5


def calculate_fuel(distance, fuel_consumption):
    """Рассчитывает количество бензина для поездки."""
    return distance * (fuel_consumption / 100)


def calculate_cost(fuel_amount):
    """Рассчитывает стоимость бензина."""
    return fuel_amount * FUEL_PRICE


print("Какое расстояние (км)?")
distance = float(input())

print("Сколько литров на 100 км ест машина?")
fuel_consumption = float(input())

fuel_amount = calculate_fuel(distance, fuel_consumption)
total_cost = calculate_cost(fuel_amount)

print(f"Нужно бензина: {fuel_amount:.2f} л")
print(f"Стоимость: {total_cost:.2f} руб.")