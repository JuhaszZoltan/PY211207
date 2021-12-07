import random

l = []
for x in range(10):
    n = random.randint(0, 100)
    if n % 3 == 0 and n % 4 != 0:
        l.append(n)

for x in l:
    print(x, end =', ')
print(f'\nSzámok átlaga: {sum(l)/len(l)}')
