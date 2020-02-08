try:
    import tkinter as tk
    import tkinter.ttk as ttk
except ImportError:
    import Tkinter as tk
    import ttk

from tkinter import *
import os
import ParticipantData
from datetime import datetime


ParticipantData = ParticipantData.ParticipantData()
root = tk.Tk()
root.title("Dr.Robo Control Panel")

style = ttk.Style()
style.theme_create('appstyle', parent='alt',
                   settings={
                       'TLabelframe': {
                           'configure': {
                             #  'background': 'blue'
                           }
                       },
                       'TLabelframe.Label': {
                           'configure': {
                               # 'background': 'red'     uncomment this to make even label red
                            }
                       }
                   }
                   )
style.theme_use('appstyle')


labelframe = ttk.LabelFrame(root, text="Gripper Controller")
labelframe.grid(padx=20, pady=20)

def OpenGripper():
    print('Open')
    #os.system(r"arduino-cli compile --fqbn arduino:avr:mega C:\Users\nalsadi\Documents\Arduino\OpenGrip")
    os.system(r"arduino-cli upload --port COM3 --fqbn arduino:avr:mega  C:\Users\nalsadi\Documents\Arduino\OpenGrip")
def CloseGripper():
    print('Close')
    #os.system(r"arduino-cli compile --fqbn arduino:avr:mega C:\Users\nalsadi\Documents\Arduino\CloseGrip")
    os.system(r"arduino-cli upload --port COM3 --fqbn arduino:avr:mega  C:\Users\nalsadi\Documents\Arduino\CloseGrip")
def VariableGripper(input):
    try:
        if(0 > int(input) > 140):
            return False
    except ValueError:
        return False
    with open(r"C:\Users\nalsadi\Documents\Arduino\Variable\Variable.ino") as f:
        content = f.readlines()
    content[28] = content[28][0:9] + input + ";"
    #print(content[28])
    with open(r'C:\Users\nalsadi\Documents\Arduino\Variable\Variable.txt', 'w') as f:
        for item in content:
            f.write("%s\n" % item)
    os.remove(r'C:\Users\nalsadi\Documents\Arduino\Variable\Variable.ino')
    os.rename(r'C:\Users\nalsadi\Documents\Arduino\Variable\Variable.txt', r'C:\Users\nalsadi\Documents\Arduino\Variable\Variable.ino')
    os.system(r"arduino-cli compile --fqbn arduino:avr:mega C:\Users\nalsadi\Documents\Arduino\Variable")
    os.system(r"arduino-cli upload --port COM3 --fqbn arduino:avr:mega  C:\Users\nalsadi\Documents\Arduino\Variable")

btn = Button(labelframe, text="Open", command=OpenGripper,borderwidth=2, relief="groove",padx=10, pady=10)
btn.pack()

btn2 = Button(labelframe, text="Close", command=CloseGripper,borderwidth=2, relief="groove",padx=10, pady=10)
btn2.pack()

varlab = tk.Label(labelframe, text="Variable Input",padx=10, pady=10)
varlab.pack()
e1 = tk.Entry(labelframe)
e1.pack()

btn4 = Button(labelframe, text="Enter", command= lambda: VariableGripper(e1.get()),borderwidth=2, relief="groove",padx=10, pady=10)
btn4.pack()

labelframe2 = ttk.LabelFrame(root, text="Data Acquistion Labeling")
labelframe2.grid(padx=20, pady=20)

Name = IntVar()

Radiobutton(labelframe2, text="Whitney", variable=Name, value=1).grid(row=1, column = 1)
Radiobutton(labelframe2, text="Nick", variable=Name, value=2).grid(row=1, column = 2)
Radiobutton(labelframe2, text="Adesh", variable=Name, value=3).grid(row=1, column = 3)
Radiobutton(labelframe2, text="Naseem", variable=Name, value=4).grid(row=1, column = 4)

def Check():
    Names = ["N\A", "Whitney", "Nick", "Adesh", "Naseem"]
    ParticipantData.name = Names[Name.get()]

btn3 = Button(labelframe2, text="Check", command= Check ,borderwidth=2, relief="groove").grid(row=1, column = 5)

# datetime object containing current date and time
now = datetime.now()
# dd/mm/YY H:M:S
dt_string = now.strftime("%d/%m/%Y %H:%M:%S")
print("date and time =", dt_string)
ParticipantData.datetime = dt_string
mainloop()


root.mainloop()