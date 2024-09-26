import math

num = float(input())
sinal = '+' if num >= 0 else '-'
num = abs(num)
exp = math.floor(math.log10(num))
esquerda = num / 10 ** exp

print(f"{sinal}{esquerda:.4f}E{exp:+03}")