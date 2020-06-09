# -*- coding: UTF-8 -*-


import tkinter as tk
from tkinter import ttk
import tkinter.messagebox
from PIL import Image, ImageTk
from gui_class_login1 import UC_show
from gui_class_login import UC_login

root = tk.Tk()
form_login = UC_login(root)


root.mainloop()
root.destroy()

root = tk.Tk()
form_show = UC_show(root)
root.mainloop()
