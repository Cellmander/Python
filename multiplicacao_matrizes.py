def multiplica_matrizes(I, J):
    soma = 0
    for k in range(dms_matriz):
        soma += A[I-1][k] * B[k][J-1] 
    return soma
   
dms_matriz = int(input())
p, q, r, s, x, y = [int(t) for t in input().split()]

A, B, col = [], [], []
for i in range(dms_matriz):
    for j in range(dms_matriz):
        valor = (p * (i+1) + q * (j+1)) % x
        col.append(valor)
    A.append(col)
    col = []
for i in range(dms_matriz):
    for j in range(dms_matriz):
        valor = (r * (i+1) + s * (j+1)) % y
        col.append(valor)
    B.append(col)
    col = []
I, J = [int(t) for t in input().split()]
print(multiplica_matrizes(I, J))