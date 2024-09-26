import math
comprimento_estrada, distancia_pedagio = [float(w) for w in input().split()]
custo_km, valor_pedagio = [float(w) for w in input().split()]

consumo = comprimento_estrada * custo_km
quantidade_pedagios = math.floor(comprimento_estrada/distancia_pedagio)
custo_pedagios = quantidade_pedagios * valor_pedagio
custo_total = consumo + custo_pedagios
print(round(custo_total))

