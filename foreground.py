import numpy as np
import cv2
import matplotlib.pyplot as plt

img = cv2.imread('C:\\Users\\sukum\\Pictures\\Camera Roll\\GrabCut.jpg')
mask = np.zeros(img.shape[:2], np.uint8)

backgroundModel = np.zeros((1,65), np.float64)
foregroundModel = np.zeros((1,65), np.float64)

rectangle = (250,87,800,700)

cv2.grabCut(img, mask, rectangle, backgroundModel, foregroundModel, 5, cv2.GC_INIT_WITH_RECT)
mask2 = np.where((mask == 2) | (mask ==0), 0, 1).astype('uint8')

img = img*mask2[:,:, np.newaxis]

plt.imshow(img)
plt.colorbar()
plt.show()

