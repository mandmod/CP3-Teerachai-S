def login():
    usernameInput = input("Username : ")
    passwordInput = input("Password : ")
    if usernameInput == "admin" and passwordInput == "1234":
        return showMenu()
    else:
        return login()
def showMenu():
    print("----- iShop -----")
    print("1. Vat Calculator")
    print("2. Price Calculator")
    return menuSelect()
def menuSelect():
    userSelected = int(input(">>"))
    if userSelected == 1:
        return priceCalculator()
    elif userSelected == 2:
        return priceCalculator()
    else:
        return menuSelect()
def vatCalculator(totalPrice):
    vat = 7
    result = totalPrice + (totalPrice * vat / 100)
    print("Price include VAT (THB) :", result)
    return result
def priceCalculator():
    price1 = int(input("First Product Price (THB): "))
    price2 = int(input("Second Product Price (THB): "))
    print("Total price (THB) :", price1+price2)
    return vatCalculator(price1+price2)

login()