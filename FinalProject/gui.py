from tkinter import *
from PIL import Image, ImageTk
import module

class GUI:
    def __init__(self, window):
        self.window = window

        # Column on the left containing different methods
        self.frameLeft = Frame(self.window, background='grey', width=500, height=767)
        self.frameLeft.grid(padx=(10, 5), pady=10, row=0, column=0)

        # Image frame on the right
        self.frameRight = Frame(self.window, background='light grey', width=910, height=767)
        self.frameRight.grid(padx=(5, 10), pady=10, row=0, column=1)

        # The Image
        self.image = ImageTk.PhotoImage(Image.open('tigerFace.jpeg').resize((612, 408)))
        self.labelImage = Label(self.frameRight, image=self.image, background='light grey', anchor='center').place(x=90, y=70, relwidth=.8, relheight=.8)
'''
        # Grayscale Button
        self.buttonGrayscale = Button(self.frameLeft, text='Grayscale', command=self.adjustImage(0))
        self.buttonGrayscale.pack()

    def adjustImage(self, method):
        if method == 1:
            module.main('original')
            self.newImage = ImageTk.PhotoImage(Image.open('done.png').resize((612, 408)))
            self.labelImage.config(image=self.newImage)
'''