n_bandejas = int(input())
copos_quebrados = 0

for i in range(n_bandejas):
    l, c = [int(w) for w in input().split()]
    if l > c:
        copos_quebrados += c
        
print(copos_quebrados)