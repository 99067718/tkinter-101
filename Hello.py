import time
import tkinter as tk
import threading
repeats = 0

def GlitchTitle():
    pass
    while True:
        time.sleep(0.02)
        root.title("Hellleellelelelell")
        time.sleep(0.02)
        root.title("Helllolololllollooooo")
        time.sleep(0.02)
        root.title("HeeeHelleHeeHHHHHellohe")
        time.sleep(0.02)
        root.title("HHHHelleleeHHoollHHHHHo")
        time.sleep(0.02)
        root.title("heLoloEloELolEO")

def GlitchSize():
    pass
    while True:
        root.geometry("700x500+2000+1000")
        time.sleep(0.03)
        root.geometry("600x400+100+700")
        time.sleep(0.3)
        root.geometry("700x450+820+50")
        time.sleep(0.3)
        root.geometry("500x550+0+0")
        time.sleep(0.1)
        root.geometry("700x500+1000+500")
        time.sleep(0.03)
        root.geometry("600x400+400+200")
        time.sleep(0.3)
        root.geometry("700x450+500+400")
        time.sleep(0.3)
        root.geometry("500x550+40+90")
        time.sleep(0.1)
        
def GlitchLoop():
    global repeats
    time.sleep(1)
    repeats += 1
    match repeats:
        case 8:
            root.config(bg="purple")
            label.config(text="GiVe uP!!111!")
            time.sleep(0.05)
            label.config(text="gI vE   Up1 1!! !1")
            root.config(bg="red")
            time.sleep(0.05)
            root.config(bg="purple")
            label.config(text="GiVe uP!!111!")
            time.sleep(0.1)
            label.config(text="gI vE   Up1 1!! !1")
            root.config(bg="black")
            time.sleep(0.05)
            root.config(bg="purple")
            label.config(text="GiVe uP!!111!")
            time.sleep(0.02)
            label.config(text="gI vE   Up1 1!! !1")
            root.config(bg="black")
            time.sleep(0.05)
            label.config(text="Hello Tkinter")
            root.config(bg="green")
        case 10:
            label.config(text="01001000 01100101 01101100 01101100 01101111 00100000 01010100 01101011 01101001 01101110 01110100 01100101 01110010")
            time.sleep(1)
            label.config(text="Hȩ̷̻͚̫͈̙̪̞͓̎̌͆̈́̆̆̏͌͝llo Tkintȩ̷̻͚̫͈̙̪̞͓̎̌͆̈́̆̆̏͌͝rrr")
            threading.Timer(1.0, GlitchTitle).start()
        case 11:
            root.config(bg="black")
            label.config(bg="purple",font="wingdings")
        case 13:
            threading.Timer(1.0, GlitchSize).start()
    threading.Timer(1.0, GlitchLoop).start()

root = tk.Tk()
root.title("Hello")
root.geometry("1000x1000")
root.config(bg="green")
label = tk.Label(root, text="Hello Tkinter",bg = "yellow", height = 10, width = 15, relief = "solid", cursor = "plus", fg= 'red')
label.pack()
GlitchLoop()
root.mainloop()