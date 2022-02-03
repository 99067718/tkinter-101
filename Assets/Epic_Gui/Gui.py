from importlib.resources import path
import tkinter
from tkinter import *
from PIL import ImageTk,Image
window = tkinter.Tk()
canvas = Canvas(window, width = 5000, height = 5000)
canvas.pack()
img = ImageTk.PhotoImage(Image.open("Discord.png"))
canvas.create_image(20, 20, anchor=NW, image=img)
window.mainloop()