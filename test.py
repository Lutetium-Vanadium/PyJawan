import cv2 as cv
import numpy as np
import time

from core.window import Window
from core.draw import Drawer
from utils.colour import Colours

from utils.constants import FRAME_RATE
from utils.colour import colour

win = Window(800, 600)
draw = Drawer(win)

av_time = 0
c = 0

while True:
    key = cv.waitKey(100) &  0xFF

    if key == 27:
        break
    
    t = time.time()
    # draw.rect(200, 150, 400, 300, colour(np.random.randint(0, 256**3-1)), thickness=10, fill=False)
    draw.ellipse(200, 150, 400, 300, colour(np.random.randint(0, 256**3-1)), thickness=10, fill=False)
    if win.render():
        break

    
    time.sleep(1./FRAME_RATE)
    av_time = (av_time*c + time.time()-t)/(c+1)

    print(av_time)
    c+=1


win.close()
