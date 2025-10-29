
def calcular_media(n1, n2):
    return (n1 + n2) / 2

def verificar_aprovacao(media):
    if media >= 7:
        print("Aluno aprovado!")
    else:
        print("Aluno reprovado!")

# Programa principal
nota1 = float(input("Digite a primeira nota: "))
nota2 = float(input("Digite a segunda nota: "))

media = calcular_media(nota1, nota2)
print(f"Média: {media:.2f}")
verificar_aprovacao(media)
