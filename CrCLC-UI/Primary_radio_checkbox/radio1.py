# -*- coding: UTF-8 -*-


import tkinter as tk
from tkinter import ttk
import tkinter.messagebox
from PIL import Image, ImageTk


top_win = tk.Tk()
top_win.title('Hello world Stanford')
win_size_pos = '1366x768'
top_win.geometry(win_size_pos)
frame_root1 = tk.Frame(top_win, bg="green", width=760, heigh=200)
frame_root1.place(x=20, y=20)

var_sel = tk.IntVar()
var_sel.set(1)
radio_btn1 = tk.Radiobutton(
    frame_root1,
    text='one',
    value=1,
    variable=var_sel,
    bg='green',
    fg='red',
    command=None
)
radio_btn1.place(x=20, y=20)


radio_btn2 = tk.Radiobutton(
    frame_root1,
    text='two',
    value=2,
    variable=var_sel,
    bg='green',
    fg='red',
    command=None
)
radio_btn2.place(x=150, y=20)

radio_btn3 = tk.Radiobutton(
    frame_root1,
    text='Three',
    value=3,
    variable=var_sel,
    bg='green',
    fg='red',
    command=None
)
radio_btn3.place(x=85, y=20)

top_win.mainloop()
