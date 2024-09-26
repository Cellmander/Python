num_saltador = int(input())

melhor_salto = -1
nome_melhor_saltador = ''
for i in range(num_saltador):
    s1, s2, s3, nome = input().split()
    maior_salto = max(float(s1), float(s2), float(s3))
    if maior_salto > melhor_salto:
        melhor_salto = maior_salto
        nome_melhor_saltador = nome
        
print(nome_melhor_saltador)