O = input()
matriz = [[float(input()) for _ in range(12)] for x in range(12)]

soma, elementos, c = 0, 0, len(matriz)-1
for p in range(0, 6):
    soma += sum(matriz[p][p+1:c])
    elementos += len(matriz[p][p+1:c])
    c -= 1
if O == 'M':
    media = soma / elementos
    print(f'{media:.1f}')
else:
    print(f'{soma:.1f}')