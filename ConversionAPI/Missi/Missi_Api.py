import gzip

from PIL import Image
class api():
    def __init__(self, image_path):
        self.image = Image.open(image_path)
    def get_dimensions(self):
        width, height = self.image.size
        return width, height
    def get_format(self):
        image_format = self.image.format
        return image_format
    def getpixel(self, x, y):
        pixel_value = self.image.getpixel((x, y))
        return pixel_value
    def gzipEncode(self, text):
        bytes = text.encode('utf-8')
        return gzip.compress(bytes)
    def gzipDecode(self, Encoded):
        return gzip.decompress(Encoded).decode('utf-8')
    def convert(self, new_format):
        #possible values: RGB, RGBA, L, etc.
        new_image = self.image.convert(new_format)
        return new_image
    def show(self):
        self.image.show()
    def IndexImage(self):
        #Get dimensions of the image
        width, height = self.get_dimensions()
        #Put in RGB mode
        self.image = self.image.convert("RGB")
        indexed = []
        for y in range(height):
            for x in range(width):
                pix = self.getpixel(x, y) 
                indexed.append(((x, y), pix))
        return indexed
    def main(self):
        #main function that does everything
        Indexed = self.IndexImage()
        Gzipped = self.gzipEncode(str(Indexed))
        return Indexed