menuList = []


def showBill():
    totle = 0
    print('<-------------- My Food -------------->')
    for number in range(len(menuList)):
        print(menuList[number][0], menuList[number][1])
        totle += int(menuList[number][1])
    print('Totle Price(THB) : ', totle)


while True:
    menuName = input('Please Enter Menu : ')
    if (menuName.lower() == 'exit'):
        break
    else:
        menuPrice = input('Price : ')
        menuList.append([menuName, menuPrice])

showBill()
