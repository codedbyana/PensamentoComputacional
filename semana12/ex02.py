
temperaturas = [30, 22, 25, 28, 31, 27, 29]


for i in range(len(temperaturas)):
    if temperaturas[i] < 25:
        temperaturas[i] += 5

print("Temperaturas atualizadas:", temperaturas)
