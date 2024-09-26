frase = input()
frase_limpa = ""

for letra in frase.lower():
    if letra.isalpha():
        frase_limpa += letra
print(frase_limpa == frase_limpa[::-1])