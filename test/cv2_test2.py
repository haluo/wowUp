from PIL import Image
import cv2

"""
改变尺寸和裁剪
"""

img = cv2.imread('lanbo.png')

print(img.shape)

imgResize = cv2.resize(img,(600,300)) ##改变尺寸

print(imgResize.shape)

imgCropped = img[0:500,0:1000]  #裁剪图片


cv2.imshow('img', img)
# cv2.imshow('imgResize', imgResize)
cv2.imshow('imgCropped', imgCropped)

cv2.waitKey(0)
