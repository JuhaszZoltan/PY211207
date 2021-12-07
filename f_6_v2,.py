n = int(input('Add meg, hogy hány sorból álljon az alakzat: '))

e = 0
v = n - 1

for x in range(n):
    print(f'{e * "_"}O{v * "_"}')
    e += 1
    v -= 1