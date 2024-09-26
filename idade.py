import math
idade = int(input())

ano = math.floor(idade / 365)
meses = math.floor((idade-365*ano)/30)
dias = (idade-365*ano)-30*meses

print(f'{ano} ano(s)')
print(f'{meses} mes(es)')
print(f'{dias} dia(s)')