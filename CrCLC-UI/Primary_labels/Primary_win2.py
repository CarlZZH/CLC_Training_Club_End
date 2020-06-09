# -*- coding: UTF-8 -*-


import tkinter as tk
from tkinter import ttk
from PIL import Image,ImageTk

top_win = tk.Tk(
)
top_win.title('Hello world Stanford'
)
win_size_pos = '1366x768'
top_win.geometry(win_size_pos
)

lbl_Hello=tk.Label(
    top_win,#隶属的父窗口
    text='Hello Le_Stanford',
    bg='green',
    fg='red',
    font=('Arial,22'),
    width=17,
    height=8
)
lbl_Hello.pack(
)

image=Image.open('images.png')
bk_img=ImageTk.PhotoImage(image)
lbl_bk=tk.Label(top_win,image=bk_img)
lbl_bk.place(x=100,y=300,width=600,height=300
)
top_win.mainloop(
)
