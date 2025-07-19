#Rpg game

import tkinter

#Window:

window = tkinter.Tk()
window.title("RPG game")
window.geometry("720x1290")

def onClick():
    print("Start")

start = tkinter.Button(window, text="Start", command=onClick)
start.pack()
window.mainloop()
