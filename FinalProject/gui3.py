from tkinter import *
from PIL import Image, ImageTk
import module

class GUI:
    def __init__(self, window):
        self.window = window

        # Left Frame
        self.frameLeft = Frame(self.window, bd=1, width=500, height=767, highlightbackground="blue", highlightthickness=2)
        self.frameLeft.grid(row=0, column=0, padx=(10,5), pady=10)
        self.frameLeft.pack_propagate(False)

        # Right Frame
        self.frameRight = Frame(self.window, bd=1, width=910, height=767, highlightbackground="blue", highlightthickness=2)
        self.frameRight.grid(row=0, column=1, padx=(5,10), pady=10)
        self.frameRight.pack_propagate(False)

        # Image
        self.image = ImageTk.PhotoImage(Image.open('tigerFace.jpeg').resize((612, 408)))
        self.label = Label(self.frameRight, image=self.image)
        self.label.pack(pady=(170, 0))

        # Grayscale Button
        self.buttonGrayscale = Button(self.frameLeft, text='Grayscale', width=100, height=3)
        self.buttonGrayscale.pack()
