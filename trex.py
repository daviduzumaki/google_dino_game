import numpy as np
import cv2
from mss import mss
import pyautogui

region_of_interest = {

    'left': 688,
    'top': 371,
    'width': 88,
    'height': 40
}
k = 1

while True:
    monitor = mss().grab(region_of_interest)  # Capture region of interest
    monitor = np.array(monitor)  # convert image into numpy array

    # [red,green,blue]
    cactus = monitor[28, :, 0]  # storing red channel(x values) of cactus [row,column,channel] from 30th pixel of y
    bird = monitor[1, :, 0]  # storing red channel(x values) of bird from 1st pixel

    cactus_sum = np.sum(cactus)
    bird_sum = np.sum(bird)
    print(cactus_sum, 'cactus')
    print(bird_sum, 'bird')

    if cactus_sum < 21736:
        pyautogui.press('up')

    if bird_sum < 21736:
        pyautogui.keyDown('down')
        k = 1

    if bird_sum == 21736 and k == 1:
        pyautogui.keyUp('down')
        k = 0


    cv2.imshow('trex', monitor)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        cv2.destroyAllWindows()
        break
