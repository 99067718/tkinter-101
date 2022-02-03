import tkinter
import time
import threading

def ClockTimer():
    global time
    global txtString
    timestr = time.strftime('%H:%M:%S')
    root.title(timestr)
    txtString.set(timestr)
    threading.Timer(1.0, ClockTimer).start()

root = tkinter.Tk()
txtString = tkinter.StringVar(value='')
Textlabel = tkinter.Label(root, textvariable=txtString,bg = "green", bd = 100, fg = "white",font=("Courier", 44))
Textlabel.pack()
root.geometry("500x500")
root.config(bg="green")

ClockTimer()
root.mainloop()