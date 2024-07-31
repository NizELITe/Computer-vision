import cv2 

import numpy as np 
from matplotlib import pyplot as plt 

image = cv2.imread(r'C:\Users\Nizam\Desktop\recomendationsystem\image_preprocessing\sample_image.jpeg',cv2.IMREAD_COLOR)
image_rgb = cv2.cvtColor(image,cv2.COLOR_BGR2RGB)

image_blurry = cv2.blur(image_rgb,(5,5)) #kernel size


plt.imshow(image_rgb),plt.axis('off')
plt.show()

plt.imshow(image_blurry),plt.axis('off')
plt.show()
