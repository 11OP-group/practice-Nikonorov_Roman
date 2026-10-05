TAX_RATE = 0.13

print("Введите годовой доход:")
income = float(input())

tax = income * TAX_RATE
money_after_tax = income - tax

print(f"Общая сумма дохода: {income:,.2f} руб.")
print(f"Сумма налога: {tax:,.2f} руб.")
print(f"Сумма на руки: {money_after_tax:,.2f} руб.")