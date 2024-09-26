cpf = input()
cpf_limpo = ""

for n in cpf:
    if n.isdigit():
        cpf_limpo += n
if cpf_limpo.count(cpf_limpo[1]) == 11:
    print(False)
else:
    if len(cpf_limpo) == 11:
        soma = 0
        peso = len(cpf_limpo) - 1
        for numero in range(len(cpf_limpo)-2):
            soma += int(cpf_limpo[numero]) * peso
            peso -= 1
        dig_verif = 11 - soma % 11
        if dig_verif >= 10:
            dig_verif = 0
        if dig_verif != int(cpf_limpo[-2]):
            print(False)
        else:
            soma = 0
            peso = len(cpf_limpo) 
            for numero in range(len(cpf_limpo)-1):
                soma += int(cpf_limpo[numero]) * peso
                peso -= 1
            dig_verif = 11 - soma % 11
            if dig_verif >= 10:
                dig_verif = 0
            print(dig_verif == int(cpf_limpo[-1]))
    else:
        print(False)
