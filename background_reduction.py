import numpy as np
import cv2

capture = cv2.VideoCapture(0)##('C:\\Users\\sukum\\Pictures\\Camera Roll\\Cows_walk.mp4')
#capture2 = cv2.VideoCapture(0)
fgbg = cv2.createBackgroundSubtractorMOG2()

while True:
	ret, frame = capture.read()
	#ret2, frame2  = capture2.read()
	fgmask =  fgbg.apply(frame)
	#fgmask2 =  fgbg.apply(frame2)
	
	cv2.imshow('original', frame)
	#cv2.imshow('original2', frame2)
	cv2.imshow('fg', fgmask)
	#cv2.imshow('fg2', fgmask2)
	
	if cv2.waitKey(1) & 0xFF == ord('q'):
		break
	
capture.release()
cv2.destroyAllWindows()

	
	
