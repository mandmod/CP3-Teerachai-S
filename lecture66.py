tupleExample = ('modlove', 'goldhand', 'mac')
print(tupleExample)
tupleExample2 = ('bank', 'key')
tupleExample3 = tupleExample + tupleExample2
print(tupleExample3)
print(tupleExample3[2])
print(tupleExample3[:3])
tupleExample4 = tupleExample + tupleExample2 * 2
print(tupleExample4)
print('modlove' in tupleExample4)

for i in tupleExample3:
    print(i)
