import random
max_seb = int(input('Add meg a legnagyobb megengedett sebességet: '))
akt_seb = random.randint(6000, 13000) / 100
print(f'Sebességed: {akt_seb} km/h')

if akt_seb > max_seb + 40:
    print('50e HUF büntetést kell fizetned!')
elif akt_seb >= max_seb + 20:
    print('30e HUF büntetést kell fizetned!')
else:
    print('Nem kell büntetést fizetned!')


