# -*- coding: UTF-8 -*-


import tkinter as tk
from tkinter import ttk
import tkinter.messagebox
from PIL import Image, ImageTk

top_win = tk.Tk()
top_win.title('windows')
win_size_pos = '800x600'
top_win.geometry(win_size_pos)
title = 'My label frame'
lfm_step1 = ttk.Labelframe(
    top_win, text=title, width=240, height=260
)
lfm_step1.grid(row=0, column=0, pady=10)
lbl_test0 = tk.Label(lfm_step1, text='oh my god', bg='blue', fg='white')
lbl_test0.grid(row=0, column=0, pady=10)
lbl_test1 = tk.Label(lfm_step1, text='oh my god', bg='blue', fg='white')
lbl_test1.grid(row=1, column=0, pady=10)
lbl_test2 = tk.Label(lfm_step1, text='oh my god', bg='blue', fg='white')
lbl_test2.grid(row=2, column=0, pady=10)
title = 'AHHHHHHHHH'
lfm_step2 = ttk.Labelframe(
    top_win, text=title, width=240, height=500
)
lfm_step2.grid(row=0, column=1, pady=10)
ent_row = tk.Entry(lfm_step2, show=None, width=8, bg='red', fg='white'
                   )
ent_row.grid(row=0, column=0, pady=10)
ent_row1 = tk.Entry(lfm_step2, show=None, width=8, bg='red', fg='white'
                    )
ent_row1.grid(row=1, column=0, pady=10)
ent_row2 = tk.Entry(lfm_step2, show=None, width=8, bg='red', fg='white'
                    )
ent_row2.grid(row=2, column=0, pady=10)


top_win.mainloop()
