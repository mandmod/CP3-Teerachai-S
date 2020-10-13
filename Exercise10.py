start = int(input('start: '))
step = int(input('Step: '))
result = ''
for i in range(5):
    print(start + step * i, end=' ')

print()

for i in range(5):
    result += str(start + step * i + 1)
    print(result)

print()

for i in range(10):
    result += str(start + step * i + 1)
    print(result)
