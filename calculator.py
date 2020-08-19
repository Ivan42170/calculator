# -*- coding: utf-8 -*-
"""
Created on Wed Aug 19 09:35:43 2020

@author: Ivan
"""

from tkinter import *
calcul = 0
root = Tk()
l1 = Label(text = '0')
b0 = Button(text="0", width=10, height=4)
b1 = Button(text="1", width=10, height=4)
b2 = Button(text="2", width=10, height=4)
b3 = Button(text="3", width=10, height=4)
b4 = Button(text="4", width=10, height=4)
b5 = Button(text="5", width=10, height=4)
b6 = Button(text="6", width=10, height=4)
b7 = Button(text="7", width=10, height=4)
b8 = Button(text="8", width=10, height=4)
b9 = Button(text="9", width=10, height=4)
b10 = Button(text="+", width=10, height=4)
b11 = Button(text="-", width=10, height=4)
b12 = Button(text="*", width=10, height=4)
b13 = Button(text=":", width=10, height=4)
b14 = Button(text="CE", width=10, height=4)
b15 = Button(text="=", width=10, height=4)
l1.place(x=530, y=0)
b0.place(x=600, y=260)
b1.place(x=520, y=190)
b2.place(x=600, y=190)
b3.place(x=680, y=190)
b4.place(x=520, y=120)
b5.place(x=600, y=120)
b6.place(x=680, y=120)
b7.place(x=520, y=50)
b8.place(x=600, y=50)
b9.place(x=680, y=50)
b10.place(x=760, y=260)
b11.place(x=760, y=190)
b12.place(x=760, y=50)
b13.place(x=760, y=120)
b14.place(x=520, y=260)
b15.place(x=680, y=260)
root.mainloop()