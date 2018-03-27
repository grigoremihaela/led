# Library Imports
#  import tkinter
from tkinter import *
from tkinter import ttk
from tkinter import font
import time
#  import datetime
from datetime import datetime
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
#  root = tkinter.Tk()
root = Tk()
# root.configure(background='black')
labelFont = ("URW Chancery L", 45, 'bold', 'italic')
statusPin = StringVar()
control = IntVar()
countPin = IntVar()
timeIn = IntVar()

global endTime 



def show_time():
    # Get the time remaining until the event
    remainder = endTime - datetime.now()
    # remove the microseconds part
    remainder = remainder - datetime.timedelta(microseconds=remainder.microseconds)
    # Show the time left
    txt.set(remainder)
    # Trigger the countdown after 1000ms
    root.after(1000, show_time)

def exitProgram():
    print("Exit Button pressed")
    GPIO.cleanup()
    root.quit()


root.title("Sown")
root.geometry('700x380')

exitButton  = Button(root, text = "Exit", command = exitProgram, height =2 , width = 6)
exitButton.pack(side = BOTTOM)



# Set the end date and time for the countdown
endTime = datetime(2017, 9, 19, 9, 0, 0)

fnt = font.Font(family='Helvetica', size=60, weight='bold')
txt = StringVar()
lbl = ttk.Label(root, textvariable=txt, font=fnt, foreground="green", background="black")
lbl.place(relx=0.5, rely=0.5, anchor=CENTER)

# mainloop()
root.mainloop()




