
tentativas = 0
idade = -1

while idade < 0 or idade > 120:
    idade = int(input('digite uma idade entre 0 e 120:'))
    tentativas += 1
      

print(f"idade confitmada: {idade}")
print(f"total de tentetivas: {tentativas}")
