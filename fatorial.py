numero = int(input())

for i in range(numero-1, 1, -1):
    if i != 0:
        fatorial = i * numero
        numero = fatorial

print(numero)