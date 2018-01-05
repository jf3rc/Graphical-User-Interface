#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Jan  5 00:16:39 2018

@author: Jason
"""

# https://stackoverflow.com/questions/17285973/reset-textboxes-in-python
# Reset textboxes in python with index at "1.0"

# Issues (simplified version on github)

from tkinter import *

window=Tk()

window.wm_title("Temperature Converter")

def from_fahrenheit():
    celsius = (float(e3_value.get()) - 32) * (9/5)
    t1.delete("1.0", END)
    t1.insert(END,celsius)
    
def from_celsius():
    fahrenheit  = (float(e4_value.get()) * (9/5)) + 32
    t2.delete("1.0", END)
    t2.insert(END, fahrenheit)

e1 = Label(window,text = "Degrees")
e1.grid(row = 0, column = 1)

e2 = Label(window,text = "Fahrenheit")
e2.grid(row = 1, column = 1)

e3_value = StringVar()
e3 = Entry(window, textvariable = e3_value)
e3.grid(row = 0, column = 0)

e4_value = StringVar()
e4 = Entry(window, textvariable = e4_value)
e4.grid(row = 1, column = 3)

e5 = Label(window, text = "Degrees")
e5.grid(row = 0, column = 4)

e6 = Label(window, text = "Celsius")
e6.grid(row = 1, column = 4)

b1 = Button(window, text = "Convert -->", command = from_fahrenheit)
b1.grid(row = 0, column = 2)

b2 = Button(window, text = "<-- Convert", command = from_celsius)
b2.grid(row = 1, column = 2)

t1 = Text(window, height = 1.35, width = 26)
t1.grid(row = 0, column = 3)

t2 = Text(window, height = 1.35, width = 26)
t2.grid(row = 1, column = 0)

window.mainloop()