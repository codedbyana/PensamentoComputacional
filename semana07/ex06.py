
 #Leia vários números inteiros fornecidos pelo usuário 
 # até que seja digitado um valor negativo. Calcule a média apenas 
 # dos números positivos.
 
soma = 0
cont = 0
while True:

    n = int(input("Forneça um número:"))
    if n < 0:
        break
    soma += n
    cont += 1
if cont > 0:
    media = soma / cont 
    print("a media dos numeros positivos é")

else:
    print("nenhum número positivo foi digitado")
