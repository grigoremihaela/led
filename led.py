# Library Imports
import tkinter
from tkinter import *
#  import sys
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

control = BooleanVar()
control.set(False)   # not has counted

countPin = IntVar()
labelCount = Label(root, textvariable=countPin, fg='white', bg='black', font=labelFont)
labelCount.place(x=70,y=-20)

def update():
    global statusPin, root # you don't really need to declare these as global because doing it this way gets rid of the ambiguity
    if GPIO.input(7) :
        GPIO.output(11,GPIO.HIGH)
        statusPin.set('pin high')
        print("ON ") 
        if (not control) :
            countPin.set(countPin.get() + 1)
            control.set(True)                 # has counted
        # else : here the control is 1, so countPin has counted
    else : 
        GPIO.output(11,GPIO.LOW)
        statusPin.set('pin low')
        control.set(False)
        print("OFF ")
    
    root.update()
    root.after(1, update)

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

update()
# mainloop()
root.mainloop()




