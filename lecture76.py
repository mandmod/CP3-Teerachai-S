fruits = {'apple', 'banana', 'pineapple', 'orange'}
print(fruits)
# del fruits
# fruits.clear()
fruits.remove('banana')
fruits.add('Grape')
print(fruits)

userInput = int(input('Enter Number of Your Favorite Fruite:'))
myFruits = set()
while (len(myFruits) < userInput):
    myFruits.add(input('Fruits: '))
    print(myFruits)
