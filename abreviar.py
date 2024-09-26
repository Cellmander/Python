nome = input().split()

for sobrenome in range(1, len(nome)-1):
    if len(nome[sobrenome]) > 3:
        nome[sobrenome] = nome[sobrenome][0] + '.'
n_completo = ''
for nomes in nome:
    n_completo += nomes + ' '
print(n_completo.strip())