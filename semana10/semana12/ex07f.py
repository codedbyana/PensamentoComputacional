

#Crie uma função avaliar_aluno(n1, n2, n3) que receba as três notas de um aluno, calcule a média e retorne o conceito:
# Média < 4: Reprovado
# 4 ≤ Média < 6: Recuperação
# Média ≥ 6: Aprovado	
# As notas devem ser passadas por parâmetros.

def av_aluno (n1, n2, n3):
    media = (n1 + n2 + n3) / 3
    if media < 4:
        return f"Média: {media:.2f} - Reprovado!"
    elif media < 6:
         return f"Média: {media:.2f} - Recuperação!"
    else:
        return f"Média: {media:.2f} - Aprovado!"
    

nota1 = float(input("Digite a primeira nota:"))
nota2 = float(input("Digite a segunda nota:"))
nota3 = float(input("Digite a terceira nota:"))
    
resultado = av_aluno(nota1, nota2, nota3)
print(resultado)
