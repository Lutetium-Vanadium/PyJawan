from core.window import Window
from utils.colour import Colours
import cv2 as cv
import time

win = Window(800, 600)

win.draw(200, 150, 400, 300, Colours.RebeccaPurple)

while True:
    key = cv.waitKey(100) &  0xFF

    if key == 27:
        break

    if win.render():
        break
    time.sleep(0.5)
    

win.close()
