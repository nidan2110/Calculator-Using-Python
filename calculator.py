import math
from tkinter import *
root = Tk()
root.title("Calculator")
root.config(bg="#f6fff4")

#TEXTBOX
e = Entry(root, width=40, borderwidth=1)
e.grid(row=0, column=0, columnspan=3, padx=10,pady=10)

#FUNCTIONS FOR BUTTONS
def button_click(number):
    new_number = e.get() + str(number)
    e.delete(0, END)
    e.insert(0, new_number)


def button_clear():
    e.delete(0, END)

def button_add():
    first_number = e.get()
    global f_num
    global math  
    math = "addition"
    f_num = int(first_number)
    e.delete(0, END)
    return    
       
def button_equal():
    second_number = e.get()
    e.delete(0, END)

    if math == "addition":
        e.insert(0, f_num + int(second_number))

    if math == "substraction":
        e.insert(0, f_num - int(second_number))

    if math == "divison":
        e.insert(0, f_num / int(second_number))

    if math == "multiplication":
        e.insert(0, f_num * int(second_number))            

def button_subsract():
    first_number = e.get()
    global f_num
    global math
    math = "substraction" 
    f_num = int(first_number)
    e.delete(0, END)

def button_divison():
    first_number = e.get()
    global f_num
    global math
    math = "divison" 
    f_num = int(first_number)
    e.delete(0, END)  

def button_multiply():
    first_number = e.get()
    global f_num
    global math
    math = "multiplication" 
    f_num = int(first_number)
    e.delete(0, END)
 

#BUTTONS
button_1 = Button(root, text="1", padx=40, pady=20, command=lambda: button_click(1))
button_2 = Button(root, text="2", padx=40, pady=20, command=lambda: button_click(2))
button_3 = Button(root, text="3", padx=40, pady=20, command=lambda: button_click(3))
button_4 = Button(root, text="4", padx=40, pady=20, command=lambda: button_click(4))
button_5 = Button(root, text="5", padx=40, pady=20, command=lambda: button_click(5))
button_6 = Button(root, text="6", padx=40, pady=20, command=lambda: button_click(6))
button_7 = Button(root, text="7", padx=40, pady=20, command=lambda: button_click(7))
button_8 = Button(root, text="8", padx=40, pady=20, command=lambda: button_click(8))
button_9 = Button(root, text="9", padx=40, pady=20, command=lambda: button_click(9))
button_0 = Button(root, text="0", padx=40, pady=20, command=lambda: button_click(0))
button_adds = Button(root, text="+", padx=39, pady=20, command=button_add)
button_equ = Button(root, text="=", padx=91, pady=20, command=button_equal)
button_clr = Button(root, text="Clear", padx=79, pady=20, command=button_clear)

button_subtract = Button(root, text="-", padx=41, pady=20, command=button_subsract)
button_multply = Button(root, text="*", padx=40, pady=20, command=button_multiply)
button_divide = Button(root, text="/", padx=41, pady=20, command=button_divison)

#BUTTONS POSITIONS
button_1.grid(row=3, column=0)
button_2.grid(row=3, column=1)
button_3.grid(row=3, column=2)

button_4.grid(row=2, column=0)
button_5.grid(row=2, column=1)
button_6.grid(row=2, column=2)

button_7.grid(row=1, column=0)
button_8.grid(row=1, column=1)
button_9.grid(row=1, column=2)

button_0.grid(row=4, column=0)
button_clr.grid(row=4, column=1, columnspan=2)
button_adds.grid(row=5, column=0)
button_equ.grid(row=5, column=1, columnspan=2)

button_subtract.grid(row=6, column=0)
button_multply.grid(row=6, column=1)
button_divide.grid(row=6, column=2)

root.mainloop()