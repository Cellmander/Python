valor_veiculo = float(input())
classe = input()
procedencia = input()
idade = int(input())

if procedencia == 'nacional':
    valor_pago = valor_veiculo * 0.1
elif procedencia == 'estrangeira':
    valor_pago = valor_veiculo * 0.15
if classe == 'A':
    desconto_classe = valor_pago * 0.3
elif classe == 'B':
    desconto_classe = valor_pago * 0.2
elif classe == 'C':
    desconto_classe = valor_pago * 0.1
elif classe == 'D':
    desconto_classe = valor_pago * 0.05
elif classe == 'E':
    desconto_classe = 0
if idade > 24:
    desconto_idade = valor_pago * 0.1
else:
    desconto_idade = 0
premio_seguro = valor_pago - desconto_classe - desconto_idade
print(f'{premio_seguro:.2f}')