# Library Imports
import tkinter
from tkinter import *
#  import sys
import RPi.GPIO as GPIO

GPIO.setmode(GPIO.BOARD)
GPIO.setup(7, GPIO.IN)
GPIO.setup(11, GPIO.OUT)
GPIO.output(11, GPIO.LOW)

root = tkinter.Tk()
# root.configure(background='black')

# statusPin = StringVar()
statusPin = IntVar()
labelFont = ("URW Chancery L", 45, 'bold', 'italic')
labelPin = Label(root, textvariable=statusPin, fg='white', bg='black', font=labelFont)
labelPin.place(x=70,y=-5)

def update():
    global statusPin, root # you don't really need to declare these as global because doing it this way gets rid of the ambiguity
    if GPIO.input(7) :
        GPIO.output(11,GPIO.HIGH)
        # statusPin.set('pin high')
        statusPin = statusPin + 1
        print("ON ")
    else :
        GPIO.output(11,GPIO.LOW)
        # statusPin.set('pin low')
        print("OFF ")
    
    root.update()
    root.after(5, update)

def exitProgram():
    print("Exit Button pressed")
    GPIO.cleanup()
    root.quit()


root.title("Sown")
root.geometry('700x380')

exitButton  = Button(root, text = "Exit", command = exitProgram, height =2 , width = 6)
exitButton.pack(side = BOTTOM)

ledButton = Button(root, text = "count pin hight", command = ledON, height = 2, width =8 )
ledButton.pack()

labelPin.pack()

update()
# mainloop()
root.mainloop()




