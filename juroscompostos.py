import math
capital = float(input('valor:'))
meses = int(input('meses:'))
taxa = float(input('taxa:'))

juros = capital * ((1 + (taxa/100))**meses)

print(round(juros, 2))