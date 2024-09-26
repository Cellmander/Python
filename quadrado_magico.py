N = int(input())
matriz = [[int (x) for x in input().split()] for x in range(N)]

eh_magico = True
valor_ref, diag_prin, diag_sec, c = sum(matriz[0]), [], [], N-1
for i in range(N):
    soma_col = 0
    if sum(matriz[i]) != valor_ref:
        eh_magico = False
        break
    diag_prin.append(matriz[i][i])
    diag_sec.append(matriz[i][c])
    c -= 1
    for j in range(N):
        soma_col += matriz[j][i]
    if soma_col != valor_ref:
        eh_magico = False
        break
diag_sec = sum(diag_sec) == valor_ref
diag_prin = sum(diag_prin) == valor_ref
print(eh_magico and diag_prin and diag_sec)
        
