import cv2
import numpy as np
from matplotlib import pyplot as plt


image = cv2.imread("C:\Users\Nizam\Desktop\recomendationsystem\image_preprocessing\sample_image.jpeg", cv2.IMREAD_GRAYSCALE)


image_enhanced = cv2.equalizeHist(image)


plt.imshow(image_enhanced, cmap="gray"), plt.axis("off")
plt.show()