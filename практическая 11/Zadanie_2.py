for b in range(11):
    for k in range(21):
        for t in range(201):
            if 10 * b + 5 * k + 0.5 * t == 100 and b + k >= 1:
                print("Быков:", b ,  "Коров:", k, "Телята:", t)

