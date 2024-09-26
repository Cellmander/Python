comprimento = float(input())
largura = float(input())
gavetas = int(input())
madeira = input()

metro = comprimento*largura
valor_mesa = metro * 100
valor_gaveta = gavetas * 30
    
if metro > 2:
    valor_mesa += 50
    
if madeira == 'mogno':
    valor_madeira = 150
elif madeira == 'carvalho':
    valor_madeira = 125
else:
    valor_madeira = 0
    
valor_total = valor_mesa + valor_gaveta + valor_madeira

if valor_total < 200:
    valor_total = 200
print(valor_total)l,,6