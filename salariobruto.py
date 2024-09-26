hora = float(input())
hora_extra = float(input())
valor_hora = 2500 / 200
extra = (valor_hora * (20/100) + valor_hora) * hora_extra

salario_bruto = (hora * valor_hora) + extra
inss = salario_bruto * 0.09
imposto = salario_bruto * 0.13
salario_liquido = salario_bruto - inss - imposto

print(f'- Salário Bruto : R$ {salario_bruto:.2f}')
print(f'- IR (13%) : R$ {imposto:.2f}')
print(f'- INSS (9%) : R$ {inss:.2f}')
print(f'- Salário Líquido : R$ {salario_liquido:.2f}')
