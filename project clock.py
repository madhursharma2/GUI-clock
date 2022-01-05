from tkinter import *
import tkinter
from time import strftime

def tym():
    t= strftime("%H:%M:%S %p")
    lbl.config(text=t)
    lbl.pack()
    lbl.after(500,tym)
    temp = f"Current time is: {t}"
    print(temp)
    print(t)
    pass
clock = tkinter.Tk()


lbl = tkinter.Label(clock)
lbl = tkinter.Label(clock, background="yellow", foreground="blue",font=("Comic Sns MS",55,"bold"))
lbl_2 =tkinter.Label(clock, text="time is:")
lbl_2.pack()


tym()
clock.mainloop()
