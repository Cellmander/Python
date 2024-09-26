def multiplica_matrizes(a, b):
    ''' Multiplica duas matrizes a(m,n) e b(n,p), retornando c(m,p) '''
    m = len(a) # o número de linhas de a
    n = len(b) # o número de linhas de b
    p = len(b[0]) # o número de colunas de b

    c = [] # inicia com uma matriz vazia
    for i in range(m):
        c.append([0] * p) # insere a linha i
        for j in range(p):  # calcula os valores da linha i
            soma = 0
            for k in range(n):
                soma += a[i][k] * b[k][j]
            c[i][j] = soma

    return c


ma = [[2,3,1],[0,1,2]]
mb = [[7,9,5,7],[8,6,4,6], [2,3,3,3]]
mc = multiplica_matrizes(ma,mb)