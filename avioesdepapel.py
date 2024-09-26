competidores, folhas_diretora, folhas_juiz = [int(w) for w in input() .split()]

necessario = folhas_juiz*competidores

if folhas_diretora >= necessario:
    print('S')
else:
    print('N')