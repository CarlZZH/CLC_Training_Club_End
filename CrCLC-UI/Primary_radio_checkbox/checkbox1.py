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
text_of_btn = ('1', '2', '3', '4')
v1 = tk.IntVar()
v2 = tk.IntVar()
v3 = tk.IntVar()
v4 = tk.IntVar()
value_of_btn = (v1, v2, v3, v4)
'''
cnk_btn1=tk.Checkbutton(
        frame_root1,
        text=text_of_btn[0],
        variable=value_of_btn[0],
        command=None
)
cnk_btn1.place(x=20,y=20)
'''


def show_selected():
    print('GOD'
          )
    for l in value_of_btn:
        print(l.get())
    return


for idx in range(4):
    chk_btn = tk.Checkbutton(
        frame_root1,
        text=text_of_btn[idx],
        variable=value_of_btn[idx],
        command=show_selected
    )
    chk_btn.place(x=20 + idx * 190, y=40)


top_win.mainloop()
