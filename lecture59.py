# Todo ไปเอ่านเอา เองนะจ๊ะ
#  https://www.w3schools.com/python/python_strings.asp
#  https://pyformat.info/
#  https://www.programiz.com/python-programming/methods/string/format
#  https://www.programiz.com/python-programming/methods/string/format
#  https://www.qhmit.com/python/reference/python_3_string_methods.cfm

name = input('Firstname : ')
lastname = input('Lastname : ')
print('Hello !! {} {} !'.format(name, lastname))
print('Hello !! {} {} !'.format(name.capitalize(), lastname.capitalize()))  # todo ทำตัวแรกให้เป็นตัวใหญ่
# todo Function Capitalize
#  จะทำให้ตัวแรก เป็นตัวใหญ่ https://www.w3schools.com/python/python_strings.asp
#  ลงไปอ่าน ในหัวข้อ String Methods

print('Hello !! {1} {0} !'.format(name.capitalize(), lastname.capitalize()))  # todo ระบุ String ที่จะใส่เข้าไป

print()
name = input('Firstname : ').capitalize()
lastname = input('Lastname : ').capitalize()
print('Hello !! {} {} !'.format(name, lastname))

print()
text = 'Teerachai'
textFormatted = 'Welcom {}'.format(text)
print(textFormatted.center(30, '-'))
print(len(text))
