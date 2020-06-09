# -*- coding: UTF-8 -*-


import tkinter as tk
from tkinter import ttk
import tkinter.messagebox
from PIL import Image,ImageTk


top_win = tk.Tk()
top_win.title('Hello world Stanford')
win_size_pos = '1366x768'
top_win.geometry(win_size_pos)


frame_root1=tk.Frame(top_win,bg="green",width=760,heigh=200)
frame_root1.place(x=20,y=20)
lbl_test=tk.Label(frame_root1,text='text in frame')
lbl_test.place(x=20,y=20)
top_win.mainloop()
