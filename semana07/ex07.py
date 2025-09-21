
#Solicite um número inteiro N e 
#exiba os N primeiros múltiplos de 9, mostrando também a soma 
# desses múltiplos ao final.

soma = 0

n = int(input("digite um numero inteiro positivo:"))

for i in range (1, n + 1):
    multiplo = 9 * i 
    print (multiplo)
    soma += multiplo

print("sima dos", n , "Primeiros multiplos de 9:", soma )
