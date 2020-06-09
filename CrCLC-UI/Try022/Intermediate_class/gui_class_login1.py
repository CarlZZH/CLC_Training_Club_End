# -*- coding: UTF-8 -*-


import tkinter as tk
from tkinter import ttk
import tkinter.messagebox
from PIL import Image, ImageTk


class UC_show:
    def __init__(self, pwin):
        print('UC_show has created!!!')
        self.parent_win = pwin
        self.parent_win.title('show_by class')
        win_size_pos = '1314x805'
        self.parent_win.geometry(win_size_pos)
        self.__init_widgets()

        return

    def __init_widgets(self):
        self.lbl_info = tk.Label(
            self.parent_win,
            text='show form',
            anchor="w",
            justify="left",
            bg='#ceceff',
            fg='white',
            height=1
        )
        self.lbl_info.place(x=20, y=20, width=200)
'''
        # Step2:
        default_var = tk.StringVar(value='username')
        self.ent_username = tk.Entry(
            self.parent_win,
            show=None,
            textvariable=default_var,
        )
        self.ent_username.place(x=20, y=60, width=200)

        default_var = tk.StringVar(value='password')
        self.ent_password = tk.Entry(
            self.parent_win,
            show='*',
            textvariable=default_var,
        )
        self.ent_password.place(x=20, y=100, width=200)
        self.btn_login = tk.Button(
            self.parent_win,
            text='Sign in ',
            relief='raised',
            width=10, height=2,
            bg='#ceceff',  fg='white',
            command=self.__cmd_login,
        )
        self.btn_login.place(x=20, y=140, width=50)

        default_var = tk.StringVar(value='password')
        self.ent_password = tk.Entry(
            self.parent_win,
            show='*',
            textvariable=default_var,
        )
        self.ent_password.place(x=20, y=100, width=200)

        return

    def __cmd_login(self):
        print(self.ent_username.get())
        print(self.ent_password.get())
        u = self.ent_username.get()
        p = self.ent_password.get()

        if u == 'admin' and p == '666':
            tk.messagebox.showinfo(title='Information', message='Successed!')
            self.login_status='OK'
            self.parent_win.quit()
        else:
            tk.messagebox.showerror(title='Information',
                                    message='Wrong username or password')
            self.login_status='NO'

            return
'''
