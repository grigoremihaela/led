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
labelPin = Label(root, textvariable=statusPin, fg='white', bg='black', font=labelFont)
labelPin.place(x=70,y=-5)

control = IntVar()
control.set(0)

countPin = IntVar()
countPin.set(0)
labelCount = Label(root, textvariable=countPin, fg='white', bg='black', font=labelFont)
labelCount.place(x=70,y=-20)

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

labelCount.pack()

labelPin.pack()

timeStartButton = Button(root, text = timeStart, height = 2, width =50 )
timeStartButton.pack()

timeEndButton = Button(root, text = timeEnd, height = 2, width =50 )
timeEndButton.pack()

timeInButton = Button(root, text = timeIn.get(), height = 2, width =50 )
timeInButton.pack()

update()
# mainloop()
root.mainloop()




