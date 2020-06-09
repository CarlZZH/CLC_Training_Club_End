# -*- coding: UTF-8 -*-


import tkinter as tk
from tkinter import ttk
import tkinter.messagebox
from PIL import Image, ImageTk

top_win = tk.Tk()
top_win.title('windows')
win_size_pos = '800x600'
top_win.geometry(win_size_pos)
lbl_background=tk.Label(
    top_win,
    text='AAAAA',
    bg='blue'
)
image=Image.open('CISI.png')
bk_img=ImageTk.PhotoImage(image)
lbl_background=tk.Label(top_win,image=bk_img,text='KKK')
lbl_background.place(x=0,y=0,width=800,height=600)
top_win.mainloop()
