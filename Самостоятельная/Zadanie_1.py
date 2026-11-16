prices = [100, 50, 200, 150]

max_price = max(prices)
min_price = min(prices)
print("Самая дорогая цена:", max_price)
print("Самая дешёвая цена:", min_price)

average_price = sum(prices) / len(prices)
print("Средняя цена:", average_price)

print(*prices, sep=", ")