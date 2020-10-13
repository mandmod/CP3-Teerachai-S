inputRound = int(input('Please Enter number : '))
sumNum = 0
print(list(range(inputRound)))
for x in range(inputRound):
    inputRound = int(input('x' + str(x + 1) + ' : '))
    sumNum += inputRound
print('Sum = ', sumNum)
