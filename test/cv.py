from PIL import Image
import cv2

img_m = Image.open('capture1.jpg')
Size = img_m.size  # 返回图片 宽高 的一个元组，单位是像素
w = img_m.width  # 图片的宽
h = img_m.height  # 图片的高
f = img_m.format  # 图像格式

print(Size)
print('宽：',w,'  高：', h, '   格式：', f)


img = cv2.imread('capture1.jpg')

cv2.imshow('1', img)
cv2.waitKey(0)
