#Crie um programa que calcule e exiba na tela a média aritmética de um conjunto de 10 números lidos do usuário utilizando o laço de repetição for.


numero = 0
for i in range (1,11):
    pessoas = int(input("Digite um número:"))
    numero += pessoas
    media = numero / 10
print("media", media)
