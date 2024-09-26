senha = 2002

while senha == 2002:
    entrada = int(input())
    if entrada != senha:
        print('Senha Invalida')
    else:
        print('Acesso Permitido')
        senha = 1