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
import time
import keyboard
import random
from screen_grab import screen_grab

f = open("stats.csv", "w")
  
time.sleep(5)
keyboard.press('space')
keyboard.release('space')

program_time = time.time()
episode_scores = []


for i in range(10):                     
    
    #look_ahead = random.randint(220, 260)
    look_ahead = 250
    ahead = look_ahead
    
    start_speedUp = random.randint(190, 210)
    count = 0
    
    zero = 0
    white = 255
    
    keyboard.press('space')
    time.sleep(2)
    keyboard.release('space')
    episode_start = time.time()
    start = time.time()
    
    while True:
        
        prev_time = time.time()
        image = screen_grab(region = (120, 530, 1850, 830))
        image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
        (thresh, image) = cv2.threshold(image, 127, 255, cv2.THRESH_BINARY)
        
        if image[146][138] == zero:
            ahead += 4
            temp = zero
            zero = white
            white = temp
        
        # three small cacti
        if image[150][ahead] == zero or image[150][ahead - 1] == zero or image[150][ahead - 2] == zero:
            keyboard.release("down")
            keyboard.press("space")
            time.sleep(0.01)
            keyboard.release("space")
            
        #bird to duck
        elif image[90][ahead] == zero:
            keyboard.press("down")
        
        #bird to jump
        elif image[175][ahead] == zero:
            keyboard.release("down")
            keyboard.press("space")
            time.sleep(0.01)
            keyboard.release("space")
        
        if image[55][835] == white and image[35][795] == zero and image[35][885] == zero:
            keyboard.release("space")
            keyboard.release("down")
            break
        
        count += int(time.time() - start)
        
        if count > start_speedUp:
            count = 0
            start = time.time()
            ahead += 1
        
    episode_score = int(time.time() - episode_start)
    if len(episode_scores) > 0:
        if max(episode_scores) < episode_score:
            print(f"New Max Score: {episode_score}\nEpisode: {i}\n Time: {int(time.time() - program_time)}")
            print(f"Look Ahead {ahead}")
        
    f.write(f"{i}, {episode_score}, {look_ahead}, {start_speedUp}\n")
    print(f"{i}, {episode_score}, {look_ahead}, {start_speedUp}\n")
    episode_scores.append(episode_score)
    keyboard.press('space')
    time.sleep(2)
    keyboard.release('space')

print(f"Episodes: {len(episode_scores)}")
print(f"Max Score: {max(episode_scores)}")
print(f"Average: {sum(episode_scores) / len(episode_scores)}")
f.close()



'''#three big cacti
        if image[80][ahead] == zero or image[80][ahead - 1] == zero or image[80][ahead - 2] == zero:
            keyboard.release("down")
            keyboard.press("space")
            time.sleep(0.02)
            keyboard.release("space")
        
        #small cactus
        elif image[130][ahead] == zero:
            keyboard.release("down")
            keyboard.press("space")
            time.sleep(0.01)
            keyboard.release("space")
        
        #big cactus
        elif image[80][ahead] == zero:
            keyboard.release("down")
            keyboard.press("space")
            time.sleep(0.02)
            keyboard.release("space")'''
            
            