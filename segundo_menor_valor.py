import math

tamanho_sequencia = int(input())
menor_valor = math.inf

for i in range(1, tamanho_sequencia+1):
    numero = int(input())
    if numero < menor_valor:
        segundo_valor = menor_valor
        menor_valor = numero
    elif numero < segundo_valor:
        segundo_valor = numero
        
print(segundo_valor)