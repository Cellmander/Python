palavra1 = input()
palavra2 = input()
if palavra1 == palavra2:
    print(False)
else:
    print(sorted(palavra1) == sorted(palavra2))