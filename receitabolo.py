import math
a, b, c = [int(w) for w in input().split()]

farinha = math.floor(a / 2)
ovo = math.floor(b / 3)
leite = math.floor(c / 5)

bolos = min(farinha, ovo, leite)
print(bolos)