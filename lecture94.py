# Todo https://tkdocs.com/tutorial/index.html
from tkinter import *


def sayHelloWorld():
    print('Hello World')


mainWindow = Tk()
button = Button(mainWindow, text='ClickMe1', command=sayHelloWorld).grid(row=0, column=1)

button2 = Button(mainWindow, text='ClickMe2', command=sayHelloWorld).grid(row=0, column=2)
button3 = Button(mainWindow, text='ClickMe3', command=sayHelloWorld).grid(row=1, column=2)

mainWindow.mainloop()
