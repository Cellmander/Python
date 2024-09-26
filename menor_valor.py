import math

i = 1
while True:
    a = math.factorial(i)
    b = i ** 10
    if a > b:
        valor = i
        break
    i += 1
print(valor)