pessoa1 = int(input())
pessoa2 = int(input())
pessoa3 = int(input())

if pessoa1 == pessoa2:
    if pessoa2 == pessoa3:
        n_festas = 1
    else:
        n_festas = 2
elif pessoa2 == pessoa3:
    if pessoa1 == pessoa3:
        n_festas = 1
    else:
        n_festas = 2
elif pessoa1 == pessoa3:
    n_festas = 2
else:
    n_festas = 3
print(n_festas)