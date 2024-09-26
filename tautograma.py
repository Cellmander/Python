while True:
    frase = input().lower()
    if frase == '*':
        break
    eh_tautograma = 'Y'
    #for letra in frase:
    for letra in range(len(frase)):
        if frase[letra] == ' ':
            if frase[letra+1] != frase[0]:
                eh_tautograma = 'N'
                break
    print(eh_tautograma)