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
	
	cv2.imshow('frame', frame)
	cv2.imshow('mask', mask)
	cv2.imshow('result', result)
	
	if cv2.waitKey(1) & 0xFF == ord('q'):
		break
	
cv2.destroyAllWindows()
cap.release()