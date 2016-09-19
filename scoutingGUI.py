# scoutingGUI.py
# uses Tkinter...

from tkinter import *
from PIL import ImageTk, Image

path = "/Users/gwc/Desktop/Python/Scouting/StrongholdField.png"

root = Tk() # main loop
root.title("Scouting")

frame = Frame(root, width = 1250, height = 580)
frame.pack()

img = ImageTk.PhotoImage(Image.open(path))
# img = img.resize((1250, 480), Image.ANTIALIAS)
background = Label (root, image = img)
# background.pack(side = TOP)
background.place(x=0, y=0, relwidth=1, relheight=1)

root.mainloop()