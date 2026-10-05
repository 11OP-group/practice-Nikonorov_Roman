print("Введите вес и рост через пробел:")
weight, height = map(float, input().split())

bmi = weight / (height * height)

print(f"Ваш ИМТ: {bmi:.1f}")2