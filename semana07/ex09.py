

#O programa deve pedir ao usuário um número
#inteiro positivo N e mostrar os N primeiros números da 
# sequência de Fibonacci. Essa sequência começa com 0 e 1.
#  A partir daí, cada número é a soma dos dois anteriores 
# (exemplo: 0, 1, 1, 2, 3, 5, 8…). O programa deve exibir um número por linha e,
# no final, mostrar qual foi o último número apresentado.

soma = 0
n = int(input("digite um numero inteiro:"))
a , b = 0 , 1
print("sequencia de fibonacci:")

for i in range (n):
    print("a")
    a , b = b , a + b 

    print("ultimo número exibido:", a - b)
