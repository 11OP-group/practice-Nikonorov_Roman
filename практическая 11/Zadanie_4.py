num = int(input("Введите натуральное число: "))

last_digit = num % 10

count_3 = 0
count_last = 0
count_even = 0
sum_greater_5 = 0
prod_greater_7 = 1
count_0_and_5 = 0

while num > 0:
    digit = num % 10

    if digit == 3:
        count_3 += 1

    if digit == last_digit:
        count_last += 1

    if digit % 2 == 0:
        count_even += 1

    if digit > 5:
        sum_greater_5 += digit

    if digit > 7:
        prod_greater_7 *= digit

    if digit == 0 or digit == 5:
        count_0_and_5 += 1

    num //= 10

print(count_3)
print(count_last)
print(count_even)
print(sum_greater_5)
print(prod_greater_7)
print(count_0_and_5)