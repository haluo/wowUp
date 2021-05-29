from PIL import Image
import cv2
import  numpy as np
img = cv2.imread('../capture1.jpg')
kernel = np.ones((5,5),np.uint8)

imgGray = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)  #灰度图
imgBlur =cv2.GaussianBlur(imgGray,(7,7),0)  #高斯模糊
imgCanny = cv2.Canny(img,150,200)  #边缘检测
imgDilation = cv2.dilate(imgCanny,kernel,iterations=1) #腐蚀
imgEroded = cv2.erode(imgDilation,kernel,iterations=1) #膨胀

# cv2.imshow('imgGray', imgGray)
# cv2.imshow('imgBlur', imgBlur)
cv2.imshow('imgCanny', imgCanny)
cv2.imshow('imgDilation', imgDilation)
cv2.imshow('imgEroded', imgEroded)

cv2.waitKey(0)
