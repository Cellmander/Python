inicio_aulas = {'0730':0, '0820':1, '0910':2, '1010':3, '1100':4, '1330':5, '1420':6, '1510':7, '1620':8, '1710':9, '1830':10, '1920':11, '2020':12, '2110':13}
quadro_horarios = [[''] * 6 for i in range(len(inicio_aulas))]

qtd_disciplinas = int(input())
choques = []

for j in range(qtd_disciplinas):
    disciplina, *horarios = input().split()
    
    for horario in horarios:
        col = int(horario[0]) - 2
        lin = inicio_aulas[horario[1:5]]
        n_aulas = int(horario[-1])
        
        for i in range(n_aulas):
            if quadro_horarios[int(lin)+i][col] != '':
                if choques == []:
                    choques.append( [quadro_horarios[int(lin)+i][col], disciplina])
            else:
                quadro_horarios[int(lin)+i][col] = disciplina
print(str(choques))