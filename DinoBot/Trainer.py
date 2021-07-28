# -*- coding: utf-8 -*-

######  ######  ######  #######   ######   #########
#       #       #       #     #   #            #
######  ####    #       #######   ####         #
     #  #       #       #    #    #            #
######  ######  ######  #     #   ######       # 

####  ####  ####  ####  ####   ##   ##   ##  ##   ##  ####  ####      #    ##
#  #  #  #  #  #  #     #  #  #  #  # # # #  # # # #  #     #  #    # #   #  #
####  ####  #  #  # ##  ####  ####  #  #  #  #  #  #  ##    ####      #  #    #
#     # #   #  #  #  #  # #   #  #  #     #  #     #  #     # #       #   #  #
#     #  #  ####  ####  #  #  #  #  #     #  #     #  ####  #  #      #    ##


"""
Fake It, Till You Make It!!

@author: SecretProgrammer10
"""

import cv2
import os
import keyboard
from screen_grab import screen_grab

count = 0
pic_no = 1



my_path = 'D:\Python_Projects\Chrome_Dino_Bot\Image_Processing'
path = os.path.join(my_path, "Training_Data\\")

while not keyboard.is_pressed("e"):
    
    image = screen_grab(region = (120, 530, 1850, 830))
    image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    (thresh, image) = cv2.threshold(image, 127, 255, cv2.THRESH_BINARY)
    cv2.imshow('Bot_View', image)
    cv2.waitKey(1)
    
    if count % 50 == 0:
        cv2.imwrite(f"{path}BOTView{pic_no}.jpg", image)
        print(f"Saved Picture: {pic_no}")
        pic_no += 1
    
    count += 1