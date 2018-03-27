#!/usr/bin/python
from tkinter import *
from tkinter import ttk
from tkinter import font
import time
import datetime

global endTime 

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
# Use tkinter lib 
root = Tk()
# root.configure(background='black')
labelFont = ("URW Chancery L", 45, 'bold', 'italic')
statusPin = StringVar()
control = IntVar()
countPin = IntVar()
timeIn = IntVar()
timeStart = datetime.datetime.now()
timeEnd = datetime.datetime.now()

def update():
    global statusPin, countPin, control, timeStart, timeEnd, timeIn, root # you don't really need to declare these as global because doing it this way gets rid of the ambiguity
    if GPIO.input(7) :
        print("ON ") 
        if (control.get() == 0) :
            timeIn = timeEnd - timeStart
            timeStart = datetime.datetime.now()
            timeIn = datetime.timedelta(microseconds=timeIn.microseconds)
            txt.set(timeIn)
            countPin.set(countPin.get() + 1)
            control.set(1)                 # has counted
            GPIO.output(11,GPIO.HIGH)
        # else : here the control is 1, so countPin has counted
        # statusPin.set('pin high')
    else : 
        if (control.get() == 1) :
            GPIO.output(11,GPIO.LOW)
            print("OFF ")
            timeEnd = datetime.datetime.now()
        # else : here the control is 1, so countPin has counted
        # GPIO.output(11,GPIO.LOW)
        # statusPin.set('pin low')
        # print("OFF ")
        # statusPin.set('pin low')
        control.set(0)
    root.after(0, update)

def exitProgram():
    print("Exit Button pressed")
    GPIO.cleanup()
    root.quit()

    
def show_time():
    # Get the time remaining until the event
    remainder = endTime - datetime.datetime.now()
    # remove the microseconds part
    remainder = remainder - datetime.timedelta(microseconds=remainder.microseconds)
    # Show the time left
    txt.set(remainder)
    # Trigger the countdown after 1000ms
    root.after(1000, show_time)


# Set the end date and time for the countdown
endTime = datetime.datetime(2017, 9, 19, 9, 0, 0)

fnt = font.Font(family='Helvetica', size=60, weight='bold')
txt = StringVar()
lbl = ttk.Label(root, textvariable=txt, font=fnt, foreground="green", background="black")
lbl.place(relx=0.5, rely=0.5, anchor=CENTER)
lbl.pack()
# root.attributes("-fullscreen", True)
# root.configure(background='black')
# root.bind("x", quit)

#  root.after(1000, show_time)

root.title("Sown")
root.geometry('700x380')

exitButton  = Button(root, text = "Exit", command = exitProgram, height =2 , width = 6)
exitButton.pack(side = BOTTOM)

labelCount = Label(root, textvariable=countPin, fg='white', bg='black', font=labelFont)
labelCount.place(x=70,y=-20)
labelCount.pack()

root.after(0, update)
# mainloop()
root.mainloop()




