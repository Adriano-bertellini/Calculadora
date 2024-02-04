from tkinter import *
from tkinter import ttk

root = Tk()
root.title("Calculadora")
root.geometry('408x305')
root.minsize(408, 305)
root.maxsize(408, 305)

root.configure(background='#282828')

e = Entry(root, width=15, borderwidth=4, relief=FLAT,fg='#282828', bg='#EEDFCC', font =('futura', 25, 'bold'), justify=CENTER )
e.grid(
    row=0,
    column=0,
    columnspan=4,
    pady=2
)

def button_division():
    return
divide = Button(root,
                text='÷',
                bg= '#EEDFCC',
                padx=40,
                pady=20,
                command=button_division(),
                fg='#282828',
                activebackground='#282828',
                activeforeground='#240046',
                relief=FLAT,
                font=('futura', 12, 'bold')
)
divide.grid(row=0, column=4)

root.mainloop()