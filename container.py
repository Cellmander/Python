import math
a, b, c = [int(w) for w in input().split()]
x, y, z = [int(w) for w in input().split()]

largura = math.floor(x/a)
comprimento = math.floor(y/b)
altura = math.floor(z/c)
quantidade_container = math.floor(largura*comprimento*altura)

print(round(quantidade_container))