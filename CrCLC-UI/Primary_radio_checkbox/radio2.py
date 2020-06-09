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
text_of_btn =('A','B','C','D')
value_of_btn=(0,1,2,3)

def show_selected():
    v=var_sel.get()
    print(text_of_btn[v])

    return

for idx in range(4):
    chk_btn = tk.Radiobutton(
        frame_root1,
        variable=var_sel,
        text=text_of_btn[idx],
        value=value_of_btn[idx],
        command=show_selected
    )
    chk_btn.place(x=20 + idx * 190, y=40)

top_win.mainloop()
