import cv2 
import numpy as np 
from matplotlib import pyplot as plt 


image = cv2.imread(r'C:\Users\Nizam\Desktop\recomendationsystem\image_preprocessing\sample_image.jpeg',cv2.IMREAD_GRAYSCALE)


#select first half of column
image_cropped = image[:,:128]

plt.imshow(image,cmap='gray'),plt.axis('off')


plt.show()

plt.imshow(image_cropped,cmap='gray'),plt.axis('off')
plt.show()