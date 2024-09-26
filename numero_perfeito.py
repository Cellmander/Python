n = int(input())

for i in range(n):
    numero = int(input())
    soma = 0
    x = 'eh perfeito'
    for z in range(1, int(numero/2)+1):
        if numero % z == 0:
            soma += z
    if soma != numero:
        x = 'nao eh perfeito'
        
    print(f'{numero} {x}')