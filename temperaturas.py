escala = input()
temperatura = float(input())
escala_destino = input()

if escala == 'c':
    if escala_destino == 'f':
       temperatura = ((temperatura / 5) * 9) + 32
    elif escala_destino == 'k':
        temperatura = temperatura + 273.15
    elif escala_destino == 'r':
        temperatura = temperatura * 9/5 + 491.67
elif escala == 'f':
    if escala_destino == 'c':
        temperatura = (temperatura - 32) * 5/9
    elif escala_destino == 'k':
        temperatura = (temperatura - 32) * 5/9 + 273.15
    elif escala_destino == 'r':
        temperatura = temperatura + 459.67
elif escala == 'k':
    if escala_destino == 'c':
        temperatura = temperatura - 273.15
    elif escala_destino == 'f':
        temperatura = ((temperatura - 273.15) * 9/5) + 32
    elif escala_destino == 'r':
        temperatura = (temperatura-273.15) * 1.8 + 491.67
elif escala == 'r':
    if escala_destino == 'c':
        temperatura = (temperatura - 491.67) * 5/9
    elif escala_destino == 'f':
        temperatura = temperatura - 459.67
    elif escala_destino == 'k':
        temperatura = temperatura / 1.8
        
print(temperatura)