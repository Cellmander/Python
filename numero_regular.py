numero = int(input())

if numero == 1:
    numero = 0
else:
    while numero > 1:
        if numero % 2 == 0:
            numero = numero / 2
        elif numero % 3 == 0:
            numero = numero / 3
        elif numero % 5 == 0:
            numero = numero / 5
        else:
            numero = 0
            break
        
if numero == 1:
    print(True)
else:
    print(False)
        