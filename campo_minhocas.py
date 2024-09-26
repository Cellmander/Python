lin, col = [int (x) for x in input().split()]

maior_valor = -1
campo = [[int (x) for x in input().split()] for _ in range(lin)]

for i in range(lin):
    if sum(campo[i]) > maior_valor:
        maior_valor = sum(campo[i])
    soma = 0
    if i < col:
        for j in range(lin):
            soma += campo[j][i]
        if soma > maior_valor:
            maior_valor = soma
print(maior_valor)
