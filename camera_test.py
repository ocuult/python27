#!/usr/bin/env python2
# -*- coding: utf-8-*-


import cv2
import numpy as np
from zxing import *


cap = cv2.VideoCapture(0)
font=cv2.FONT_HERSHEY_SIMPLEX
word= None
zxing_location = "./zxing"

def test_codereader(testimage):
    zx = BarCodeReader(zxing_location)
    # zx = BarCodeReader()

    barcode = zx.decode(testimage)
    if barcode:
        return barcode.data
    else:
        return "没有识别到"

while(1):
    # get a frame
    ret, frame = cap.read()
    # show a frame
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    cv2.putText(gray, word, (20, 100), font, 1, (0, 255, 0), 4)
    cv2.imshow("capture", gray)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break
    if cv2.waitKey(1) & 0xFF == ord('s'):
        cv2.imwrite("skin.jpg", gray)
        word = test_codereader('skin.jpg')
# cv2.imwrite("skin.jpg", frame)
# cap.release()
cv2.destroyAllWindows()
#
# import numpy as np

# import cv2
#
# camera = cv2.VideoCapture(0)
# font=cv2.FONT_HERSHEY_SIMPLEX
# # determine upper and lower HSV limits for (my) skin tones
# # lower = np.array([0, 100, 0], dtype="uint8")
# # upper = np.array([50,255,255], dtype="uint8")
#
# while (True):
#   ret, frame = camera.read()
#   if not ret:
#     continue
#   # switch to HSV
#   # hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)
#   # # find mask of pixels within HSV range
#   # skinMask = cv2.inRange(hsv, lower, upper)
#   # # denoise
#   # skinMask = cv2.GaussianBlur(skinMask, (9, 9), 0)
#   # # kernel for morphology operation
#   # kernel = cv2.getStructuringElement(cv2.MORPH_ELLIPSE, (4, 4))
#   # # CLOSE (dilate / erode)
#   # skinMask = cv2.morphologyEx(skinMask, cv2.MORPH_CLOSE, kernel, iterations = 3)
#   # # denoise the mask
#   # skinMask = cv2.GaussianBlur(skinMask, (9, 9), 0)
#   # # only display the masked pixels
#   # skin = cv2.bitwise_and(frame, frame, mask = skinMask)
#   cv2.putText(frame, 'hello world', (20, 100), font, 1, (0, 255, 0), 4)
#   cv2.imshow("HSV", frame)
#   # quit or save frame
#   key = cv2.waitKey(1000 / 12) & 0xff
#   if key == ord("q"):
#     break
#   if key == ord("p"):
#     cv2.imwrite("skin.jpg", frame)
#
# cv2.destroyAllWindows()