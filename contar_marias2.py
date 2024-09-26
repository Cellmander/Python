qtd_nomes = int(input())
marias = 0
for _ in range(qtd_nomes):
    nome = input()
    nome += ' '
    nome = nome.lower()
    if nome.count('maria') != 0:
        indice = nome.index('maria')
        branco = nome.count(' ', indice, indice + 6)
        if branco != 0:
            marias += nome.count('maria')
    
print(marias)