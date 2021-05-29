import cv2
import numpy as np
#img = np.zeros((512,512) 灰度图

img = np.zeros((512,512,3),np.uint8)
print(img.shape)

# img[:] = 250,0,0 #全部变为蓝色
# img[100:200,300:400] = 250,0,0 #部分变蓝色

cv2.line(img,(0,0),(img.shape[1],img.shape[0]),(0,255,0),3) #（00）到（300，300） 粗度为3的绿色的线
cv2.rectangle(img,(0,0),(250,350),(0,0,255),2) #矩形
# cv2.rectangle(img,(0,0),(250,350),(0,0,255),cv2.FILLED) #矩形填充
cv2.circle(img,(450,50),30,(255,255,0),5) #圆形


cv2.putText(img,"opencv",(300,100),cv2.FONT_HERSHEY_COMPLEX,1,(0,150,0),2) #文字 大小为1厚度为2


cv2.imshow("img",img)

cv2.waitKey(0)
