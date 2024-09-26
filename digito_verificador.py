frase = input()
frase_limpa = ""

for letra in frase:
    if letra.isalpha():
        frase_limpa += letra
print(frase_limpa == frase_limpa[::-1])