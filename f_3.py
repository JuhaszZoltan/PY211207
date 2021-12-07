n = int(input('Adj meg egy pozitíbv egész számot: '))

c = 0
for x in range(n + 1):
    print(x, end=' ')
    if x % 10 == 7: c += 1

print(f'\n7-re végződők száma: {c}')