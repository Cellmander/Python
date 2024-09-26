mensagem = input()
mensagem_decodificada = ''
mensagem = mensagem.replace(' ', '  ')
for p in mensagem[1::2]:
    mensagem_decodificada += p
print(mensagem_decodificada)