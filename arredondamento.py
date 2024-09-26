import math
nota = float(input())

decimo = nota - math.floor(nota)
nota = nota - decimo

if decimo < 0.25:
    decimo = 0
elif decimo >= 0.25 and decimo < 0.5:
    decimo = 0.5
elif decimo == 0.5:
    decimo = decimo
elif decimo > 0.5 and decimo < 0.75:
    decimo = 0.5
elif decimo >= 0.75:
    decimo = 1
    
nota = nota + decimo
print(nota)