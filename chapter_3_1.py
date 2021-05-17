import cv2
import numpy as np

img = cv2.imread("Resources\loro.jpg")
print(img.shape)

imgResize = cv2.resize(img,(900,500)) #height, length
print(imgResize.shape)

imgCropped = img[0:400,200:400] #height,length

cv2.imshow("Image",img)
cv2.imshow("Image Resize",imgResize)
cv2.imshow("Image Cropped",imgCropped)

cv2.waitKey(0)