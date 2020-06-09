# -*- coding: UTF-8 -*-


import tkinter as tk
from tkinter import ttk

top_win = tk.Tk()
top_win.title('Hello world Stanford')
win_size_pos = '1366x768'
top_win.geometry(win_size_pos)

entry_cleartext = tk.Entry(
    top_win,
    show=None,
    bg='green',
    fg='red',
    width=50,
    font=('Arial', 14)
    # 显示成明文形式
)
entry_cleartext.place(x=520,y=85,width=85)

entry_advanced_cleartext=tk.Text(top_win,height=22)
entry_advanced_cleartext.place(x=850,y=222,width=622)

top_win.mainloop()
