consumo = int(input())
valor_30k = 30*0.09556
valor_100k = 70*0.16698
valor_200k = 100*0.25052

if consumo <= 30:
    valor_pago = consumo * 0.09556
elif consumo <= 100:
    excedente = consumo - 30
    valor_pago = valor_30k + excedente*0.16698
elif consumo <= 200:
    excedente = consumo - 100
    valor_pago = valor_30k + valor_100k + excedente*0.25052
else:
    excedente = consumo - 200
    valor_pago = valor_30k + valor_100k + valor_200k + excedente*0.27836
    
print(f'{valor_pago:.2f}')
    