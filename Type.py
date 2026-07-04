from tkinter import *

root = Tk()

type = Label(root, text="Type Anything", font=("Arial", 30))
type.grid(row=0, column=0)
type = Entry(root, font=("Arial", 50))
type.grid(row=1, column=0)

def show():
    show.config(text=type.get())

but = Button(root, text="Enter", font=("Arial", 10), command=show)
but.grid(row=2, column=0)

show = Label(root, font=("Arial", 20))
show.grid(row=4, column=0)

root.mainloop()