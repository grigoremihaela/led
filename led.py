# Library Imports
import tkinter
from tkinter import *
#  import sys
import time
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
timeStart = time.time()
timeEnd = time.time()

def update():
    global statusPin, countPin, control, timeStart, timeEnd, timeIn, root # you don't really need to declare these as global because doing it this way gets rid of the ambiguity
    if GPIO.input(7) :
        if (control.get() == 0) :
            timeIn = timeEnd - timeStart
            timeStart = time.time()
            countPin.set(countPin.get() + 1)
            control.set(1)                 # has counted
        # else : here the control is 1, so countPin has counted
        GPIO.output(11,GPIO.HIGH)
        statusPin.set('pin high')
        print("ON ") 
        timeEnd = time.time()
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

ledButton = Button(root, text = "COUNT", height = 2, width =8 )
ledButton.pack()

labelCount = Label(root, textvariable=countPin, fg='white', bg='black', font=labelFont)
labelCount.place(x=70,y=-20)
labelCount.pack()

labelPin = Label(root, textvariable=statusPin, fg='white', bg='blue', font=labelFont)
labelPin.place(x=70,y=-5)
labelPin.pack()

labelTimeIn = Label(root, textvariable=timeIn, fg='black', bg='green', font=labelFont)
labelTimeIn.place(x=70,y=-45)
labelTimeIn.pack()

update()
# mainloop()
root.mainloop()




