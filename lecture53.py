def vatCalculate(totalPrice):
    result = totalPrice + (totalPrice * 7 / 100)
    return result


print(vatCalculate(200))


# todo การเขียนโปรแกรม ให้สั้น และกระชับ จะมีผลกับ Memmory ถ้า function นั้น ไม่ได้นำไปใช้งานต่อ
# todo ก็ไม่ควร ที่จะ สร้างตัวแปล ให้เปลีอง Memmory

def vatCalculate(totalPrice):
    return = totalPrice + (totalPrice * 7 / 100)


print(vatCalculate(200))
