while True:
    jogadas = int(input())
    if jogadas == 0:
        break
    resultados = input()
    mary = resultados.count('0')
    print(f'Mary won {mary} times and John won {jogadas - mary} times')