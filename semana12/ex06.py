
lista_b = []

print("Digite 5 números para a primeira lista:")
for i in range(5):
    lista_a.append(float(input(f"Número {i+1}: ")))

print("Digite 5 números para a segunda lista:")
for i in range(5):
    lista_b.append(float(input(f"Número {i+1}: ")))

lista_comum = [x for x in lista_a if x in lista_b]
print("Elementos comuns:", lista_comum)
