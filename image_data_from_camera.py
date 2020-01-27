import numpy as np
import cv2

cap = cv2.VideoCapture(0)
fourcc = cv2.VideoWriter_fourcc(*'XVID') ## Video Codec
out = cv2.VideoWriter('D:\\Python experiments\\OpenCV\\video_output.avi', fourcc, 24.0, (640,480))

while True:
	ret, frame = cap.read()
	out.write(frame)
	gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
	cv2.imshow('frame', frame)
	cv2.imshow('gray', gray)
	 
	if cv2.waitKey(1) & 0xFF == ord('q'):
		break
		
cap.release()
out.release()
cv2.destroyAllWindows()


