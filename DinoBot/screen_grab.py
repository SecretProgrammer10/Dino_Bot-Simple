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
import numpy as np
import win32gui, win32ui, win32con, win32api

def screen_grab(region = None):
    
    window = win32gui.GetDesktopWindow()
    
    if region:
        left, top, x1, y1 = region
        width = x1 - left + 1
        height = y1 - top + 1
    
    else:
        width = win32api.GetSystemMetrics(win32con.SM_CXVIRTUALSCREEN)
        height = win32api.GetSystemMetrics(win32con.SM_CYVIRTUALSCREEN)
        left = win32api.GetSystemMetrics(win32con.SM_XVIRTUALSCREEN)
        top = win32api.GetSystemMetrics(win32con.SM_YVIRTUALSCREEN)
    
    window_dc = win32gui.GetWindowDC(window)
    src_dc = win32ui.CreateDCFromHandle(window_dc)
    memory_dc = src_dc.CreateCompatibleDC()
    bmp = win32ui.CreateBitmap()
    bmp.CreateCompatibleBitmap(src_dc, width, height)
    memory_dc.SelectObject(bmp)
    memory_dc.BitBlt((0, 0), (width, height), src_dc, (left, top), win32con.SRCCOPY)
    
    signedIntArr = bmp.GetBitmapBits(True)
    img = np.fromstring(signedIntArr, dtype = 'uint8')
    img.shape = (height, width, 4)
    
    src_dc.DeleteDC()
    memory_dc.DeleteDC()
    win32gui.ReleaseDC(window, window_dc)
    win32gui.DeleteObject(bmp.GetHandle())
    
    return cv2.cvtColor(img, cv2.COLOR_BGRA2RGB)
    