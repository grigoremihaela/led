# Library Imports
import tkinter
from tkinter import *
#  import sys
import RPi.GPIO as GPIO

GPIO.setmode(GPIO.BOARD)
GPIO.setup(7, GPIO.IN)

GPIO.setmode(GPIO.BOARD)
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

def update():
    global statusPin, root # you don't really need to declare these as global because doing it this way gets rid of the ambiguity
    if GPIO.input(7) :
        GPIO.output(11,GPIO.HIGH)
        if control == 0 :
            countPin.set(countPin.get() + 1)
            control.set(1)
            statusPin.set('pin high')
            print("ON ")
    else :
        GPIO.output(11,GPIO.LOW)
        statusPin.set('pin low')
        control.set(0)
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




