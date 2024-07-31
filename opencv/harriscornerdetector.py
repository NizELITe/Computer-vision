import cv2
import numpy as np
from matplotlib import pyplot as plt


# Load image as grayscale
image_bgr = cv2.imread(r"C:\Users\Nizam\Desktop\recomendationsystem\image_preprocessing\images.jpeg")
image_gray = cv2.cvtColor(image_bgr, cv2.COLOR_BGR2GRAY)
image_gray = np.float32(image_gray)

# Set corner detector parameters
block_size = 2
aperture = 29
free_parameter = 0.04
# Detect corners
detector_responses = cv2.cornerHarris(image_gray,
 block_size,
aperture,
free_parameter)



detector_responses = cv2.dilate(detector_responses, None)


threshold = 0.02
image_bgr[detector_responses >
 threshold *
 detector_responses.max()] = [255,255,255]

# Convert to grayscale
image_gray = cv2.cvtColor(image_bgr, cv2.COLOR_BGR2GRAY)
# Show image
plt.imshow(image_gray, cmap="gray"), plt.axis("off")
plt.show()




plt.imshow(detector_responses, cmap='gray'), plt.axis("off")
plt.show()


