mes = [[int (x) for x in input().split()] for _ in range(12)]
media = []
for i in range(12):
    media.append(round(sum(mes[i])/len(mes[i]), 2))
print(str(media))