# Заранее вычисляем пятые степени чисел от 1 до 150, чтобы программа работала быстро
pows = [i ** 5 for i in range(151)]

found = False

# Перебираем a <= b <= c <= d, чтобы не проверять одинаковые комбинации
for a in range(1, 151):
    for b in range(a, 151):
        for c in range(b, 151):
            for d in range(c, 151):
                sum_abcd = pows[a] + pows[b] + pows[c] + pows[d]

                # Если сумма уже больше 150^5, дальше проверять нет смысла
                if sum_abcd > pows[150]:
                    break

                # Проверяем, является ли сумма пятой степенью какого-то числа e
                e = int(round(sum_abcd ** (1 / 5)))
                if e <= 150 and pows[e] == sum_abcd:
                    print(f"a = {a}, b = {b}, c = {c}, d = {d}, e = {e}")
                    print(f"Сумма a + b + c + d + e = {a + b + c + d + e}")
                    found = True
                    break
            if found:
                break
        if found:
            break
    if found:
        break





