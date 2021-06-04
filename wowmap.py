import cv2
import numpy as np

"""
地图解析
"""

def cv_show(img,name):
    cv2.imshow(name,img)
    cv2.waitKey()
    cv2.destroyAllWindows()

img = cv2.imread('data/capture1.jpg')
print(img.shape)
img = cv2.resize(img,(600,400))
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
ret, binary = cv2.threshold(gray, 60, 255, cv2.THRESH_BINARY_INV)
kernel = np.ones((3,3),np.uint8)
closing = cv2.morphologyEx(binary,cv2.MORPH_OPEN,kernel)
# closing = cv2.morphologyEx(opening,cv2.MORPH_CLOSE,kernel)
cv_show(np.hstack((binary,closing)),'closing')
contours, hierarchy = cv2.findContours(binary, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
big_contours = []
mj = 600*400/10
for count in contours:
    area = cv2.contourArea(count)
    print(area)
    if area > mj/3:
        big_contours.append(count)
draw_img = img.copy()
print(len(big_contours))
# res = cv2.drawContours(draw_img, big_contours, -1, (0, 0, 255), 2)
# cv_show(res,'res')

for count in big_contours:
    x, y, w, h = cv2.boundingRect(count)
    draw_img = cv2.rectangle(draw_img, (x, y), (x + w, y + h), (0, 255, 0), 2)

cv_show(draw_img, 'draw_img')
