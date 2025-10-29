def somaImposto(taxaImposto, custo):
    custo_final = custo + (custo * (taxaImposto / 100))
    return custo_final

# Programa principal
taxa = float(input("Digite a taxa de imposto (%): "))
valor = float(input("Digite o custo do item: "))

print(f"Valor com imposto: R${somaImposto(taxa, valor):.2f}")
