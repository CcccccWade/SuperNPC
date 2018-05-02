#coding=utf-8

import os

from supernpc import pipline as pp



import cv2



import numpy as np



parent = "E:\image"



for filename in os.listdir(parent):

    print(filename)

    path = os.path.join(parent, filename)

    print(path)

    if path.endswith(".jpg") or path.endswith(".png"):

        image = cv2.imdecode(np.fromfile(path, dtype=np.uint8), -1)



        image, res = pp.SimpleRecognizePlate(image)

        cv2.imshow("image", image)

        cv2.waitKey(0)