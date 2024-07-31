import cv2 
import numpy as np 
from matplotlib import pyplot as plt 

image = cv2.imread(r'C:\Users\Nizam\Desktop\recomendationsystem\image_preprocessing\sample_image.jpeg',cv2.IMREAD_GRAYSCALE)

#create kernel which highlights the target pixels 
kernel = np.array([[0, -1, 0],
 [-1, 5,-1],
 [0, -1, 0]])


#sharpen image
image_sharp = cv2.filter2D(image,-1,kernel)


plt.imshow(image_sharp, cmap="gray"), plt.axis("off")
plt.show()

