espaço = False
while True:
    dim = int(input())
    if dim == 0:
        break
    matriz = []
    n_linha = 1

    # Criação da matriz inicial
    for l in range(dim):
        linha = [n_linha] * dim
        n_linha = 2
        matriz.append(linha)

    # Ajuste dos valores na matriz
    for i in range(dim):
        for c in range(1, dim):
            matriz[i][c] = matriz[i][c-1] * 2

    # Determinação do maior número da matriz
    maior_numero = max(max(linha) for linha in matriz)
    T = len(str(maior_numero))

    if espaço:
        print()
    # Impressão da matriz formatada usando o operador *
    for linha in matriz:
        linha_formatada = ' '.join(f'{num:>{T}}' for num in linha)
        print(linha_formatada)
