from core.window import Window
from utils.colour import colour
import cv2 as cv
import time

win = Window(200, 100)

print(win.size)

win.draw(50, 30, 100, 40, colour(95, 55, 245))

while True:
    key = cv.waitKey(100) &  0xFF

    if key == 27:
        break

    if win.render():
        break
    time.sleep(0.5)
    

win.close()
