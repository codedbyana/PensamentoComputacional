
numeros = []
for i in range(10):
    n = float(input(f"Digite o {i+1}º número: "))
    numeros.append(n)

print("Maior número:", max(numeros))
print("Menor número:", min(numeros))
