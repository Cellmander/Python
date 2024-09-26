import math
tempo = float(input())
minuto = tempo / 60
segundos = round((minuto - math.floor(minuto))*60)
minuto = math.floor(minuto)
hora = minuto / 60
minuto = round((hora - math.floor(hora))*60)
hora = math.floor(hora)

print(f'{hora}:{minuto}:{segundos}')

