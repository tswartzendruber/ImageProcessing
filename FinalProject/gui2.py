from tkinter import *
from PIL import Image, ImageTk
import module

class GUI:
    def __init__(self, window):
        self.window = window

        self.frameLeft = Frame(self.window, bg='red', width=200, height=200)
        self.frameLeft.pack(side=LEFT, padx=10, pady=10)

        self.frameRight = Frame(self.window, bg='blue')
        self.frameRight.pack(side=RIGHT)

        self.labelLeft1 = Label(self.frameLeft, text='Left Frame 1', bg='red')
        self.labelLeft1.pack(padx=100, pady=100)

        self.labelLeft2 = Label(self.frameLeft, text='Left Frame 2', bg='red')
        self.labelLeft2.pack(padx=100, pady=100)

'''
        self.labelRight = Label(self.frameRight, text='Right Frame')
        self.labelRight.pack()
        '''