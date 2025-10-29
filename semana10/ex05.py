def calcular_media(notas):
    return sum(notas) / len(notas)

def situacao(media):
    if media >= 7:
        return "Aprovado"
    elif media >= 4:
        return "Recuperação"
    else:
        return "Reprovado"

def exibir_resultado(media, status):
    print(f"Média: {media:.2f} - Situação: {status}")

# Programa principal
notas = [float(input(f"Digite a {i+1}ª nota: ")) for i in range(5)]
media = calcular_media(notas)
status = situacao(media)
exibir_resultado(media, status)
