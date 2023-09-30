import tkinter

try:
    from TkinterDnD2 import *
    root = TkinterDnD.Tk()
    root.withdraw()
    def getroot(*a,**b):
        return root
    tkinter.Tk = getroot
except Exception as e:
    print("TkinterDnD2 not installed",e)

import TextPlus
tkinter.Text = TextPlus.TextPlus

import idlelib.__main__
