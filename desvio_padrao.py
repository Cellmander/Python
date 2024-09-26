import math
n = int(input())
valores = []
somatorio = []

for _ in range(n):
    numero = float(input())
    valores.append(numero)
media = sum(valores)/len(valores)
for numero in valores:
    somatorio.append((numero - media) ** 2)

resultado = math.sqrt(sum(somatorio)/(n-1)) 
print(resultado)