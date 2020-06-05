from core.window import Window
from utils.colour import Colours
import cv2 as cv
import numpy as np
import time

from utils.constants import FRAME_RATE
from utils.colour import colour

win = Window(800, 600)
win.draw(200, 150, 400, 300, Colours.RebeccaPurple)

av_time = 0
c = 0

while True:
    key = cv.waitKey(100) &  0xFF

    if key == 27:
        break
    
    t = time.time()
    win.draw(200, 150, 400, 300, colour(np.random.randint(0, 256**3-1)))
    if win.render():
        break

    
    time.sleep(1./FRAME_RATE)
    av_time = (av_time*c + time.time()-t)/(c+1)

    print(av_time)
    c+=1


win.close()
