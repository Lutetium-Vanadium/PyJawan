import numpy as np
import cv2 as cv
from utils.colour import Colours

class Window():
    def __init__(self, width, height, name="GUI lib"):
        self.name = name
        self.img = np.zeros((height, width, 3), dtype=np.uint8)
        self.window = cv.namedWindow(name, cv.WINDOW_NORMAL | cv.WINDOW_GUI_NORMAL)
        cv.resizeWindow(name, width, height)

    @property
    def height(self):
        return self.img.shape[0]
    
    @property
    def width(self):
        return self.img.shape[1]
    
    @property
    def size(self):
        return self.img.shape[1::-1]
    
    def render(self):
        if cv.getWindowProperty(self.name, 4) == 0:
            return True
        
        cv.imshow(self.name, self.img)

        return False

    def close(self):
        cv.destroyAllWindows()

    def draw(self, x, y, width, height, colour):
        if isinstance(colour, Colours):
            colour = colour.value
        self.img[y:y+height, x:x+width] = colour
