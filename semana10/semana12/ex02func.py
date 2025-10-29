#Faça uma função soma(a, b) que receba dois 
# números como parâmetros e retorne o resultado da soma. No programa principal, 
# solicite dois números ao usuário e exiba o resultado chamando a função.

def soma (a,b):
    return a+b

numero1 = float(input("Digite o primeiro numero:"))
numero2 = float(input("Digite o segundo número:"))

resultado = soma(numero1, numero2)
print(f"A soma de {numero1}+ {numero2} é = {resultado}")
