# Todo ไปเอ่านเอา เองนะจ๊ะ
#  https://www.w3schools.com/python/python_strings.asp
#  https://pyformat.info/
#  https://www.programiz.com/python-programming/methods/string/format
#  https://www.programiz.com/python-programming/methods/string/format
#  https://www.qhmit.com/python/reference/python_3_string_methods.cfm

name = 'Teerachai'
weight = '66'

print('Hello' + ' Teerachai ! and weight is ' + '66' + ' kg')
print('Hello %s ! and weight is %s kg' % (name, weight))
print('Hello %s ! and weight is %s kg' % (name, weight))

print()
mylist = [1, 2, 3]
print('a list: %s' % mylist)

print()
txt = "For only {price:.2f} dollars!"
print(txt.format(price=49))

print()
txt1 = "My name is {fname}, I'am {age}".format(fname="John", age=36)
txt2 = "My name is {0}, I'am {1}".format("John", 36)
txt3 = "My name is {}, I'am {}".format("John", 36)
print(txt1)
print(txt2)
print(txt3)
