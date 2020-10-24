# Todo https://tkdocs.com/tutorial/index.html
from tkinter import *


def sayHelloWorld():
    print('Hello World')


mainWindow = Tk()
button = Button(mainWindow, text='ClickMe', command=sayHelloWorld)
button.place(x=50, y=20)
mainWindow.mainloop()
