a = float(input('Add meg a téglatest egyik élét: '))
b = float(input('Add meg a téglatest másik élét: '))
c = float(input('Add meg a téglatest harmadik élét: '))

if a <= 0 or b <= 0 or c <= 0:
    print('Hibás adatbevitel!')
else:
    print(f'A téglatest felszíne: {2 * (a * b + a * c + b* c)}cm^2')
    print(f'A téglatest térfogata: {a * b * c} cm^3')
