from compression import gzip

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
    def get_pixel(self, x, y):
        pixel_value = self.image.getpixel((x, y))
        return pixel_value
    def gzipEncode(self, text):
        bytes = text.encode('utf-8')
        return gzip.compress(bytes)
    def gzipDecode(self, Encoded):
        return gzip.decompress(eval(Encoded)).decode('utf-8')
