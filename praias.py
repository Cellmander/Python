n_praias = int(input())

mais_distante = -1
praia_mais_distante = ''
qtd_praias = 0
soma = 0

for i in range(n_praias):
    praia, distancia = input().split(';')
    distancia = int(distancia)
    if distancia > mais_distante:
        mais_distante = distancia
        praia_mais_distante = praia
    if distancia >= 15 and distancia <= 20:
        qtd_praias += 1
    soma += distancia
    
media_distancia = soma / n_praias
print(f'{praia_mais_distante};{qtd_praias};{media_distancia:.1f}')