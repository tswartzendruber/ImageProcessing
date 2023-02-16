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
        self.labelImage = Label(self.frameRight, image=self.image)
        self.labelImage.pack(pady=(170, 0))

        # Original Button
        self.buttonOriginal = Button(self.frameLeft, text='Original', width=100, height=3, command=self.original)
        self.buttonOriginal.pack()

        # Grayscale Button
        self.buttonGrayscale = Button(self.frameLeft, text='Grayscale', width=100, height=3, command=self.grayscale)
        self.buttonGrayscale.pack()

        # Rotate 180 Button
        self.buttonRotate180 = Button(self.frameLeft, text='Rotate180', width=100, height=3, command=self.rotate180)
        self.buttonRotate180.pack()
    
    def original(self):
        module.main('original')
        self.newImage = ImageTk.PhotoImage(Image.open('done.png').resize((612, 408)))
        self.labelImage.config(image=self.image)

    def grayscale(self):
        module.main('grayscale')
        self.newImage = ImageTk.PhotoImage(Image.open('done.png').resize((612, 408)))
        self.labelImage.config(image=self.newImage)
    
    def rotate180(self):
        module.main('rotate180')
        self.newImage = ImageTk.PhotoImage(Image.open('done.png').resize((612, 408)))
        self.labelImage.config(image=self.newImage)
