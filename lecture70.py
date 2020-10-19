words = {'Bird': 'มันคือนก', 'Worm': 'หนอนไงหละ', 'Fan': 'พัดลมง'}
print(words['Bird'])
# words.clear() # todo Clear ข้อมูล ใน directory
# words.copy() # todo copy ข้อมูล ใน directory
print(words.items())
print(words.keys())

for i in words.keys():
    print(i)

for i in words.values():
    print(i)
