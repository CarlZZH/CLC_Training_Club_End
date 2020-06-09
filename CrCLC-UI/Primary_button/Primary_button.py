# -*- coding: UTF-8 -*-


import tkinter as tk
from tkinter import ttk
import tkinter.messagebox
from PIL import Image, ImageTk

top_win = tk.Tk()
top_win.title('Hello world Stanford')
win_size_pos = '1366x768'
top_win.geometry(win_size_pos)


def cmd_print():
    print('Oh,no,you should kill the BOSS first!~')
    return


def cmd_pop():
    tk.messagebox.showinfo(title='Good News', message='WIN')
    return


# btn_game=tk.Button(top_win,text='click me for level up!',
# command=cmd_pop
# )
# btn_game.pack()

#button_relieves = ('flat', 'groove', 'raised', 'ridge', 'solid', 'sunken')
# for r in button_relieves:
    # tk.Button(top_win,text=r,relief=r,width=10,height=2).pack()

image = Image.open('images.png')
bk_img = ImageTk.PhotoImage(image)
btn_try_pic = tk.Button(top_win,
                        text='BIG BOSS',
                        compound='center',
                        image=bk_img,
                        command=cmd_pop
                        )
btn_try_pic.pack()


top_win.mainloop()
