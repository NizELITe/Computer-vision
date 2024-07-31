import cv2
import numpy as np
from matplotlib import pyplot as plt




image_bgr = cv2.imread(r'C:\Users\Nizam\Desktop\recomendationsystem\image_preprocessing\images.jpeg')
image_gray = cv2.cvtColor(image_bgr, cv2.COLOR_BGR2GRAY)
# Number of corners to detect
corners_to_detect = 10
minimum_quality_score = 0.05
minimum_distance = 25






corners = cv2.goodFeaturesToTrack(image_gray,
 corners_to_detect,
minimum_quality_score,
minimum_distance)
corners = np.float32(corners)
# Draw white circle at each corner
for corner in corners:
 x, y = corner[0]
 cv2.circle(image_bgr, (x,y), 10, (255,255,255), -1)
# Convert to grayscale
image_rgb = cv2.cvtColor(image_bgr, cv2.COLOR_BGR2GRAY)
# Show image
plt.imshow(image_rgb, cmap='gray'), plt.axis("off")
plt.show()