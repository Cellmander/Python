def opera_matriz(L, T):
    if T == 'S':   
        return sum(matriz[L])
    else:
        return sum(matriz[L])/len(matriz)

L = int(input())
T = input()

matriz = []
for x in range(12):
    linha = [float(input()) for _ in range(12)]
    matriz.append(linha)
    
print(f'{opera_matriz(L, T):.1f}')
