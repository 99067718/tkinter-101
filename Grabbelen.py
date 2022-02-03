import random
from tabnanny import check
import tkinter

AmountOfClicks = 0
CongratsText = "Gefeliciteerd!!!"

def displayGrabbedItem():
    global AmountOfClicks
    global CongratsText
    randomChosen = random.choice(randomItems)
    AmountOfClicks += 1
    if AmountOfClicks == 5:
        txtVar.set("HEY, waarom pak jij zo veel, je mag er maar 1 per persoon!!!")
        CongratsText = "maar je verdient het niet, dus het we nemen het weer in."
    else:
        txtVar.set(f"Je hebt een {randomChosen} gepakt, {CongratsText}")
    
    

randomItems = ["Lege verpakking", "Nintendo Switch", "Schildpad", "Mes", "Appel", "Kaas", "koe"]
MyWindow = tkinter.Tk()
txtVar = tkinter.StringVar(value="Je hebt nog niet gegrabbelt.")
TextLabel = tkinter.Label(MyWindow,textvariable=txtVar).pack()
TriggerRandom = tkinter.Button(text="Klik om te grabbelen",command=displayGrabbedItem).pack()
MyWindow.mainloop()