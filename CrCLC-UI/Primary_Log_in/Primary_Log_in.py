# -*- coding: UTF-8 -*-



import tkinter as tk
from tkinter import ttk
import tkinter.messagebox
from PIL import Image,ImageTk
import math

def cmd_pop():
    tk.messagebox.showinfo(title='Good News', message='LOG IN successfully')
    return
def new_window():
    Log_in_window=tk.Label(
    top_win,
    text='Log in',
    font='Arial,17',
    width=520,
    height=321
    )
    Log_in_window.pack()
    entry_cleartext = tk.Entry(
        Log_in_window,
        show=None,
        bg='green',
        fg='red',
        width=50,
        font=('Arial', 17)
    )
    entry_cleartext.pack()
    return


Top_win=tk.Tk(
)
Top_win.title('Log in')
win_size_pos = '1366x768'
Top_win.geometry(win_size_pos)


lbl_Hello=tk.Label(
    Top_win,#隶属的父窗口
    text='Log in window',
    bg='green',
    fg='red',
    font=('Arial,22'),
    width=17,
    height=8
)
lbl_Hello.pack(
)

pwd_username = tk.Entry(
    Top_win,
    show=None,
    bg='green',
    fg='red',
    width=100,
    font=('Arial', 14),
    # 显示成明文形式
)
pwd_username.place(x=300,y=200,width=400)




pwd_pwd = tk.Entry(
    Top_win,
    show=None,
    bg='green',
    fg='red',
    width=100,
    font=('Arial', 14),
    # 显示成明文形式
)
pwd_pwd.place(x=300,y=300,width=400)



def pwd_check():
    pwd_username=pwd_username.get()
    pwd_pwd=pwd_pwd.get()
    if pwd_username!='CARL':
        tk.messagebox.showinfo(title='BAD News', message='LOG IN failed')
    elif pwd_pwd!='32994':
        tk.messagebox.showinfo(title='BAD News', message='LOG IN failed')
    else:
        tk.messagebox.showinfo(title='Good News', message='LOG IN successfully')
    return

btn_Log_in=tk.Button(Top_win,text='Log in',
 command=pwd_check
)
btn_Log_in.place(x=400,y=400,width=88)


#place(x=683,y=384,width=100)

#top_win = tk.Label(
    #Top_win,
    #text='Log in',
    #bg='yellow',
    #font='Arial,22',
    #width=1366,
    #height=768
#)


#top_win.place(x=0,y=0,width=1366,height=768)


#btn_Log_in=tk.Button(top_win,text='Log in',command=new_window)
#btn_Log_in.pack()#place(x=600,y=400,width=22,height=17)


#top_win.title('Log in')
#win_size_pos = '520x321'
#top_win.geometry(win_size_pos)




Top_win.mainloop()
