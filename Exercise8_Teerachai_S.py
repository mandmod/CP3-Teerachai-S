usernameInput = input("Username :")
passwordInput = input("Password :")
vat = 7

if usernameInput == "admin" and passwordInput == "1234":
    print("<----- Hello " + usernameInput + ' ----->')
    print()
    print("<----- Welcome to Apple Shop ----->")
    print()
    print("1. Ipad Air ================> 20,000 บาท")
    print("2. Apple Watch Series 20 ===> 10,000 บาท")
    print("3. Iphone 18 Pro ===========> 60,000 บาท")

    userSelected = int(input("สินค้าที่ลูกค้าต้องการ :"))
    buyQuantity = int(input('จำนวน : '))
    if userSelected == 1:
        price = 20000
        sumQuan = price * buyQuantity
        sumvat = sumQuan * vat / 100
        sumPrice = sumQuan + sumvat
        print("<---------------- Apple Shop ---------------->")
        print('<---------------- รายการสินค้า ----------------->')
        print('Ipad Air ================> 20,000', '*', buyQuantity, '=', sumQuan)
        print('Vat', vat, '%                               =', sumvat)
        print('Sum---------------------------------- =', sumPrice)
        print('<-------------- ขอบคุณที่ใช้บริการ --------------->')
    elif userSelected == 2:
        price = 10000
        sumQuan = price * buyQuantity
        sumvat = sumQuan * vat / 100
        sumPrice = sumQuan + sumvat
        print("<---------------- Apple Shop ---------------->")
        print('<---------------- รายการสินค้า ----------------->')
        print('Apple Watch Series 20 ===> 20,000', '*', buyQuantity, '=', sumQuan)
        print('Vat', vat, '%                               =', sumvat)
        print('Sum---------------------------------- =', sumPrice)
        print('<-------------- ขอบคุณที่ใช้บริการ --------------->')
    elif userSelected == 3:
        price = 60000
        sumQuan = price * buyQuantity
        sumvat = sumQuan * vat / 100
        sumPrice = sumQuan + sumvat
        print("<---------------- Apple Shop ---------------->")
        print('<---------------- รายการสินค้า ----------------->')
        print('Iphone 18 Pro ===========> 20,000', '*', buyQuantity, '=', sumQuan)
        print('Vat', vat, '%                               =', sumvat)
        print('Sum---------------------------------- =', sumPrice)
        print('<-------------- ขอบคุณที่ใช้บริการ --------------->')
    else:
        print('ไม่มี สินค้าตัวนี้ จ๊ะ  กระณา Login ใหม่นะจ๊ะ')
else:
    print('Username หรือ Password ผิดนะจ๊ะ')
