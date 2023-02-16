from PIL import Image
import math
import colorsys
import gui8

class MyIPClass:
    currentState = 'original'
    dimensions = 'original'

    def __init__(self, image,):
        self.image = Image.open(image)
        self.pixels = self.image.load()
        self.width = self.image.size[0]
        self.height = self.image.size[1]
    
    def save(self):
        self.image.save("./Images/done.png", "PNG")
        return self
    
    def original(self):
        original = self.image
        self.image = original
        MyIPClass.currentState = 'original'
        MyIPClass.dimensions = 'original'
        return self
    
    def grayscale(self):
        for y in range(self.height):
            for x in range(self.width):
                rgb = self.pixels[x,y]
                r = rgb[0]
                g = rgb[1]
                b = rgb[2]
                newRGB = (int((r+g+b)/3), int((r+g+b)/3), int((r+g+b)/3))
                self.pixels[x,y] = newRGB
        MyIPClass.currentState = 'grayscale'
        if MyIPClass.dimensions == 'original':
            MyIPClass.dimensions = 'original'
        else:
            MyIPClass.dimensions = 'flipped'
        return self
    
    def rotate180(self):
        intermediate = Image.new(mode='RGB', size=(self.width, self.height))
        interPixels = intermediate.load()
        for y in range(self.height):
            for x in range(self.width):
                rgb = self.pixels[x,y]
                x1 = self.width - x - 1
                y1 = self.height - y - 1

                interPixels[x1,y1] = (rgb[0], rgb[1], rgb[2])
        self.image = intermediate
        MyIPClass.currentState = 'rotate180'
        if MyIPClass.dimensions == 'original':
            MyIPClass.dimensions = 'original'
        else:
            MyIPClass.dimensions = 'flipped'
        return self
    
    def rotate90(self):
        intermediate = Image.new(mode='RGB', size=(self.height, self.width))
        interPixels = intermediate.load()
        for y in range(self.height):
            for x in range(self.width):
                rgb = self.pixels[x,y]
                y1 = self.width - x - 1
                x1 = self.height - y - 1

                interPixels[x1,y1] = (rgb[0], rgb[1], rgb[2])
        self.image = intermediate

        MyIPClass.currentState = 'rotate90'
        if MyIPClass.dimensions == 'original':
            MyIPClass.dimensions = 'flipped'
        else:
            MyIPClass.dimensions = 'original'
        return self
    
    def changeHue(self, degrees):
        bw = self.width
        bh = self.height
        intermediate = Image.new(mode='RGB', size=(bw, bh))
        interPixels = intermediate.load()

        for y in range(bh):
            for x in range(bw):
                original = self.pixels[x,y]
                (h, s, v) = colorsys.rgb_to_hsv(original[0], original[1], original[2])
                h += degrees
                #while h < 0:
                #    h += 360
                h /= 255
                (red, green, blue) = colorsys.hsv_to_rgb(float(h), float(s), float(v))
                interPixels[x,y] = (int(red), int(green), int(blue))
                self.color = interPixels[x,y]
        self.image = intermediate

        MyIPClass.currentState = 'changeHue'
        if MyIPClass.dimensions == 'original':
            MyIPClass.dimensions = 'original'
        else:
            MyIPClass.dimensions = 'flipped'
        return self
    
    def changeSaturation(self, amount):
        '''
        # If they put 100, actually put -100
        amount -= (amount*2)

        # Original Range (-1 to 0)

        # New Range (0 to 1)
        amount -= 1

        # New Range (-100 to 0)
        amount /= 100
        '''
        amount = 100 - amount

        bw = self.width
        bh = self.height
        intermediate = Image.new(mode='RGB', size=(bw, bh))
        interPixels = intermediate.load()

        for y in range(bh):
            for x in range(bw):
                original = self.pixels[x,y]
                (h, s, v) = colorsys.rgb_to_hsv(original[0], original[1], original[2])
                s -= amount/110
                if s < 0:
                    s = 0
                elif s > 255:
                    s = 255
                (r, g, b) = colorsys.hsv_to_rgb(float(h), float(s), float(v))
                interPixels[x,y] = (int(r), int(g), int(b))
                self.color = interPixels[x,y]
        self.image = intermediate

        MyIPClass.currentState = 'changeSaturation'
        if MyIPClass.dimensions == 'original':
            MyIPClass.dimensions = 'original'
        else:
            MyIPClass.dimensions = 'flipped'
        return self
    
    def changeValue(self, amount):

        amount -= 245

        bw = self.width
        bh = self.height
        intermediate = Image.new(mode='RGB', size=(bw, bh))
        interPixels = intermediate.load()

        for y in range(bh):
            for x in range(bw):
                original = self.pixels[x,y]
                (h, s, v) = colorsys.rgb_to_hsv(original[0], original[1], original[2])
                v += amount
                v -= 10

                #if amount > 100:
                #    v = 255
                #elif amount < 0:
                #    v = 0
                '''
                if v < 0:
                    v = 0
                elif v > 255:
                    v = 255
                '''
                (r, g, b) = colorsys.hsv_to_rgb(float(h), float(s), float(v))
                interPixels[x,y] = (int(r), int(g), int(b))
                self.color = interPixels[x,y]
        self.image = intermediate

        MyIPClass.currentState = 'changeValue'
        if MyIPClass.dimensions == 'original':
            MyIPClass.dimensions = 'original'
        else:
            MyIPClass.dimensions = 'flipped'
        return self
    
    def glow(self):
        amount = 180

        amount -= 245

        bw = self.width
        bh = self.height
        intermediate = Image.new(mode='RGB', size=(bw, bh))
        interPixels = intermediate.load()

        for y in range(bh):
            for x in range(bw):
                original = self.pixels[x,y]
                (h, s, v) = colorsys.rgb_to_hsv(original[0], original[1], original[2])
                v += amount

                v *= 5

                #if amount > 100:
                #    v = 255
                #elif amount < 0:
                #    v = 0
                '''
                if v < 0:
                    v = 0
                elif v > 255:
                    v = 255
                '''
                (r, g, b) = colorsys.hsv_to_rgb(float(h), float(s), float(v))
                interPixels[x,y] = (int(r), int(g), int(b))
                self.color = interPixels[x,y]
        self.image = intermediate

        MyIPClass.currentState = 'glow'
        if MyIPClass.dimensions == 'original':
            MyIPClass.dimensions = 'original'
        else:
            MyIPClass.dimensions = 'flipped'
        return self

def main(method, number):
    # If the 'original' button is clicked, run through logic for 'original' 
    if method == 'original':
        #print(MyIPClass.currentState)
        if MyIPClass.currentState == 'original':
            MyIPClass(gui8.GUI.imagePath).original().save()
        else:
            MyIPClass('./Images/done.png').original().save()

    elif method == 'grayscale':
        #print(MyIPClass.currentState)
        if MyIPClass.currentState == 'original':
            MyIPClass(gui8.GUI.imagePath).grayscale().save()
        else:
            MyIPClass('./Images/done.png').grayscale().save()
        
    elif method == 'rotate180':
        #print(MyIPClass.currentState)
        #print(MyIPClass.dimensions)
        if MyIPClass.currentState == 'original':
            MyIPClass(gui8.GUI.imagePath).rotate180().save()
        else:
            MyIPClass('./Images/done.png').rotate180().save()
    
    elif method == 'rotate90':
        #print(MyIPClass.currentState)
        if MyIPClass.currentState == 'original':
            MyIPClass(gui8.GUI.imagePath).rotate90().save()
        else:
            if MyIPClass.dimensions == 'flipped':
                MyIPClass('./Images/done.png').rotate90().save()
                MyIPClass('./Images/done.png').rotate180().save()
                MyIPClass.currentState = 'rotate90'
            else:
                MyIPClass('./Images/done.png').rotate90().save()
    
    elif method == 'changeHue':
        #print(MyIPClass.currentState)
        #print(number)
        if MyIPClass.dimensions == 'original':
            MyIPClass('./Images/done.png').changeHue(number).save()
        else:
            MyIPClass('./Images/done.png').changeHue(number).save()
    
    elif method == 'changeSaturation':
        #print(MyIPClass.currentState)
        #print(number)
        if MyIPClass.currentState == 'original':
            MyIPClass('./Images/done.png').changeSaturation(number).save()
        else:
            MyIPClass('./Images/done.png').changeSaturation(number).save()
    
    elif method == 'changeValue':
        #print(MyIPClass.currentState)
        #print(number)
        if MyIPClass.currentState == 'original':
            MyIPClass('./Images/done.png').changeValue(number).save()
        else:
            MyIPClass('./Images/done.png').changeValue(number).save()
    
    elif method == 'glow':
        #print(MyIPClass.currentState)
        #print(number)
        if MyIPClass.currentState == 'original':
            MyIPClass(gui8.GUI.imagePath).glow().save()
        else:
            MyIPClass('./Images/done.png').glow().save()

if __name__ == '__main__':
    method = 0
    main(method)
