number = int(input('Input Number : '))
print()
text = ''
text2 = ''
text3 = ''
text4 = ''
for i in range(number):
    text = text + '*'
print(text)
print('--------------')
print()
print(number * '*')
print('--------------')
print()
for i in range(number):
    text2 = text2 + '*'
    print(text2)
print('--------------')
print()
for x in range(number):
    text3 = ''
    for y in range(x + 1):
        text3 += '*'
    print(text3)
print('--------------')
print()
for i in range(number):
    print('*' * (i + 1))
