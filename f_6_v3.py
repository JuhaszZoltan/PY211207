n = int(input('Add meg, hogy hány sorból álljon az alakzat: '))

for x in range(n):
    print(f'{x * "_"}O{(n - 1 - x) * "_"}')