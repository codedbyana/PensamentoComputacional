
lista1 = []
lista2 = []

print("Digite 5 números para a primeira lista:")
for i in range(5):
    lista1.append(float(input(f"Número {i+1}: ")))

print("Digite 5 números para a segunda lista:")
for i in range(5):
    lista2.append(float(input(f"Número {i+1}: ")))

lista_unida = lista1 + lista2
print("Lista unida:", lista_unida)
