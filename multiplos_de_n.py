n = int(input())
m = int(input())

#while m > 1:
 #   eh_multiplo = m % n
  #  if eh_multiplo == 0:
   #     print(m, end=' ')
    #m -= 1
for i in range(1, m+1, 1):
    eh_multiplo = i % n
    if eh_multiplo == 0:
        print(i, end=' ')