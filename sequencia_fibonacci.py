numero = int(input())

if numero == 1 or numero == 2:
    n_termo = 1
else:
    a = 1
    b = 1
    for i in range(1, numero-1):
        c = a + b
        a = b
        b = c
    n_termo = c
print(n_termo)