#Escreva um programa que imprima na tela a sequência de Fibonacci até o décimo termo utilizando o laço de repetição for.

anterior = 0
atual = 1


print("anterior")
print("atual")

for i in range (2,10):
   proximo = anterior + atual
   print(proximo)
   anterior = atual
   atual = proximo
