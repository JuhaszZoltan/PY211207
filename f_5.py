import random

c = 0
s = 0
for x in range(10):
    n = random.randint(0, 100)
    if n % 3 == 0 and n % 4 != 0:
        print(n, end=', ')
        c += 1
        s += n
if c == 0:
    print('nincsenek a feltételnek megfelelő számok')
else:
    print(f'\nA számok átlaga: {s / c}')