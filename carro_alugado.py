dias = int(input())
quilometragem = float(input())

valor_uso = 45 * dias
km_dia = quilometragem / dias

if km_dia > 60:
    excedente = km_dia - 60
    valor_km = (excedente * 0.5)*dias
else:
    valor_km = 0
    
valor_total = valor_uso + valor_km
print(valor_total)