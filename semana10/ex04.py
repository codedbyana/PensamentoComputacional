def calcular_valor(quantidade):
    if quantidade <= 12:
        preco = 0.40
    else:
        preco = 0.25
    return quantidade * preco

# Programa principal
qtd = int(input("Digite a quantidade de laranjas: "))
total = calcular_valor(qtd)
print(f"Valor total da compra: R${total:.2f}")
