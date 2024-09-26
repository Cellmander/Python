while True:
    n = int(input())
    if n == 0:
        break
    
    matriz = []
    for i in range(n):
        linha = []
        for j in range(n):
            linha.append(2**(j+i))
        matriz.append(linha)
        
    