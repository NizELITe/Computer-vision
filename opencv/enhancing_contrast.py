import cv2
import numpy as np
from matplotlib import pyplot as plt

image = cv2.imread(r"C:\Users\Nizam\Desktop\recomendationsystem\image_preprocessing\sample_image.jpeg", cv2.IMREAD_GRAYSCALE)


#Histogram equalization is a tool for image processing that can make objects and
#shapes stand out only when grayscale image

image_enhanced = cv2.equalizeHist(image)

plt.imshow(image_enhanced, cmap="gray"), plt.axis("off")
plt.show()


#enhance contrast of color image

image_bgr = cv2.imread(r'C:\Users\Nizam\Desktop\recomendationsystem\image_preprocessing\sample_image.jpeg')

image_yuv = cv2.cvtColor(image_bgr,cv2.COLOR_BGR2YUV)

image_yuv[:,:,0] = cv2.equalizeHist(image_yuv[:,:,0])


image_rgb = cv2.cvtColor(image_yuv, cv2.COLOR_YUV2RGB)
# Show image
plt.imshow(image_rgb), plt.axis("off")
plt.show()
