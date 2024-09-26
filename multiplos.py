a, b = [int(w) for w in input() .split()]

if a%b == 0 or b%a == 0:
    print('Sao Multiplos')
else:
    print('Nao sao Multiplos')