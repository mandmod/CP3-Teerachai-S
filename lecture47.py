for y in range(11):
    for x in range(12):
        print(y + 2, 'x', x + 1, '=', (y + 2) * (x + 1))
    print()
    break

for vol in 'hello':
    if vol == 'l':
        continue
    print(vol)
print('The End')
