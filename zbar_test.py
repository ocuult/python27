#!/usr/bin/python
from sys import argv
import zbar
from PIL import Image

img_file = "more.png"
# create a reader
scanner = zbar.ImageScanner()
# configure the reader
scanner.parse_config('enable')
# obtain image data
pil = Image.open(img_file).conver('L')
width, height = pil.size
raw = pil.tostring()
# wrap image data
image = zbar.Image(width, height, 'Y800', raw)
# scan the image for barcodes
scanner.scan(image)
# extract results
for symbol in image:
    # do something useful with results
    print 'decoded', symbol.type, 'symbol', '"%s"' % symbol.data

# clean up
del (image)


# import zbar
#
# from PIL import Image
#
#
#
# scanner = zbar.ImageScanner()
#
# scanner.parse_config('enable')
#
# img = Image.open('./test.jpg').convert('L')
#
# w, h = img.size
#
# zimg = zbar.Image(w, h, 'Y800', img.tobytes())
#
#
#
# scanner.scan(zimg)
#
#
#
# for s in zimg:
#
#     print s.type, s.data