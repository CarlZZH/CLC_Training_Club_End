# -*- coding: UTF-8 -*-


import tkinter as tk
from tkinter import ttk
import tkinter.messagebox
from PIL import Image,ImageTk


top_win = tk.Tk()
top_win.title('Hello world Stanford')
win_size_pos = '1366x768'
top_win.geometry(win_size_pos)

def cmd_undo():
    tk.messagebox.showinfo(title='Info',message='Undo sth')
    return
def cmd_redo():
    tk.messagebox.showinfo(title='Info',message='Undo sth')
    return
menubar=tk.Menu(top_win)
menubar.add_command(label='Undo',command=cmd_undo)
menubar.add_command(label='Redo',command=cmd_redo)

frame=tk.Frame(top_win,width=400,height=400,bg='green')
frame.pack()

def popup(event):
    menubar.post(event.x_root,event.y_root)
frame.bind("<Button-3>",popup)

top_win.mainloop()
