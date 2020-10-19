menuList = []
priceList = []


def showBill():
    totle = 0
    print('<-------------- My Food -------------->')
    for number in range(len(menuList)):
        print(menuList[number], priceList[number])
        totle += int(priceList[number])
    print('Totle Price(THB) : ', totle)


while True:
    menuName = input('Please Enter Menu : ')
    if (menuName.lower() == 'exit'):
        break
    else:
        menuPrice = input('Price : ')
        menuList.append(menuName)
        priceList.append(menuPrice)

showBill()
