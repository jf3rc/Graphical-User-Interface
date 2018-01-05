#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Jan  4 23:10:27 2018

@author: Jason
"""

# https://stackoverflow.com/questions/17285973/reset-textboxes-in-python
# Reset textboxes in python with index at "1.0"

from tkinter import *

window=Tk()

window.wm_title("Fahrenheit to Celsius Converter")

def from_fahrenheit():
    celsius = (float(e2_value.get()) - 32)* (9/5)
    t1.delete("1.0", END)
    t1.insert(END,celsius)

e1=Label(window,text="Degrees Fahrenheit")
e1.grid(row=0,column=1)

e2_value = StringVar()
e2 = Entry(window,textvariable = e2_value)
e2.grid(row=0,column=0)

b1=Button(window,text="Convert To",command=from_fahrenheit)
b1.grid(row=0,column=2)

t1=Text(window,height=1,width=20)
t1.grid(row=0,column= 3)

e3 = Label(window, text = "Degrees Celsius")
e3.grid(row = 0, column = 4)

window.mainloop()