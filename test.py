import cv2 as cv
import numpy as np
import time

from core.window import Window
from core.draw import Drawer

from utils.constants import FRAME_RATE
from utils.color import Color

win = Window(1920, 1080)
draw = Drawer(win)

av_time = 0
c = 0

while True:
    key = cv.waitKey(100) &  0xFF

    if key == 27:
        break
        
    
    t = time.time()
    # draw.polygon([[200, 390], [420, 104], [66, 88]], Color(np.random.randint(0, 256**3-1)), thickness=1, fill=True)
    draw.text("Hello, World!", 100, 200, 50, color=Color(np.random.randint(0, 256**3-1)))
    if win.render():
        break

    
    time.sleep(1./FRAME_RATE)
    av_time = (av_time*c + time.time()-t)/(c+1)

    print(av_time)
    c+=1


win.close()
