import tkinter
from tkinter import *

window = Tk()
window.title("Basic Calculator")

e = Entry(window, width = 45, borderwidth = 5)
e.grid(row=0, column = 0, columnspan= 3, padx = 10, pady = 10)

def buttonclick(number):
    current = e.get()
    e.delete(0, END)
    e.insert(0, str(current)+str(number))

def button_clear():
    e.delete(0, END) 

def button_add():
    first_number = e.get()
    global f_num
    global math 
    math = "addition"
    f_num = int(first_number)
    e.delete(0,END)

def button_sub():
    first_number = e.get()
    global f_num
    global math 
    math = "subtraction"
    f_num = int(first_number)
    e.delete(0,END)

def button_mul():
    first_number = e.get()
    global f_num
    global math 
    math = "multiplication"
    f_num = int(first_number)
    e.delete(0,END)

def button_divide():
    first_number = e.get()
    global f_num
    global math 
    math = "division"
    f_num = int(first_number)
    e.delete(0,END)            

def button_equal():
    second_number = e.get()
    e.delete(0,END)

    if math == "addition":
        e.insert(0, f_num + int(second_number))

    if math == "subtraction":
        e.insert(0, f_num - int(second_number))

    if math == "multiplication":
        e.insert(0, f_num * int(second_number))

    if math == "division":
        e.insert(0, f_num / int(second_number))            

button1 = Button(window, text="1",padx =40 ,pady = 20, command = lambda: buttonclick(1))
button2 = Button(window, text="2", padx =40 ,pady = 20,command = lambda: buttonclick(2))
button3 = Button(window, text="3", padx =40 ,pady = 20,command = lambda: buttonclick(3))
button4 = Button(window, text="4", padx =40 ,pady = 20,command = lambda: buttonclick(4))
button5 = Button(window, text="5", padx =40 ,pady = 20,command = lambda: buttonclick(5))
button6 = Button(window, text="6", padx =40 ,pady = 20,command = lambda: buttonclick(6))
button7 = Button(window, text="7", padx =40 ,pady = 20,command = lambda: buttonclick(7))
button8 = Button(window, text="8", padx =40 ,pady = 20,command = lambda: buttonclick(8))
button9 = Button(window, text="9", padx =40 ,pady = 20,command = lambda: buttonclick(9))
button0 = Button(window, text="0", padx =40 ,pady = 20,command = lambda: buttonclick(0))
button_add = Button(window, text="+", padx =39 ,pady = 20,command = button_add)
button_equal = Button(window, text="=", padx =91 ,pady = 20,command =  button_equal)
button_clear = Button(window, text="clear", padx =79 ,pady = 20,command = button_clear)

button_sub = Button(window, text="-", padx =41 ,pady = 20,command = button_sub)
button_mul = Button(window, text="*", padx =40 ,pady = 20,command = button_mul)
button_divide = Button(window, text="/", padx =41 ,pady = 20,command = button_divide)

button7.grid(row = 1 , column =0 )
button8.grid(row = 1 , column =1 )
button9.grid(row = 1 , column =2 )

button4.grid(row = 2 , column =0 )
button5.grid(row = 2 , column =1 )
button6.grid(row = 2 , column =2 )

button3.grid(row = 3 , column =0 )
button2.grid(row = 3 , column =1 )
button1.grid(row = 3 , column =2 )

button0.grid(row = 4 , column =0 )
button_clear.grid(row = 4, column = 1, columnspan= 2)
button_add.grid(row = 5, column = 0)
button_equal.grid(row = 5, column = 1, columnspan= 2)

button_sub.grid(row = 6, column = 0)
button_mul.grid(row = 6, column = 1)
button_divide.grid(row = 6, column = 2)



window.mainloop()
