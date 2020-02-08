from tkinter import *
import os
window = Tk()

window.title("Welcome to the Control Panel")

window.geometry('350x200')

lbl = Label(window, text="Gripper Control\n----------------------")
lbl.grid(column=0, row=0)
def OpenGripper():
    print('Open')
    os.system(r"arduino-cli compile --fqbn arduino:avr:mega C:\Users\robot\Documents\Arduino\sketch_feb06a\sketch_feb06a.ino")
def CloseGripper():
    print('Close')
    os.system(r"arduino-cli upload --port COM6 --fqbn arduino:avr:mega  C:\Users\robot\Documents\Arduino\sketch_feb06a\sketch_feb06a.ino")

btn = Button(window, text="Open", command=OpenGripper)

btn.grid(column=0, row=1)

btn2 = Button(window, text="Close", command=CloseGripper)

btn2.grid(column=0, row=4)

window.mainloop()
