from tkinter import *
from tkinter import ttk

root = Tk()
root.title("Calculadora")
root.geometry('600x500')
root.minsize(600, 500)
root.maxsize(600, 500)

root.configure(background='#282828')

e = Entry(root, width=15, borderwidth=4, relief=FLAT,fg='#FFFFFF', bg='#a7a28f', font =('futura', 25, 'bold'), justify=CENTER )
e.grid(
    row=0,
    column=0,
    columnspan=4,
    pady=2
)

root.mainloop()