salario = float(input())

if salario <= 720:
    inss = salario * 0.0765
elif salario > 720 and salario <= 1200:
    inss = salario * 0.09
elif salario > 1200 and salario <= 2400:
    inss = salario * 0.11
elif salario > 2400:
    inss = 2400 * 0.11
    
print(f'{inss:.2f}')