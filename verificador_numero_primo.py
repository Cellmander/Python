import math
numero = int(input())

if numero == 2:
    eh_primo = True
elif numero % 2 == 0 or numero == 1:
    eh_primo = False
else:
    eh_primo = True
    raiz = int(math.sqrt(numero))
    for i in range(3, raiz + 1, 2):
        if numero % i == 0:
            eh_primo = False
            break
        
print(eh_primo)