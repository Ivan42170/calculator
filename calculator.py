# -*- coding: utf-8 -*-
"""
Created on Wed Aug 19 09:35:43 2020

@author: Ivan
"""

from tkinter import *
calcul = 0

root = Tk()
root.geometry('445x355+250+250')
root.resizable(width=False, height=False)

entry_text = StringVar()
e1 = Entry(root, width= 26, bd = 10, font = 'Arial 16', textvariable = entry_text)
b0 = Button(text="0", width=10, height=4)
#b0 = Button(text="0", width=10, height=4, activebackground='red', bg = '#cacaca', command=lambda x: )
b1 = Button(text="1", width=10, height=4)
b2 = Button(text="2", width=10, height=4)
b3 = Button(text="3", width=10, height=4)
b4 = Button(text="4", width=10, height=4)
b5 = Button(text="5", width=10, height=4)
b6 = Button(text="6", width=10, height=4)
b7 = Button(text="7", width=10, height=4)
b8 = Button(text="8", width=10, height=4)
b9 = Button(text="9", width=10, height=4)
b_plus = Button(text="+", width=10, height=4)
b_minus = Button(text="-", width=10, height=4)
b_mul = Button(text="*", width=10, height=4)
b_dif = Button(text=":", width=10, height=4)
b_del = Button(text="CE", width=10, height=4)
b_eq = Button(text="=", width=10, height=4)
b_sing = Button(text="+/-", width=10, height=4)
b_dot = Button(text=',', width=10, height=4)

top_space = 50
button_width = 85
button_height = 75
left_space = 10
right_space = 10

e1.place(x=0+left_space, y=0, width=5*button_width-5 )
b0.place(x=left_space+button_width*1, y=top_space+button_height*3)
b1.place(x=left_space+button_width*0, y=top_space+button_height*2)
b2.place(x=left_space+button_width*1, y=top_space+button_height*2)
b3.place(x=left_space+button_width*2, y=top_space+button_height*2)
b4.place(x=left_space+button_width*0, y=top_space+button_height*1)
b5.place(x=left_space+button_width*1, y=top_space+button_height*1)
b6.place(x=left_space+button_width*2, y=top_space+button_height*1)
b7.place(x=left_space+button_width*0, y=top_space+button_height*0)
b8.place(x=left_space+button_width*1, y=top_space+button_height*0)
b9.place(x=left_space+button_width*2, y=top_space+button_height*0)
b_plus.place(x=left_space+button_width*3, y=top_space+button_height*3)
b_minus.place(x=left_space+button_width*3, y=top_space+button_height*2)
b_del.place(x=left_space+button_width*3, y=top_space+button_height*0, width=2*button_width-5)
b_dif.place(x=left_space+button_width*3, y=top_space+button_height*1)
b_mul.place(x=left_space+button_width*0, y=top_space+button_height*3)
b_sing.place(x=left_space+button_width*2, y=top_space+button_height*3)
b_eq.place(x=left_space+button_width*4, y=top_space+button_height*2, height=2*button_height-5)
b_dot.place(x=left_space+button_width*4, y=top_space+button_height*1)

root.mainloop()