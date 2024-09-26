while estoura == False:
    lin, col, k = [int(x) for x in input().split()]
    k -= 1
    estoura = False
    for l in range(lin):
        if estoura:
            break
        compartimentos = [int(x) for x in input().split()]

        i = k
        while compartimentos[i] == 0:
            i -= 1
            
        j = k
        while compartimentos[j] == 0:
            j += 1

        resultante = compartimentos[i] - compartimentos[j]
        k += resultante

        estoura = k <= i or k >= j
    k += 1
    l += 1

    if estoura:
        print(f'BOOM {l} {k}')
        
    else:
        print(f'OUT {k}')
