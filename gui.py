#simple python Hello World gui with Tkinter
from tkinter import *       # type: ignore
root = Tk()
#creating a label widget
myLabel = Label(root, text="Hello World!")
#displaying on screen
myLabel.pack()
#looping the program to be seen
root.mainloop()