valor_veiculo = float(input())
sexo = input()
idade = int(input())
valor_premio = valor_veiculo * 0.1

if sexo == 'M':
    if idade <= 24:
        desconto = 0
    elif idade > 24 and idade <= 33:
        desconto = valor_premio * 0.1
    elif idade > 33:
        desconto = valor_premio * 0.2
        
elif sexo == 'F':
    if idade <= 24:
        desconto = valor_premio *0.05
    elif idade > 25 and idade <= 33:
        desconto = valor_premio * 0.20
    elif idade > 33:
        desconto = valor_premio * 0.35
        
valor_premio = valor_premio - desconto

print(f'{valor_premio:.2f}')