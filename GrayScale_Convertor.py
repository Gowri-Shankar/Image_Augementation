import cv2
import numpy as np
import sys
import os
file="D:\\colour_to_grey\\convert" #Folder Path with need to be converted
items=os.listdir(file)
i=0
result_path="D:\\colour_to_grey\\result"  #Folder Path to save result image
for item in items:
    path=file+"\\" +item
    print (path)
    image = cv2.imread(path) # change image name as you need or give sys.argv[1] to read from command line
    gray_image= cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)  # convert image to gray
    new_path=result_path+"\\"+"image"+str(i)+".jpg"
    print (new_path)
    cv2.imwrite(new_path,gray_image)   # saves gray image to disk
    i=i+1
cv2.imshow('color_image',image)
cv2.imshow('gray_image',gray_image)

cv2.waitKey(0)
cv2.destroyAllWindows()


