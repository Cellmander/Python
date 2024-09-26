n1 = int(input())
n2 = int(input())
n3 = int(input())
n4 = int(input())
n5 = int(input())

def par(n):
    if n == 0:
        return 0
    else:
        return n % 2

impares = 0
pares = 0
if par(n1) == 0:
    pares += 1
else:
    impares += 1
if par(n2) == 0:
    pares += 1
else:
    impares += 1
if par(n3) == 0:
    pares += 1
else:
    impares += 1
if par(n4) == 0:
    pares += 1
else:
    impares += 1
if par(n5) == 0:
    pares += 1
else:
    impares += 1
    
positivo = 0
negativo = 0
if n1-0 > 0:
    positivo += 1
elif n1-0 < 0:
    negativo += 1
else:
    negativo += 0
if n2-0 > 0:
    positivo += 1
elif n2-0 < 0:
    negativo += 1
else:
    negativo += 0
if n3-0 > 0:
    positivo += 1
elif n3-0 < 0:
    negativo += 1
else:
    negativo += 0
if n4-0 > 0:
    positivo += 1
elif n4-0 < 0:
    negativo += 1
else:
    negativo += 0
if n5-0 > 0:
    positivo += 1
elif n5-0 < 0:
    negativo += 1
else:
    negativo += 0

    
print(f'{pares} valor(es) par(es)')
print(f'{impares} valor(es) impar(es)')
print(f'{positivo} valor(es) positivo(s)')
print(f'{negativo} valor(es) negativo(s)')