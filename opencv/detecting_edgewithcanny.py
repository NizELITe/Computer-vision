# we will use edge detection technique called canny edge detection

import cv2
import numpy as np
from matplotlib import pyplot as plt


image_gray = cv2.imread(r"C:\Users\Nizam\Desktop\recomendationsystem\image_preprocessing\images.jpeg", cv2.IMREAD_GRAYSCALE)

# Calculate median intensity
median_intensity = np.median(image_gray)
# Set thresholds to be one standard deviation above and below median intensity

lower_threshold = int(max(0, (1.0 - 0.33) * median_intensity))
upper_threshold = int(min(255, (1.0 + 0.33) * median_intensity))

image_canny = cv2.Canny(image_gray, lower_threshold, upper_threshold)

plt.imshow(image_canny, cmap="gray"), plt.axis("off")
plt.show()