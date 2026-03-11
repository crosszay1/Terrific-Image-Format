from ConversionAPI.api import api
from pathlib import Path

image = "ExampleImages/Colorwheel.jpg"
#Associate image
api = api(image)

#Index an image
indexed = api.IndexImage()

#gzip the indexed image 
gzipped = api.gzipEncode(str(indexed))

title = Path(image).stem

with open(f"{title}.tif", "w") as file:
    file.write(str(gzipped))

exit(1)



#ungzip an image
ungzipped = api.gzipDecode(gzipped)