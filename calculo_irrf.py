salario = float(input())
dependentes = int(input())

desconto_dependentes = dependentes * 137.99

if salario <= 720:
    inss = salario * 0.0765
elif salario > 720 and salario <= 1200:
    inss = salario * 0.09
elif salario > 1200 and salario <= 2400:
    inss = salario * 0.11
elif salario > 2400:
    inss = 2400 * 0.11
    
if salario <= 1372.81:
    aliquota = 0
    deducao = 0
elif salario > 1372.81 and salario <= 2743.25:
    aliquota = 0.15
    deducao = 205.92
elif salario > 2743.25:
    aliquota = 0.275
    deducao = 548.82
    
irrf = (salario - desconto_dependentes - inss) * aliquota - deducao
if irrf > 0:
    print(f'{irrf:.2f}')
else:
    print(0.0)
