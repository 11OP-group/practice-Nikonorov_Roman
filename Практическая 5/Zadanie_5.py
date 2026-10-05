B5000 = 5000
B2000 = 2000
B1000 = 1000
B500 = 500
B200 = 200
B100 = 100

print("Введите сумму для снятия:")
amount = int(input())

count_5000 = amount // B5000
amount = amount % B5000

count_2000 = amount // B2000
amount = amount % B2000

count_1000 = amount // B1000
amount = amount % B1000

count_500 = amount // B500
amount = amount % B500

count_200 = amount // B200
amount = amount % B200

count_100 = amount // B100

print(f"Купюр 5000: {count_5000}")
print(f"Купюр 2000: {count_2000}")
print(f"Купюр 1000: {count_1000}")
print(f"Купюр 500: {count_500}")
print(f"Купюр 200: {count_200}")
print(f"Купюр 100: {count_100}")