# Todo https://tkdocs.com/tutorial/index.html
import math
from tkinter import *


def bmiCalculator(event):
    print(float(textBoxWeight.get()) / math.pow(float(textBoxHeight.get()) / 100, 2))
    bmiCalcu = float(textBoxWeight.get()) / math.pow(float(textBoxHeight.get()) / 100, 2)
    # lableResult.configure(text=bmiCalcu)

    if bmiCalcu < 18.5:
        lableResult.configure(text='อยู่ในเกณท์ := ซน้ำหนักน้อย / ผอม')
    elif bmiCalcu >= 18.5 and bmiCalcu < 23:
        lableResult.configure(text='อยู่ในเกณท์ := ปกติ (สุขภาพดี)')
    elif bmiCalcu >= 23 and bmiCalcu < 25:
        lableResult.configure(text='อยู่ในเกณท์ := ท้วม / โรคอ้วนระดับ 1')
    elif bmiCalcu >= 25 and bmiCalcu < 30:
        lableResult.configure(text='อยู่ในเกณท์ := ท้วม / โรคอ้วนระดับ 2')
    elif bmiCalcu >= 30:
        lableResult.configure(text='อยู่ในเกณท์ := ท้วม / โรคอ้วนระดับ 3')


mainWindow = Tk()

labelHeight = Label(mainWindow, text='ส่วนสูง (cm.)')
labelHeight.grid(row=0, column=0)
textBoxHeight = Entry(mainWindow)
textBoxHeight.grid(row=0, column=1)

labelWeight = Label(mainWindow, text='น้ำหนัก (Kg)')
labelWeight.grid(row=1, column=0)
textBoxWeight = Entry(mainWindow)
textBoxWeight.grid(row=1, column=1)

calculatorButton = Button(mainWindow, text='คำนวน')
calculatorButton.bind('<Button-1>', bmiCalculator)
calculatorButton.grid(row=2, column=0)

lableResult = Label(mainWindow, text='ผลลัพธ์')
lableResult.grid(row=2, column=1)

mainWindow.mainloop()
