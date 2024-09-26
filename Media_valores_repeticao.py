tamanho = int(input())
soma = 0

for i in range(tamanho):
    soma += float(input())
    
media = soma / tamanho
print(media)