import numpy as np
import cv2

img = cv2.imread('C:\\Users\\sukum\\Pictures\\Camera Roll\\EE.jpg')
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
gray = np.float32(gray)
#print (gray)

corners = cv2.goodFeaturesToTrack(gray, 250,0.01,15) ## img, quantity of corners, img quality, distance between corners
corners = np.int0(corners)

for corner in corners:
	x,y = corner.ravel()
	cv2.circle(img, (x,y), 3, 255, -1)

cv2.imshow('Corners', img)
