#!/usr/bin/env python2
# -*- coding: utf-8-*-


from zxing import *

zxing_location = "./zxing"
testimage = "./image/more.png"


def test_barcode_parser():
    text = """
file:/home/oostendo/Pictures/datamatrix/4-contrastcrop.bmp (format: DATA_MATRIX, type: TEXT):
Raw result:
36MVENBAEEAS04403EB0284ZB
Parsed result:
36MVENBAEEAS04403EB0284ZB
Also, there were 4 result points.
  Point 0: (24.0,18.0)
  Point 1: (21.0,196.0)
  Point 2: (201.0,198.0)
  Point 3: (205.23952,21.0)
"""

    barcode = BarCode(text)
    if barcode:
        print barcode.data
    else:
        print "当前图片没有取到特征点"
    if (barcode.format != "DATA_MATRIX"):
        return 0

    if (barcode.raw != "36MVENBAEEAS04403EB0284ZB"):
        return 0

    if (barcode.data != "36MVENBAEEAS04403EB0284ZB"):
        return 0

    if (len(barcode.points) != 4 and barcode.points[0][0] != 24.0):
        return 0

    return 1


def test_codereader():
    zx = BarCodeReader(zxing_location)
    # zx = BarCodeReader()

    barcode = zx.decode(testimage)
    if barcode:
        print barcode.data
    else:
        print "没有识别到"
    # if re.match("http://", barcode.data):
    #     return 1
    #
    # return 0

test_barcode_parser()
test_codereader()