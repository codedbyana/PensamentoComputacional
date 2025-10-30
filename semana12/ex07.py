
numeros = []
for i in range(10):
    n = int(input(f"Digite o {i+1}º número: "))
    numeros.append(n)

pares = [n for n in numeros if n % 2 == 0]
impares = [n for n in numeros if n % 2 != 0]

print("Números pares:", pares)
print("Números ímpares:", impares)
