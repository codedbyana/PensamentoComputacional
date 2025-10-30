
idades = []
while True:
    idade = int(input("Digite uma idade (0 para sair): "))
    if idade == 0:
        break
    idades.append(idade)

if len(idades) > 0:
    media = sum(idades) / len(idades)
    print("Média das idades:", media)
else:
    print("Nenhuma idade foi digitada.")
