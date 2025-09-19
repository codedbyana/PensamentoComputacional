'''Leia dois inteiros A e
B (com A ≤ B) e exiba, no intervalo fechado de A até B, apenas os números que são múltiplos de 3 e não são múltiplos de 5. Informe também quantos números foram exibidos.
a = int(input("Digite o valor de A:"))
b = int(input("digite o valor de B:"))
'''
cont = 0

print("numeros que são multiplos de 3 e não de 5 no intervalo:")

for i in range (a , b + 1):
    if i % 3 == 0 and i % 5 != 0:
        print(i , end=" ")
        cont += 1
        print("\nTotal de números exibidos:", cont)
