# Library Imports
import tkinter
from tkinter import *
#  import sys
import time
from datetime import datetime
import RPi.GPIO as GPIO
#set up GPIO using BCM numbering
#GPIO.setmode(GPIO.BCM)
#setup GPIO board using board numbering
GPIO.setmode(GPIO.BOARD)
GPIO.setup(7, GPIO.IN)
# GPIO.setup(7, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)
# GPIO.setup(7, GPIO.IN, pull_up_down=GPIO.PUD_UP)
GPIO.setup(11, GPIO.OUT)
GPIO.output(11, GPIO.LOW)

root = tkinter.Tk()
# root.configure(background='black')
labelFont = ("URW Chancery L", 45, 'bold', 'italic')
statusPin = StringVar()
control = IntVar()
countPin = IntVar()
timeIn = IntVar()
timeStart = datetime.now().replace(microsecond=0)
timeEnd = datetime.now().replace(microsecond=0)

def update():
    global statusPin, countPin, control, timeStart, timeEnd, timeIn, root # you don't really need to declare these as global because doing it this way gets rid of the ambiguity
    if GPIO.input(7) :
        if (control.get() == 0) :
            timeIn = timeEnd - timeStart
            timeStart = datetime.now().replace(microsecond=0)
            countPin.set(countPin.get() + 1)
            control.set(1)                 # has counted
        # else : here the control is 1, so countPin has counted
        GPIO.output(11,GPIO.HIGH)
        statusPin.set('pin high')
        print("ON ") 
        timeEnd = datetime.now().replace(microsecond=0)
    else : 
        if (control.get() == 1) :
            GPIO.output(11,GPIO.LOW)
            print("OFF ")
        # else : here the control is 1, so countPin has counted
        # GPIO.output(11,GPIO.LOW)
        # statusPin.set('pin low')
        # print("OFF ")
        statusPin.set('pin low')
        control.set(0)
    
    root.update()
    root.after(0, update)

def exitProgram():
    print("Exit Button pressed")
    GPIO.cleanup()
    root.quit()


root.title("Sown")
root.geometry('700x380')

exitButton  = Button(root, text = "Exit", command = exitProgram, height =2 , width = 6)
exitButton.pack(side = BOTTOM)

labelCount = Label(root, textvariable=countPin, fg='white', bg='black', font=labelFont)
labelCount.place(x=70,y=-20)
labelCount.pack()

labelPin = Label(root, textvariable=statusPin, fg='white', bg='blue', font=labelFont)
labelPin.place(x=70,y=-5)
labelPin.pack()

labelTimeStart = Label(root, textvariable=datetime.now().replace(microsecond=0), fg='black', bg='green', font=labelFont)
labelTimeStart.place(x=70,y=-40)
labelTimeStart.pack()

labelTimeEnd = Label(root, textvariable=timeEnd, fg='black', bg='green', font=labelFont)
labelTimeEnd.place(x=70,y=-50)
labelTimeEnd.pack()

labelTimeIn = Label(root, textvariable=timeIn, fg='black', bg='orange', font=labelFont)
labelTimeIn.place(x=70,y=-60)
labelTimeIn.pack()

update()
# mainloop()
root.mainloop()




