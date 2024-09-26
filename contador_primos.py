import math
x = int(input())
y = int(input())
contador = 0

for i in range(x, y+1):
    contador += 1
    if i == 2:
        contador += 0
    elif i % 2 == 0 or i == 1:
        contador -= 1
    else:
        raiz = int(math.sqrt(i))
        for z in range(3, raiz+1, 2):
            if i % z == 0:
                contador -= 1
                break
                
print(contador)