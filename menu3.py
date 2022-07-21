#!/usr/bin/python
import sys
import sys
import os
from tkinter import *
import tkinter as tk

root = tk.Tk()
top=tkinter.tk()

def helloCallBack():
    os.system('python menu.py')

B=Tkinter.Button(top,text="hello",command= helloCallBack)
B.pack()
top.mainloop()