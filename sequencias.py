x = 1
while x != 0:
    x = int(input())
    for i in range(1, x+1, 1):
        if i != x+1:
            print(i, end=' ')
        else:
            print(i)
            print()