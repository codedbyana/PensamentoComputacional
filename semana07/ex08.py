


#O programa deve solicitar ao usuário um número 
# inteiro positivo e verificar se ele é um número perfeito. 
# Um número é dito perfeito quando a soma de todos os seus divisores positivos, 
# excluindo ele mesmo, é igual ao próprio número (por exemplo, 6 = 1 + 2 + 3). 
# Mostre todos os divisores usados no cálculo e, ao final, diga se o número é ou
#  não perfeito.


soma = 0
n = int(input("digite um numero inteiro:"))

print(f"divisores de {n} usados no calculo:")

for i in range (1, n):
    if n % i == 0:
        print(i, end = " ")
        soma += i
print("\nSoma dos divisores:", soma )
if soma == n:
    print(n, "é um numero perfeito!")
else:
    print(n, "não é um numero perfeito!")
