import tkinter
from tkinter import *
import RPi.GPIO as GPIO

GPIO.setmode(GPIO.BOARD)
GPIO.setup(7, GPIO.IN)
GPIO.setup(11, GPIO.OUT)
GPIO.output(11, GPIO.LOW)

root = tkinter.Tk()

def ledON():
    if GPIO.input(7) :
        GPIO.output(11,GPIO.HIGH)
        #ledButton["text"] = "LEDON"
        labelPin = Label(root, text = 'pin high')
        labelPin.pack()
        print("LED ON ")
    else :
        GPIO.output(11,GPIO.LOW)
        #ledButton["text"] = "LEDOFF"
        labelPin = Label(root, text = 'pin low')
        labelPin.pack()
        print("LED OFF ")

def exitProgram():
    print("Exit Button pressed")
    GPIO.cleanup()
    root.quit()


root.title("First GUI")
root.geometry('700x380')

exitButton  = Button(root, text = "Exit", command = exitProgram, height =2 , width = 6)
exitButton.pack(side = BOTTOM)

ledButton = Button(root, text = "LED-ON", command = ledON, height = 2, width =8 )
ledButton.pack()

exitButton.pack(side = BOTTOM)

ledButton = Button(root, text = "LED-ON", command = ledON, height = 2, width =8 )
ledButton.pack()

mainloop()