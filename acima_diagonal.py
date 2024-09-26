O = input()
matriz = [[float(input()) for _ in range(12)] for x in range(12)]
c, soma, elementos = 11, 0, 0
for i in range(0, 12, 1):
    soma += sum(matriz[i][0:c])
    elementos += len(matriz[i][0:c])
    c -= 1
if O == 'M':
    media = soma / elementos
    print(f'{media:.1f}')
else:
    print(f'{soma:.1f}')