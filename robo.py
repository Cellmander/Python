lin, col = [int (x) for x in input().split()]

lin_inicial, col_inicial = [int (x) for x in input().split()] 
matriz = [[int (x) for x in input().split()] for _ in range(lin)]
lin_inicial -= 1
col_inicial -= 1

while True:
    for delta_lin, delta_col in ( (-1,0), (1,0), (0, -1), (0,1)):
        nova_lin = lin_inicial + delta_lin
        nova_col = col_inicial + delta_col
        if nova_lin in range(0, lin) and nova_col in range(0, col) and matriz[nova_lin][nova_col] == 1:
            matriz[lin_inicial][col_inicial] = 0
            lin_inicial = nova_lin
            col_inicial = nova_col
            break
    else:
        break
print(lin_inicial + 1, col_inicial + 1)