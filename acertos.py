gabarito = input()
respostas = input()
acertos = 0

for i in range(len(gabarito)):
    if gabarito[i] == respostas[i]:
        acertos += 1
print(acertos)