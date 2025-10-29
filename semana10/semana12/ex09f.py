
#Faça uma função calcular_desconto(valor) que aplique descontos conforme a faixa:
# até R$100 → 5%
# de R$101 a R$500 → 10%
# acima de R$500 → 15%
# Retorne o valor final e mostre o desconto aplicado.

def calcular_desc (valor):
    if valor <= 100:
        desconto = valor * 0.95
    elif valor <= 500:
        desconto = valor * 0.90
    else:
       desconto = valor * 0.85

    print(f"Valor com desconto: R${desconto:.2f}")



def main():
    valor = int(input("Digite o valor:"))
    calcular_desc(valor)

    
main()
