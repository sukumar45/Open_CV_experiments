import numpy as np
import cv2
import matplotlib.pyplot as plt

img = cv2.imread('D:\\Python experiments\\OpenCV\\calf.jpg', cv2.IMREAD_COLOR)
cv2.line(img, (0,0),(150,150), (255,255,255), 15) ##(img_source, start_point, end_point, color in BGR, line_width)
cv2.rectangle(img, (828,128), (1385,628), (0,0,255),5)
cv2.circle(img, (1022,325), 20, (0,255,0), 3) ##(img_source, centre_point, radius, color in BGR, line_width)
cv2.circle(img, (1230,330), 20, (0,255,0), 3)

pts = np.array([[150,250],[1200,300],[300,300],[320,320],[520,520]],np.int32)

cv2.polylines(img, [pts], True, (0,255,255), 2)

font = cv2.FONT_HERSHEY_SIMPLEX
cv2.putText(img, 'openCV_text!', (0,130), font, 2, (255,255,0), 2, cv2.LINE_AA)

plt.imshow(img, cmap = 'gray', interpolation = 'bicubic')
cv2.imshow('suku', img)
plt.show()

cv2.waitKey(0)
cv2.destroyAllWindows()