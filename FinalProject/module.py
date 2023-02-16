from PIL import Image
import math
import colorsys

class MyIPClass:
    def __init__(self, image,):
        self.image = Image.open(image)
        self.pixels = self.image.load()
        self.width = self.image.size[0]
        self.height = self.image.size[1]
    
    def save(self):
        self.image.save("done.png", "PNG")
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
        return self


def main(method):

    if method == 'original':
        pass

    elif method == 'grayscale':
        MyIPClass('tigerFace.jpeg').grayscale().save()
        
    elif method == 'rotate180':
        MyIPClass('tigerFace.jpeg').rotate180().save()

if __name__ == '__main__':
    method = 0
    main(method)
