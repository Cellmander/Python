n = int(input())

a = 1
b = 1
c = 1
for _ in range(3, n+1):
    c = a + b
    a = b
    b = c
    
print(c)