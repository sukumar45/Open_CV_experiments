import numpy as np
import cv2

cap = cv2.VideoCapture(0) ## '0' represents primary camera source - you can use '1' if you have a secondary camera connected to usb
while True:
	_, frame = cap.read()
	
	laplacian = cv2.Laplacian(frame, cv2.CV_64F)
	
	## gradients
	sobelx = cv2.Sobel(frame, cv2.CV_64F, 1, 0, ksize = 5)
	sobely = cv2.Sobel(frame, cv2.CV_64F, 0, 1, ksize = 5)
	
	## edge detection
	edges = cv2.Canny(frame, 100, 200) 
	
	cv2.imshow('frame', frame)
	cv2.imshow('laplacian', laplacian)
	#cv2.imshow('sobelx', sobelx)
	#cv2.imshow('sobely', sobely)
	cv2.imshow('edges', edges)
	
	
	if cv2.waitKey(1) & 0xFF == ord('q'):
		break
	
cv2.destroyAllWindows()
cap.release()