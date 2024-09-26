O = input()

matriz = []
for x in range(12):
    linha = [float(input()) for _ in range(12)]
    matriz.append(linha)

c = 1
soma = 0
elementos = 0
for i in range(1, 12, 1):
        soma += sum(matriz[i][0:c])
        elementos += len(matriz[i][0:c])
        c += 1

if O == 'M':
    media = soma / elementos
    print(f'{media:.1f}')
else:
    print(f'{soma:.1f}')