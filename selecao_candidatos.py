listaregras = []
while True:
    regra = input().split() #entrada da regra
    if int(regra[0]) == 0 and int(regra[1]) == 0: #avalia o parametro de parada
        break
    ordem = regra[3].split(';') #separa a ordem de seleção por ponto e vírgula
    listaregras.append(regra)

vagas = {}
categoria = listaregras[0][3].split(',')
for ordem_selecao in categoria:
    vagas[ordem_selecao] = int(input()) #cria um dicionário com o número de vagas por categoria

n_candidatos = int(input())
lista_candidatos = []
for i in range(n_candidatos):
    candidato = input().split()
    lista_candidatos.append(candidato)
    