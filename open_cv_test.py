import numpy as np
import cv2

image_name = "tree_2"

print("read an image from file")
img = cv2.imread("/repos/daily_python/"+image_name+".jpeg")

print("create a window holder for the image")
cv2.namedWindow("Fancy Window", cv2.WINDOW_NORMAL)

print("display a key inside the image and make a copy")
#cv2.waitKey(0)

print("Image copied to folder images/copy/")
cv2.imwrite("images/copy/"+image_name+"-copy.jpeg",img)

