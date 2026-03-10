from ConversionAPI.api import api


#Associate image
api = api('Example_image.png')

#Get dimensions
dimensions = api.get_dimensions()
print(f"Dimensions: {dimensions}")

#Get format
image_format = api.get_format()
print(f"Format: {image_format}")

#Get pixel value at (100, 100)
pixel_value = api.getpixel(100, 100)
print(f"Pixel value at (100, 100): {pixel_value}")

#Gzip Encode and Decode text
text = "Hello World!"

encoded_text = api.gzipEncode(text)
print(f"Encoded text: {encoded_text}")

decoded_text = api.gzipDecode(encoded_text)
print(f"Decoded text: {decoded_text}")

#next