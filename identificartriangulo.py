a = int(input())
b = int(input())
c = int(input())

if a == b and a == c and b == c:
    print('equilátero')
elif a != b and a != c and b != c:
    print('escaleno')
else:
    print('isósceles')