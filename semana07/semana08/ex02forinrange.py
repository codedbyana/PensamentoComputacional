#Faça um algoritmo que peça dois números para o usuário (o primeiro sempre será menor que o segundo), posteriormente apresente somente os números pares no intervalo entre os dois número. 
while True:
    n1 = int(input("digite o primeiro numero (deve ser baixo):"))
    n2 = int(input("Digite o segundo número:"))
   
    for i in range (n1, n2):
        if i % 2 == 0:
            print("Numeros pares", i )
    else:
     print("Valor 1 deve ser menor")
        
