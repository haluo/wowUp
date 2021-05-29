import cv2
import numpy as np

"""合并图片"""

img = cv2.imread("lena.png")
imgHor = np.hstack((img,img))
imgVer = np.vstack((img,img))


cv2.imshow("imgHor",imgHor)
cv2.imshow("imgVer",imgVer)

cv2.waitKey(0)
