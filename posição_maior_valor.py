import math

tamanho_sequencia = int(input())
maior_valor = -math.inf

for i in range(1, tamanho_sequencia+1):
    numero = int(input())
    if numero > maior_valor:
        maior_valor = numero
        posição = i
        
print(maior_valor, posição)