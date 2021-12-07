n = int(input('Add meg, hogy hány sorból álljon az alakzat: '))

for s in range(n):
    for o in range(n):
        if s == o:
            print('O', end='\0')
        else:
            print('_', end='\0')
    print()