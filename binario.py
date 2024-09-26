numero = int(input())

if numero == 0:
    binario = '0'
else:
    binario = ''
    while numero > 0:
        binario = str(numero % 2) + binario
        numero = numero // 2

print(binario)
        