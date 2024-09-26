lin, col = [int (x) for x in input().split()]
matriz = [[input().split()] for _ in range(lin)]
instrucoes = []
primeiro_passo = False
direcoes = dict()

for i in range(lin):
    if 'X' in set(matriz[i][0]):
        lin_inicial, col_inicial = [i, matriz[i][0].index('X')]
        break
while True:
    for delta_lin, delta_col in ( (-1,0), (1,0), (0, -1), (0,1)):
        nova_lin = lin_inicial + delta_lin
        nova_col = col_inicial + delta_col
        if nova_lin in range(0, lin) and nova_col in range(0, col) and matriz[nova_lin][nova_col] == 0:
            matriz[lin_inicial][col_inicial] = 1
            if primeiro_passo:
                
            in_inicial = nova_lin
            col_inicial = nova_col
            break