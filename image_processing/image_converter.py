from cv2 import cv2 
import numpy as np

default_image_size = tuple((256, 256))

def convert_image_to_array(in_image):
    image = cv2.imread(in_image)
    image = cv2.resize(image,default_image_size)
    x=np.array(image,dtype=np.float16)/255
    image_array = np.expand_dims(x,axis=0)
    return image_array
 