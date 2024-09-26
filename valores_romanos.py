val_romanos = {'M':1000, 'D':500, 'C':100, 'L':50, 'X':10, 'V':5, 'I':1}

num_romanos = input()
decimais = 0

for num in range(len(num_romanos)-1):
    valor = num_romanos[num]
    valor_prox = num_romanos[num+1]
    if val_romanos[valor] >= val_romanos[valor_prox]:
        decimais += val_romanos[valor]
    else:
        decimais -= val_romanos[valor]
decimais += val_romanos[num_romanos[-1]]

print(decimais)