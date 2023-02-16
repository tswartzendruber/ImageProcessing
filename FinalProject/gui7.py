from tkinter import *
from PIL import Image, ImageTk
import module4

class GUI:
    def __init__(self, window):
        self.window = window

        # Left Frame
        self.frameLeft = Frame(self.window, bd=1, width=500, height=767, highlightbackground="black", highlightthickness=2, background='#FFAE42')
        self.frameLeft.grid(row=0, column=0, padx=(10,5), pady=10)
        self.frameLeft.pack_propagate(False)

        # Right Frame
        self.frameRight = Frame(self.window, bd=1, width=910, height=767, highlightbackground="black", highlightthickness=2, background='#FEFECE')
        self.frameRight.grid(row=0, column=1, padx=(5,10), pady=10)
        self.frameRight.pack_propagate(False)

        # Gradient Image
        self.gradient = Image.open('./Images/gradient.jpeg')
        self.gradient = self.gradient.resize((490, 50))
        self.gradientImage = ImageTk.PhotoImage(self.gradient)

        # Image
        self.image = ImageTk.PhotoImage(Image.open('tigerFace.jpeg').resize((612, 408)))
        self.labelImage = Label(self.frameRight, image=self.image)
        self.labelImage.pack(pady=70)

        # Original Button
        self.buttonOriginal = Button(self.frameLeft, text='Original', width=500, height=50, command=self.original, borderwidth=0, image=self.gradientImage, compound='center')
        self.buttonOriginal.pack(pady=(0, 10))

        # Grayscale Button
        self.buttonGrayscale = Button(self.frameLeft, text='Grayscale', width=500, height=50, command=self.grayscale, borderwidth=0, image=self.gradientImage, compound='center')
        self.buttonGrayscale.pack(pady=(0, 10))

        # Rotate 180 Button
        self.buttonRotate180 = Button(self.frameLeft, text='Rotate180', width=500, height=50, command=self.rotate180, borderwidth=0, image=self.gradientImage, compound='center')
        self.buttonRotate180.pack(pady=(0, 10))

        # Rotate 90 Button
        self.buttonRotate90 = Button(self.frameLeft, text='Rotate90', width=500, height=50, command=self.rotate90, borderwidth=0, image=self.gradientImage, compound='center')
        self.buttonRotate90.pack(pady=(0, 10))

        # Glow Button
        self.buttonGlow = Button(self.frameLeft, command=self.glow, text='Glow', width=500, height=50, borderwidth=0, image=self.gradientImage, compound='center')
        self.buttonGlow.pack(pady=(0, 10))

        # Hue Drop Down Menu
        '''
        self.HueInt = IntVar()
        self.HueInt.set(355)
        self.menuHue = OptionMenu(self.frameLeft, self.HueInt, 0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35, 36, 37, 38, 39, 40, 41, 42, 43, 44, 45, 46, 47, 48, 49, 50, 51, 52, 53, 54, 55, 56, 57, 58, 59, 60, 61, 62, 63, 64, 65, 66, 67, 68, 69, 70, 71, 72, 73, 74, 75, 76, 77, 78, 79, 80, 81, 82, 83, 84, 85, 86, 87, 88, 89, 90, 91, 92, 93, 94, 95, 96, 97, 98, 99, 100, 101, 102, 103, 104, 105, 106, 107, 108, 109, 110, 111, 112, 113, 114, 115, 116, 117, 118, 119, 120, 121, 122, 123, 124, 125, 126, 127, 128, 129, 130, 131, 132, 133, 134, 135, 136, 137, 138, 139, 140, 141, 142, 143, 144, 145, 146, 147, 148, 149, 150, 151, 152, 153, 154, 155, 156, 157, 158, 159, 160, 161, 162, 163, 164, 165, 166, 167, 168, 169, 170, 171, 172, 173, 174, 175, 176, 177, 178, 179, 180, 181, 182, 183, 184, 185, 186, 187, 188, 189, 190, 191, 192, 193, 194, 195, 196, 197, 198, 199, 200, 201, 202, 203, 204, 205, 206, 207, 208, 209, 210, 211, 212, 213, 214, 215, 216, 217, 218, 219, 220, 221, 222, 223, 224, 225, 226, 227, 228, 229, 230, 231, 232, 233, 234, 235, 236, 237, 238, 239, 240, 241, 242, 243, 244, 245, 246, 247, 248, 249, 250, 251, 252, 253, 254, 255, 256, 257, 258, 259, 260, 261, 262, 263, 264, 265, 266, 267, 268, 269, 270, 271, 272, 273, 274, 275, 276, 277, 278, 279, 280, 281, 282, 283, 284, 285, 286, 287, 288, 289, 290, 291, 292, 293, 294, 295, 296, 297, 298, 299, 300, 301, 302, 303, 304, 305, 306, 307, 308, 309, 310, 311, 312, 313, 314, 315, 316, 317, 318, 319, 320, 321, 322, 323, 324, 325, 326, 327, 328, 329, 330, 331, 332, 333, 334, 335, 336, 337, 338, 339, 340, 341, 342, 343, 344, 345, 346, 347, 348, 349, 350, 351, 352, 353, 354, 355)
        self.menuHue.pack()
        '''

        # Hue Slider
        self.HueInt = IntVar()
        self.HueInt.set(255)
        self.sliderHue = Scale(self.frameLeft, variable=self.HueInt, from_=0, to=255, orient=HORIZONTAL, length=400, width=20, bg='light grey')
        self.sliderHue.pack(pady=(20, 7))

        # Hue Submit Button
        self.buttonHue = Button(self.frameLeft, command=self.changeHue, text='Change Hue')
        self.buttonHue.pack()

        # Saturation Drop Down Menu
        '''
        self.SaturationInt = IntVar()
        self.SaturationInt.set(100)
        self.menuSaturation = OptionMenu(self.frameLeft, self.SaturationInt, 0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35, 36, 37, 38, 39, 40, 41, 42, 43, 44, 45, 46, 47, 48, 49, 50, 51, 52, 53, 54, 55, 56, 57, 58, 59, 60, 61, 62, 63, 64, 65, 66, 67, 68, 69, 70, 71, 72, 73, 74, 75, 76, 77, 78, 79, 80, 81, 82, 83, 84, 85, 86, 87, 88, 89, 90, 91, 92, 93, 94, 95, 96, 97, 98, 99, 100)
        self.menuSaturation.pack()
        '''

        # Saturation Slider
        self.SaturationInt = IntVar()
        self.SaturationInt.set(100)
        self.sliderSaturation = Scale(self.frameLeft, variable=self.SaturationInt, from_=0, to=100, orient=HORIZONTAL, length=400, width=20)
        self.sliderSaturation.pack(pady=(20, 7))

        # Saturation Submit Button
        self.buttonSaturation = Button(self.frameLeft, command=self.changeSaturation, text='Change Saturation')
        self.buttonSaturation.pack()

        # Value Drop Down Menu
        '''
        self.ValueInt = IntVar()
        self.ValueInt.set(255)
        self.menuValue = OptionMenu(self.frameLeft, self.ValueInt, 0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35, 36, 37, 38, 39, 40, 41, 42, 43, 44, 45, 46, 47, 48, 49, 50, 51, 52, 53, 54, 55, 56, 57, 58, 59, 60, 61, 62, 63, 64, 65, 66, 67, 68, 69, 70, 71, 72, 73, 74, 75, 76, 77, 78, 79, 80, 81, 82, 83, 84, 85, 86, 87, 88, 89, 90, 91, 92, 93, 94, 95, 96, 97, 98, 99, 100, 101, 102, 103, 104, 105, 106, 107, 108, 109, 110, 111, 112, 113, 114, 115, 116, 117, 118, 119, 120, 121, 122, 123, 124, 125, 126, 127, 128, 129, 130, 131, 132, 133, 134, 135, 136, 137, 138, 139, 140, 141, 142, 143, 144, 145, 146, 147, 148, 149, 150, 151, 152, 153, 154, 155, 156, 157, 158, 159, 160, 161, 162, 163, 164, 165, 166, 167, 168, 169, 170, 171, 172, 173, 174, 175, 176, 177, 178, 179, 180, 181, 182, 183, 184, 185, 186, 187, 188, 189, 190, 191, 192, 193, 194, 195, 196, 197, 198, 199, 200, 201, 202, 203, 204, 205, 206, 207, 208, 209, 210, 211, 212, 213, 214, 215, 216, 217, 218, 219, 220, 221, 222, 223, 224, 225, 226, 227, 228, 229, 230, 231, 232, 233, 234, 235, 236, 237, 238, 239, 240, 241, 242, 243, 244, 245, 246, 247, 248, 249, 250, 251, 252, 253, 254, 255)
        self.menuValue.pack()
        '''

        # Value Slider
        self.ValueInt = IntVar()
        self.ValueInt.set(255)
        self.sliderValue = Scale(self.frameLeft, variable=self.ValueInt, from_=0, to =255, orient=HORIZONTAL, length=400, width=20)
        self.sliderValue.pack(pady=(20, 7))

        # Value Submit Button
        self.buttonValue = Button(self.frameLeft, command=self.changeValue, text='Change Value')
        self.buttonValue.pack()

    
    def original(self):
        module4.main('original', 0)
        self.newImage = ImageTk.PhotoImage(Image.open('done.png').resize((612, 408)))
        self.labelImage.config(image=self.image)
            
    def grayscale(self):
        module4.main('grayscale', 0)
        if module4.MyIPClass.dimensions == 'original':
            self.newImage = ImageTk.PhotoImage(Image.open('done.png').resize((612, 408)))
        else:
            self.newImage = ImageTk.PhotoImage(Image.open('done.png').resize((408, 612)))
        self.labelImage.config(image=self.newImage)
    
    def rotate180(self):
        module4.main('rotate180', 0)
        if module4.MyIPClass.dimensions == 'original':
            self.newImage = ImageTk.PhotoImage(Image.open('done.png').resize((612, 408)))
        else:
            self.newImage = ImageTk.PhotoImage(Image.open('done.png').resize((408, 612)))
        self.labelImage.config(image=self.newImage)
    
    def rotate90(self):
        module4.main('rotate90', 0)
        if module4.MyIPClass.dimensions == 'original':
            self.newImage = ImageTk.PhotoImage(Image.open('done.png').resize((612, 408)))
        else:
            self.newImage = ImageTk.PhotoImage(Image.open('done.png').resize((408, 612)))
        self.labelImage.config(image=self.newImage)
    
    def changeHue(self):
        module4.main('changeHue', self.HueInt.get())
        if module4.MyIPClass.dimensions == 'original':
            self.newImage = ImageTk.PhotoImage(Image.open('done.png').resize((612, 408)))
        else:
            self.newImage = ImageTk.PhotoImage(Image.open('done.png').resize((408, 612)))
        self.labelImage.config(image=self.newImage)
    
    def changeSaturation(self):
        module4.main('changeSaturation', self.SaturationInt.get())
        if module4.MyIPClass.dimensions == 'original':
            self.newImage = ImageTk.PhotoImage(Image.open('done.png').resize((612, 408)))
        else:
            self.newImage = ImageTk.PhotoImage(Image.open('done.png').resize((408, 612)))
        self.labelImage.config(image=self.newImage)
    
    def changeValue(self):
        module4.main('changeValue', self.ValueInt.get())
        if module4.MyIPClass.dimensions == 'original':
            self.newImage = ImageTk.PhotoImage(Image.open('done.png').resize((612, 408)))
        else:
            self.newImage = ImageTk.PhotoImage(Image.open('done.png').resize((408, 612)))
        self.labelImage.config(image=self.newImage)
    
    def glow(self):
        module4.main('glow', 0)
        if module4.MyIPClass.dimensions == 'original':
            self.newImage = ImageTk.PhotoImage(Image.open('done.png').resize((612, 408)))
        else:
            self.newImage = ImageTk.PhotoImage(Image.open('done.png').resize((408, 612)))
        self.labelImage.config(image=self.newImage)
