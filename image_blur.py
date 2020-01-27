import numpy as np
import cv2

cap = cv2.VideoCapture(0)

while True:
	_, frame = cap.read()
	hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)
	
	lower_c = np.array([20,80,120])
	upper_c = np.array([255,255,255])
	
	mask =  cv2.inRange(hsv, lower_c, upper_c)
	result  = cv2.bitwise_and(frame, frame, mask = mask)
	
	kernel = np.ones((15,15), np.float32)/225
	smoothed = cv2.filter2D(result, -1, kernel)
	Gaussian_blur = cv2.GaussianBlur(result, (15,15) , 0)
	median_blur = cv2.medianBlur(result, 15)
	bilateral_filter = cv2.bilateralFilter(result, 15, 75,75)
	
	
	cv2.imshow('frame', frame)
	cv2.imshow('mask', mask)
	cv2.imshow('result', result)
	cv2.imshow('smoothed', smoothed)
	cv2.imshow('GaussianBlur', Gaussian_blur)
	cv2.imshow('median_blur', median_blur)
	cv2.imshow('bilateral_filter', bilateral_filter)
	if cv2.waitKey(1) & 0xFF == ord('q'):
		break
	
cv2.destroyAllWindows()
cap.release()