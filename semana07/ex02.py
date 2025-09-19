

n = int(input('digite um numero inteiro positivo:'))
 
print(f"divisores de numero {n} ")
contagem = 0

for i in range( 1, n + 1 ):
    if n % i == 0:
        print (i)
        contagem += 1
        
        
print(f"Total de divisores: {contagem}")
