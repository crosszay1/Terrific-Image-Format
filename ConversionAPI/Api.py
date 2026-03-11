import gzip
import binascii

from PIL import Image
class api():
    def __init__(self, image_path):
        self.image = Image.open(image_path)

    def get_dimensions(self):
        width, height = self.image.size
        return width, height
    
    def getpixel(self, x, y):
        pixel_value = self.image.getpixel((x, y))
        return pixel_value

    def IndexImage(self):
        #Get dimensions of the image
        width, height = self.get_dimensions()
        #Put in RGB mode
        self.image = self.image.convert("RGB")

        indexed = []
        for y in range(height):
            for x in range(width):
                rgbPix = self.getpixel(x, y) #Get in RGB
                hexPix = '%x%x%x' % (rgbPix[0], rgbPix[1], rgbPix[2]) #Turn to hex
                indexed.append(((y*width)+x, hexPix))
        return indexed
    
    def main(self):
        #main function that does everything
        Indexed = self.IndexImage()
        #Gzipped = self.gzipEncode(str(Indexed))
        return Indexed