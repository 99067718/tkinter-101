from email.mime import image
from glob import glob
import tkinter
import threading
import pygame
from playsound import playsound


repeats = 0
def explode():
    global repeats
    repeats += 1
    if repeats == 3:
        root.geometry("70x70")
        root.configure(bg="yellow")
    elif repeats == 4:
        root.geometry("100x100")
        root.configure(bg="#ff9d00")
    elif repeats == 5:
        root.geometry("130x130")
        root.configure(bg="#ff5900")
    elif repeats == 6:
        root.geometry("160x160")
        root.configure(bg="#c73200")
    elif repeats == 7:
        root.geometry("190x190")      
        root.configure(bg="red")
    elif repeats == 8:
        root.geometry("210x210")
        root.configure(bg="#780000")
    elif repeats == 9:
        root.geometry("240x240")
        root.configure(bg="#2b0033")
    elif repeats == 10:
        root.geometry("436x360")
        root.configure(bg="#34aeeb")
        canvas1 = tkinter.Canvas( root, width = 270, height = 270)
        canvas1.pack(fill = "both", expand = True)
        canvas1.create_image( 0, 0, image = PictureExplosion, anchor = "nw")
    elif repeats == 68:
        window2 = tkinter.Tk()
        window2.geometry("7000x7000")
        window2.configure(bg="black")
        window2.mainloop()
        while True:
            print("✡︎□︎◆︎ ♋︎❒︎♏︎ ■︎□︎⧫︎ ♑︎□︎♓︎■︎♑︎ ⧫︎□︎ ♏︎⬧︎♍︎♋︎◻︎♏︎ ❍︎♏︎ ♋︎♑︎♋︎♓︎■︎✏︎✏︎✏︎")
            print(' ̶̧̢̨̮͖͔͎̖̗͖̜̟͔̘̭̻͕͓͕̞͔̣̱̻̱͔̝͇̺͇̽ ̶̛̱̣̦̭͙̞̻͚̒̒̔͊͗̌̈́̿̽̊͊̄̾̍͆̇͑͗̈́̽̾͛̈́̓̊͊̋́̆̅̂͐͋̀͐̄͒̏́̉̿͌͘͘̕̕͘͜͝͠ ̸̨̡̳̲͚̟̖̟̞͚̊̃͆͜ ̵̡̢̢̛̛̝͖̙͍̜͓̩̜͎̪̫͕̳͎̫͇͖͉̼̮̳͕͙͉̰͚͊̿̌̾̿̌͋̈́̈̒̏͐̅̈̈́̊̿̇̌͂̋̓͆̍̽̒̅̋͌́͑̔̅͛͐̈̏̕̚͘̚͜͜͜͜͝͝ͅ ̶̛̛̛̞̱̭̺̠̼͂̈́̌̂̄̄͑̀̐͂́̈͒̈́͛̿̈́͌͛̆́̓̅͐̊̓̍̓́̆̚̕͘͠͝ ̸̧̢̛̥͉̞͕͉̼̤̰͈̬͍̼̹̘̬̗̩͎̲̺̩͔̜̤̖̩͍͋̉͂̐͐̽̓͊͑̒̾̋̓̂̉̊̽͌͒̾̌͋͌͑͛̉̾̓̓̅̌̇͐̓́̊̍̎̄́͘͘̚̕͝͝ͅͅ ̵̢̧̧̧̱̩̻̹͉̣̲͔̞̩͉́ ̴̡̨̨̛̟̮̫̱͕͉̰͓͚̗̼̻̻̩̭̻̪̝͕̙͈͇̤̣̥͙͎͖̟͍̲̹̹͍̟͉̯̙̥͕̟̙̱̗̂̅͆̎́́̈̄̏̏̓̓̇̄̎̇͆́̔̇͘̕͝ͅͅ ̵̡̨̧̡͔̜̥̭̱̬̱̮͙̜̞̥̪̦̣̯͎͓̮͇͔̯̻̫͖̳̹̳͚̉͊̈́͊ͅͅ ̴̨̧̧̧̧̩̙͙͖̮̲͙̬̪̭̗͙͖͙͔̮̻͇͇̙͈̫͕̙͎̫̼̦͎̟̖̱̮̳̑ ̷̻̬͚̞̹͈͖̬̤̓̓̾͗̍͆̏͝ ̶̮̳̦̏͂̾͛̄̃̚̚̚͝ ̸̨̭̗͓̰̱͓͙̠̗̙̖̘̜̒̆̈́̇̀͂̑̅̑̏̇́́̀̎́̑̏͐̀̆̈͌̌͗̕̕͘̚̕͠͠͝ ̷̢̡̨̛̫̬̥̖̭̥̺͙̞̮͖̠̺̦̋́̎͑̔̃̎̆̇̈̌̑̄͒́̑̋̈́̀͊̿̄̈́̎̍̂̾̒́͛͘͘̕͘͘̚͜͝͝͝ͅ ̸̧̛̪̤̼̘̩͔͎͎̫̜̩͎̗̼̈́͗̍̋͂͂͆͆̃̽̐͛̀̋̑̉̐̉̈́̀͂̔̋̓̊͐͘͝͠͝͠ ̴̛͔̝̞̞͚͍͔̗͕̪̘̩̈̿̈́̌̓͊̀͐͊̒͛̒̈́͘̚͘͘ͅ ̶̢̬̪̹̟̜̝̺͇̗͖͊̈́̄̔̄͋͆͆̊̃́͌͆̂͂͗̾͗̌̾͋̒͂͐́̑̊̋̍̚͝͠͝ ̷̢̧̛̛͉͙̠͇̳̮̳̤̥͖̙͉͔̙̭͓̼͙͈̂̆͑͊̐̆̈́̈́̍̉͐̔̔̑̀̊̿̐̇̅͑̂͒̈́̀̓̉̐̈́̽͋̆̓̿̓̃̅̀̉̍̎͘͘͜ ̸̡̢̬̳͚̫̠̘̺̘͇͉͔̩̝̗̝̬͎͔͓̦͕̳͒̊͑͌́̀͂̇̃̈̾͌͜͠ ̵̨̣̯͇̯̘͇̮͍͔̰͉̪̤͍̜̜̌̔̔̈́́͊́̏̿̋̈͒͛͛͋͐̓̑͑͋̓̔̇͘̕͜͠͝͝͝ ̸̛̜̻̤̝̩̖̥͚̞͔̳̼͖̃̿͗͂͋͑̓̾͋̊̔͂̽͐̋̀́̽̾̀̄͐̈́͜͠͝͝ ̶̨̛̛͇̮̪̱͍͕̺͈͚͖̖̈̈́́̃̒́̑̈́̀̈́̀̓̇͊̊͗̌́̎̍̂̈́̓͆̓͛̇͂̍̆̕͘͘̕͘͠͝ ̴̨̠͖͚̥͎̤̲̯̥̣͕͉̖̎͑̈́̄̇̈̍̀̀̈͑́̿͆̍͒͊̾̍̏͌̿̆̑̄͂̑̌͑͊̈̍̓̉̾͂͊̀͗̔̋̽̈́̽̾̕̕͝ ̶̨̨̨̛͎̲̱͍̗͇͉̠̻̗̖̯̱̙̘̮̱͚͔̳̳͚͉̠̝͎̲͕͔̮̟̺̬̰͙̘̤̩̰̮̯͖̺̼͇̦̤̐͛͐͗̐̓̊̒̔̇͑͑̅̈̿̓̇̈́́͋͘͘̚͝͠ ̴̛̛̛̙͎̼͖̟̠̈́̋̽͊̿̒̉͐̎͠ ̷̨̨̡̨̨̡̛̛͈̣̦͉̠̙̳̘̜̩͔͙̹͇̙̯̹̘͙̤̖͙̩̩̀̀́̓̽̑̅̌̓̒̂͂͆͂̽͒̀̓͌̒̾́̋͆̾̿̀̂͋̊̏͑̉́́͋̀̐̌̐̈́̅͘̚͘̕͜͝ͅ ̸̠̥̻̦̻͑͊̓̀͌̽̓͗̆͛̔̑̋͛͝͠ ̶̨̡̨̛̗̤̣͉͚͈̬̫͙̥̟͓̻̼̟̣̣̝̫̯̻̣̰͚͔͎̹̖̄̇̑̅̍̾̆̾̈́͛̾̇͛̍͌̋̀̿̐̈̆̂́́̅̋̾̌́̂͗̇̊̀͌̕̕̕̚͘͜͜͜͝͝͠ͅͅ ̶̧̢̨̧̡̢̧̛̛̜̞͍̭̳͕̥̩̗̥̞̭͎̤̥͚̣̩̳̞̹̘̭̳͔̮̝̈̀̉̉̑̒̂͊̓͋̃̋̽̓̔͐̽̾̊̂̑̚͘͘̚̚͝͝ ̸̢̫̳̭̙͗̀͆̎̋̈́̐̾̊̓̓̅̆̏̄̌̊̆͋̅̎̾̑̊̅̈́̔̔̕̕̕͠͝͝ ̴̢̡̧̨̯̼̭̱̳̠͖̰̼̪̗͓̤̩̣͕̼̈́̏͐̃̚͜͜ͅͅ ̸̧̢̨͚̮̻͎̦̱̹̣̟͈͔̞̙̜̞͕͖̳͇̝̦͓͉͍̭̻͍̈́̾́̌͋͗͌̈̆̎̇̎̈́̍̅͊̌͑͆̃͗͌́̀̊̎̑̔̾̅͂̕͜͜͜͝͝͝͝͝͝͠ͅ ̶̨̤̼̦̰̞̞͈̬̻̼͎̖̫͔̗̖̦̟̫̜͖̬͂̌̌̀̏̎̒̿̏̕͝͝͠ ̵̩͙͖̟̥̟̬̬͇͈͎͂̄̅̄̂̇̄̎̽̈́̌͑̒͆̍͌͂͐͗̃̒̎̏̍̚͘͝͝͝ ̸̢̧̢̨̖͎̩͎̼̙͚̙̗̭̱̗͕̮͕̥̯̝͕͉̩̩̣̭͎͔̱͈͕̪̗̯̰̣͇̰͑͗͒̔͌͒̃̀̈̚͠ ̵̙̙̥͉̩̦́͛̋̇̆̑́̀̿̇̒̃̓̈́̄̓̈́̉̌̔̒̈́̀̈̉͊̆̈́̈̔͊͌́̈́͑̅̄̽͐̌̕̚͝͝͠ ̶̢̧̛̛̝̪̦͔̹͉̬̗̪̯̦̰̼̝̗͉̻̯̤͍̦͚̻͍̂̀͗̿̌̎͋͑̎̎̓̇̊̇͗̈́͑̀̎̈́̓̚͝ ̶͔͚͑̃̒̂̀̏̿̍̎̏̋̌̾̈́̈͠ ̴̘̼̰̗̗̯͙͈͇̲͆̎̂͆̈́͑̌̎͐͊̍͆̋̿͛̇͋͐̏̃̍̓͗̔͛̽͆́͘͠͝͝ͅͅ ̷̙̣͓̪̙̺̪͎̲̗̫̟͝ͅ ̵̡̛̛̛̹͔͙̼̮̱͍͔͖̔̍͆̊̍̓̍̾̽̾̀̎̇̓̒̉̓̀̋̿̽̊̅̉̀͒́̍̎̂̈́̕͘̕̕̕͘͠͠͝͝͝͠͝ ̷̧̢̘͕̮̹͓̺̼̻͍̬̻̝͑̈́͛͐̎̾̆̐͗̿̉̐̃̔̐͋̑͒̎̕͝͠͠͝ͅ ̵̢̢̢̛̛̤͇͍̩̻̞̫͈͕̫͉̺̞̜̞̘͈̣̩͍͒͒̅̇͆̿̀̒̈́͝ͅ ̴̡̢̧̨̨̗̼͔͚̖͓͕͔̜̬̳̳̝̰̮͚̪͍͍̟̮̻̝̖͔̯̬̫̯̆̈́̈̑̎̌̅̓͆̑͑ͅͅ ̶̢̨̢̡̨̛̛̛̜̮̹̩̙̮͎͕̲̥̘̻̳͍̫̱̺̣̰̖̬̤͓̞̖͉̞̺͖̥̭̫̳̟̍́̆͊̏̓̋̈́̀̓̌͂͊̈́͊̈́̊͌̍̓̕͝͝ ̸̛̛̯̟̳̫̽̂̍̈̅͂̓̃̀̈́̑̾̄͜͝͝͝ͅ ̷̡̢̛̫̬̺͚͈̫̲̤̝̻̰̣̬̣̬͖̰̖̠̖̙̣̪͚̫̝͙̠̰̪̘̲͎̮̓̍́͛̒͐̾̈́͛͘͘ ̶̛̛̛̛̤̪̥͖͖̙͇̪̞͎̖̅̓̍̂̆́͗̎̀͒̏͆͂̌̋̈́̿̍̂̆̒̋̓͒͒̓͆̾̇̆̃͂̑̊̀̉̓͆͘̕͠͝ ̸̧̡̧̨͇̟̪̝̖͔̪͈̘̤̥͍̘͙͈͕̤͍̭̭̟͕̰̠̪̙͆́̓̇͑̒̓̈́̄̈͊͋̓͌̌̽̚͘͜͜ͅ ̵̧͙̙̹̝̜͕̝̂̌̑̆̃̃̈́̓́͗̎͂͆̿̐̇̊͑̀͗̽̂͑̋̃̔͛̓̓̽̅̏͐̈́̾̂̀̇̐̕̚̕̚̚͘̚͝͠͝ ̸̢̢̖̱̤̬̭͖̭̺̩̖̼͉̗̥̝̲͉̘̟̟̬͈̼͕̩̲̠̆̌̄̓̒̎́͛̇̊̇̋̃̓̅̒̔̇̏̓̽̓͂̚͜͜ͅ ̷̛̛͈͉͈͔͖̭̗̪̩͍̲̝̪̜̦̰̮̝̯̞̲̪̦̲̭̈̂͐͋̾̉̄̒̀̎̊̎͌̾͆̔͆̈́̌͗̍̾̌́̈̋̾̑̎̊̀͊͘͠͠͝͠ ̴̡̨̡̢̨̡̛̛̪͓̭̠̻̺͎͈̫̥͕̦̯̟̜͇̭̼̞̹̪̝̱͖͖̼̲̩̹̠̯̩̹͍͈̻̲̀͒́͆͊̏͋̉̂́͗̄̅̋͆̑̅̔͋͐͐̈̃̅̓͆͋͆̈̃̈́̇̌̉́͂̽̓̑̈̕̚͘̕͜͜͝͝͝ͅ ̴͖̠̲͍̠͖̳̺͓̳͕͈̭̈͑͒͛̏̀́͝ ̵̧̡̡̨̢̡̨̭̗͍̲͖͖̩̖̣͍͎͓̻̣̟̟̰̺̳̥̙̟̘͕̻͎͔̙͔̝͔͉̳̰͕̼̊̉̽̒͐̉͌̈́́̈́̏̎̏̊̈́͒̾̿̚͘̚͘̕͜͝͠ ̶̧̧̧̛͙͇̣̼̦̼͙̮̹̲̯͈̣̼͉̭̘̤̗̺̲͚̼̝̭̭͇̠͔͖̲̖͓̞̜̬̹̝̰̂̌͒̃̊̊̔̍̓̓͒̆̏̀͋̓̅͒̃̏̔̓̈́͊̕͘͘͜͠͝͠ͅ ̷̧̢̧̧̧̼̬̞̹͚̤͇̭̺̹̪͈͕̗̹͔͔̝͇̩͎͉͍̘͈̠̝͉͈̘̰̜̫̏̉͜͝ͅͅ ̵̧̨̧̱̭͍͕̞̠̖̣̝̗͙͓̠̹̣̬̟̣͔͇̝̮̻͕̲̥̬̺̦͇̦̇͌̃̊̈́͋̎̌̈́̚͝ͅ ̴̨̡̡͖̠̳͓̬̝̲̱̮̳̤̰̬̰͙̞̪̝̖̰͎͚̭̙̤̣̳͎͖̟̜̹̱̞̝͔͔̜̩͕̦͍͍̌̏̀͛̔̒̌͛̍̊͛̈́̓̋͂̅́̋̍̈́̑́̈̅̑̑̌̿͘̚͠ͅͅ ̴̡̡͉̞̹̪̝̮̰͙̗̗̠̲̝͓̤͖͇̬̩͕͙͉̥̑̑̄͛͗̍̇̂̃̎̈́͆̑̊͒̀̀́̆͂͋̒̓͒̉̓̂͘͘͜͝ ̵̡̧̡̱̻̱̟̘͓̬̤̻̼͚̬̝͚̩̩̟̮̦̹̟̜̬̩̣̹̯͇̰̞͚̱̆͒̓̇̆̋͊̈́̒͝͠ͅ ̷̡̡̛̛̜͖̲͈̳̫̖̞̍̍̀̀̑̾͐̍́̐͒̐͛̎͌̀͐̾̓̈́̌͛͛͐̆́̏͒̈̽͆̇̿̒̓̊̈́̎̃͐̂̂̿̕̚̕͠ ̴̧̢̜̩̙͖̣͎̜͍̟͔̪̝̲̖͉̦̗̠͈̭͆̍̂͒̊̌͒͗̀ ̶̨̧̨̡̠̬̮̗̳̦͕̲͍͓͕̤͙͚̯͓̮̙̲̞̦̤͇̼̳̬̮̥͖͚̱̣͎͈͔̤̞̺̓̅̐̾ͅͅ ̴̨̨̛̹̬̺̰͍̝̩͚͉̰̯̲̙̺̪̺̥̖̫̼͈̰̦̲̤̣̘̺͚̪̰̲̹̞͌̑̒̇͐̆̏̈́̾̀̂́̂͆̿̑̏̽̀̎̍̔̏̐̇̓̍́̕ ̷̡̡̡̗̣̪̞̳̥̬̺̰̣͙̻̥̞̹̰̰̘̰̣̦̭̜̘̇̃̾̆̔̓͘ ̸̨̡̮̝̭̜̱̞̤̱͍̩̰͔͔̦̭͍̤͚͍̎̄̾́̐̏̎̀͆ ̶̫̻̲͙̌̏͆̔̈͛̍̉̒͐̊̈̒́̓̔̋͑͛̈͊͛̎͐̾́͑͛̑͐̐̽̏̉͘͝͝͠ ̸̢̠̰̭͖͖̳̰͔͇͆ ̷̢̧̝̪̙̪͖̻̞̠͕̯͈̙̱̗̤̣̟̘͎̭̬͎̇̿̓͒̉͐̈́͌̓̋̆̇͒͂̆̅̎̆̊̎̚͘͝ ̷̡̢̧̢̜̻̞͙̤̭̹̫͍̱͔̻̬̘̩̳̙̠̟͎͕̻̮͖̺̝̫̗̝̖̺̙̺̘̀̀͜ͅ ̴̨̨͚̹͔̦̳̥̯̲͖̠͖̺͕̙͓̹̮͙̱͖̭͇͍̑̇̄̚͜͝ͅ ̴̡̢̢̨̢̼̟͙̤̳̟̗̼̹͎͙̟͉͈̗̼̰̻̬͎̜̳̩͚̗͇̞̝̘̜̙̫̗͍̯̒͐̇̽̊̉̎͗̓͘͝ͅ ̶̧̡̧̜͖̞̝̲͚͕̻̞̘͍̼̩̱̥͇͔̲̭̻͕̮͓̿̈̓͆̌̿̂͛͠͝ͅ ̵̨̡̡̛̛͔̤̬̮̙͍̮͖̟̤͕̬͉̦̣̱̖͉̤̥̮̳̦͛͛͂̇̑͌̾̀́̋̓̋̈̀̈́̈́͒͗̇͆̄̇̀̋̆̀̑͐̑̑͋͌͌̚͘͘͘͠ ̸̧̢̨̙͖͍͓̤̖̹̟͙͈̜͓̻̲̖͎͕̮͍̙͕͈̟̱͖̲̮͔͔̜͉͉̰͙͚̬̙͙̱̺͇̯̮̊̃͗̄͆͆̈́̃̈́͋̅̽̽́̐̀͛̒͂̕͝͠ͅͅ ̴͉̪̀̿̋̑͗͛̓̅͑̽̈̈́̀̃̐͗ ̸̡̨̢̛͖̯̦̼̠͓̙͇͇͔̥̥̦͇̩̺̜̜͈̦̑̾̊̈͒͊̈́̊̍͑̊͗̏̇̈́́̾̉͂̈́̉͛̓̏͊͐̚͘ͅ ̵̡̛͎͉̻̤̩̖̻͍͓̬͍̯̜̯̠͔̭̺͚̱̽͂̄̍̌̄͆̐̒̊̓̽̏̄̀̌͑͗̍̀̽̐̋̈͂̊̎͛͌͑͘͝ͅ ̶̨̨̢̛͖̻̰̹̥̫̲̹̖̺͍̜̼̼͚̠͚̳̳͈̬̠̝̹̝̼͚̺̜͈͕̗͈̼̦̲̫͇͖̝͍̣̓̂̊͊̈̓̉͜͜͜ ̴̧̨̡̡̖̼͍͙͈̪̤̠̬͓͍̜̺̼̱̥̥͓̞͚̜̖̬̭̘̦̙͈̤͕͙̯̬̣̳͒̉͛̀̍̌̑̎̇̆̎̃̃̈̓͐͗̎̓̓́́̍̀̈̀́͑̅̆̍̑̚͜͝ͅͅͅ ̶͚̖͇̺̙͙͚͍͓̻͍̞͉͙̰̇͑͂͐͋̀͋̑̋͆̋̔̌̍͒́̊̏͋̆̈́͂ ̵̢̨̡̢̛͈̲̝̼̮̼̝̠̯͕͓̹̖̰̠̲̙̑͌̅͒̅͛̍͋̇͑̈́̈́̽̐́͆̊̋̒̉̈́̆̔̅̔̈́̌̋̈̎̓̐̓̌͂̆̇͘̚͘͘͝͝͝ͅ ̶̨̛̜̣͇͕̼͍̟̂̆̓̓̈͂͗̓͆͊̄̈́͐̋̄̈̽̋̈͋̌͂̅͘̕͘̚͘͜͠ ̵̡̧̡̻̳̭̩͙̟̬͍͖̣̼͎̣͚̝̭͙̩͔͚͔̐̔̃̀͐̈̈͒̄̊͂̚̕̚͜͝ ̷̧̛̤̞̖̻̪̻̰̬̰̙̦̩̘̫̩̠͙̻͔̟̣̰͚̘̙̙̭̻͚̱̠̟͓͍͎͑́̈́̋́̃̈́͑̂̒͒͂̕͘͜͜ ̵̢̡̢̮̤̠̖̭͔͓̬͉͕̤̯͈̖͍̪̗̼̠͈̞̫̩̜̹̣̥̠͎͍̤̭͕̓̿̄̑͛͒̿̑͊̏͘͘̕͘͜ ̵̡͔̜͔̪̭͖̤̮̠̩̞̥̥̪̠̗̜̪̦̥̳̝̤̼̻̜̰̞͎̯̀͂̃̈́̔̇̋͊̍͗̍̓͛̀̕͜͜͝ ̵̢̢̡̢̢̛͓͇̪̼̟͎͍̙͓̱̱̭̬̱͍̲̰̲̲͚͔͖͚̙͇̥̳̤̪̥̭̜͚͚͉̙͐̇̎̀̈̆̀̌̋̂͒͋̽́͒̆̂͋͗̄́̐̌͐̈́̃̍͑̚͜͝ ̸̨̧̡͈̗͚͓̺̤̥̬̟̬͙̰̪̜̣̠̼̜̩͇͖̱̣̮̠̫̱̜̼̤̮̮̱̪̥̙͕͚̺̱̫̣̈̈́̐̊͊̈͐̍͌̀͂̆̓̑͌̈͗̈́̂͛̌̑̒̈́̾͆͌̊͊͒͗̕͘̕͠͝͝ͅ ̵̡̛̪̠͉͉̹̠̞̝̣̞̭͎͕̤̺̙͇͈̳̙͉̲̇͋͂̄̊͋͒̀͆͌̅͒̃̿̂̍̇͋̏̐̚̕͘͜͜͝͝ ̸̡̧̨̟̟͓͉̩̲͎̲̺̀͒͌̾̇̀̒ ̸̞̞̟̥̮͎͇̘̙̼̣͙̓̈͋͆͛̌͌͗̈̍́̂͊̏̅̒̌̈́́̓̑̃͂̿̑̎͆̿̈͊̾͘̕̕͜͝͝͠͝ ̵͕̻͙͖̼̍͆̑̆̎͆̐̄̈́͐̀̀̏̒́̂̒̂̆͐͆͐͊̔̾̃̋̚̚͠ ̵̨̡̛̤̭̖̩̦͓̠̩̰̦̞̹̹̮͔͈̻͉͚̩̯̲̟̈́͋͂̔̓̌̉̊̉͗̀̽̀̆̇͋͌̈́̽́́̾̐̕̕̚͜͝ͅ ̴̰̭̪̱̗͙̱̥͎̙͕̄͑̀̀̏͐̿͗̉̎͒̔̔̎̽̈́̀̾́͂̌́̌̌́̑̈́͑̀͝͠ ̵̨̢̛̪̯̥̯̯̫͊̆̅͊̑̇̆̈̋̊̿́̄̃̉̔̈́̿͗̅͛͊͌̈̓̓͑̈́̀̅̈̕̚͠ͅ ̸̰̱̗̼͆̈͑͋͑̅̌̋̒̄͒̊̓̍́̈͠͝͠ ̷̧̛͔͇̤̫̮̫̲̼̹̼̮̳͍̟̟̝̠̬̘͙̼̜͎͚͚̫̯̣̣͇̳̻͓̙̪̲͉̟͓̦̜͈͙͕̻̆͛̾͗́͑̿̏̾̾͗̒̌̄͂͒̔̈́͂̂̈́̈̎̽̃̒̆̉͒̆̾̓̑͐̂̚͜͝͝͝ͅ ̷̢̛̰͚̖̙̯̲͕͓̣̹̟̮̖̝͓͚̙̊͗͋̓̊̉̓̃̾̍̔̈́̀̍̈̎̄́͒̓͗̄͘͝ ̴̨̰͇̍ͅ ̸̧̧̧̛̣̰̲̗͔̯̟̳̜̩̮̜̹̺͓̩̘̞͎͎̜̜̩̮̱̼̼͇̠͍͚͕̼̩̥͉̪̪̙̒͐͋͗̋͌̆̓͂̄̌̓͂̿̓͋́̇͌̉̽͆̄̒͊̈́̎̕̚͘̚̕̕͝͠͝ ̵̛̩̖̳̩͎̤͇͖̥͈̦̲̗̰̳̰͔̲̩͚̝̟͓̫̋͌̊͂̽̽̂͆̑͐̂̈́̿̍́͊̄̊̇̄̊̈͗͑͊̆̃̕̕͝͝͝ͅ ̶̡̢̡̛͇̼̺̙͖͕͔̩͔̫̘͎̳̘͕̬̜̝̩̞̘̣̥͖͚̥͙̤͕͖̬̳̪͖̲̞̋̾̀̂̂̂̔̈́͗̉͐̎̄̎͆̈́̑̏̒̊̈́͐̎͛̈̈́̎̿́̾̑̆̽̂̒̏͆̈́̅͊͘͠͝ͅ ̷̧̧̨̱̙̣̼͇̳͕̦̯͈͖̯̼̱̪̭̖̖̹͙̲͎̠̯̰̖̩̫͎͙̫͔͍̭̫̪̩̹̖̰̭̲̰͆͜ ̷̪͕̞͈͓̘̬͉̄͆̀̋̃̈͋̋̐̆̾́͛͆́̉̒̀̀͝͠ ̷̢̢̨̮̗̥̼̝͎̭̣̪̹̯̈́̄͊̄͑͆̐͌̃͆̎̏̓̍͂̉̄̇̈͑̚̚͜ ̴̧̢̧̡̢͇̰̗̼̰͓̞̳̤̹̘̖̤̠̬̼͚̺͔̠̼͔̱̝̠̮͈̤͉̖̰̩̫̓̿̿̈́̑̃͂̈͊͂̀̽̽̂́̓͂̀̾̎͆̔͂͌̅̽̈́̊̿̓͗̍͂͋̄̂̓̚̕̚͘͠͝͝͝͝͠ͅ ̸̡̧̨͕̪̘̫̱̪̲̙̟̹̮͍͇̪̟̖̗͈̻̖͙̠̞̱̖̯̃̔͑̍̌̑̾͌͌͒̉̏̆̓͗͂̿͆̿̚͘͜͜͝͠ͅͅ ̸̨̡̛̛̖̺̲͚͇̲̺͇̼̗͓̭͓͔̘̱̹͍̜̞̺͕̖̽̎͌͒͂̾̇͋͛̑͑̆̏̏̑͒͑͂̈̀́͗̔͊͑̚̕͠͠ͅ ̴̡̧̨̨̧̧̛̛̛̖̳͓̭͚̙͕͇͉̼̦̲̹̲̫̥̠̝̦̰͚̙̺̯̺̖̭̫̻͈̞̼̼̅̋̍̔̆̉̔̓͐̄͐̍̊͆̽̈̑̒̍̑͐̌͊̓͊͑̄̈́̍͋̂̚̕͘͝͝͠͠ͅ ̷̨̧̛̛̛͈̳̗̺̲̹̰͙̖̤̺̪̫̦̬͕̪̠̓̃̉̍̊͐͋͗͒̏̔̋̅̈́̃̎̓͗͋̒̄̓́̈͊̒͒̈͐̔̋̂́̓̌̇̋͛̏̚̕ͅ ̷̨̛̛̛̫̹͍̮̣̘̯̤͔̥̻̥̗̫̙̻̠̹̝̞̥̬̯͚̺̦͎͓̲͉̙̯̱̺̗̤̃͆̎̅̂̊̈̋͒̈́̍͑̆͊̈́̑̾͑̂́̂́̆̂̾̈́̆̐͛͋̋̈́̃̂̂̇̓̀̈́̕͘͜͝͠͝͠͝ ̶̢̰̲͉̪̲̪̤̖̤̦͙̹̲͔̮̘̪̻̩͇͍̙͉̝̱̘̖̣̦̮̱̼̣͚̹̖̥̪͇̫̳̠͙͚̤̓̒̒̑͂̆͋̀̄̎̔͗͌̍ͅͅ ̴̡̧̢̛̙̺̝͍͎̘̞̺͉̲̘͙̞̤̯̮͚̻͖̺͖̪̗̟̣̣͔͚̝̅̎̾͗̌̈̅̆̅̊̋̑͌̐͆͗̕͘̚͝͠͠ͅ ̸̛̛̮̹̬̤͎̣̺̞̤̭̩̰͚̱͇̣̓̀̾̓̋̋̄̎̐͐̅̂̉̽̋̈̈͒̐̇́̀͒̎͑̍̌͐̂͊̎̚͜͜͠͠ ̴̡̨̨̢̢̣̗͍̹͎̱̺͙̤̖̩͈̫͚̰̥̯͔̝͓͇̱͇̳̜̮̺̩̺̻̭̱̗̹͙̻̌̅͆͊̿̃̄̋̃̀̃͐͗͜͝͝͠ͅͅͅ')

    print(repeats - 1)
        
    threading.Timer(1.0, explode).start()
root = tkinter.Tk()
PictureExplosion = tkinter.PhotoImage(file="Assets\Images\Biem.png")
repeats += 1
root.resizable(width=False, height=False)
root.wm_attributes("-transparentcolor","#34aeeb")
root.configure(bg="white")
root.geometry("40x40")
explode()
root.mainloop()

