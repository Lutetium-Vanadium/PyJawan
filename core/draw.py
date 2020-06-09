import cv2 as cv
import numpy as np
from PIL import Image, ImageDraw

from utils.colour import Colours

class Drawer:
    def __init__(self, window):
        self.window = window
        self.fonts = {}

    def load_font(self, name, path):
        self.fonts.set(name, ImageFont.load_path(path))

    def _regularizeColour(self, colour):
        if isinstance(colour, Colours):
            return colour.value
        return colour

    
    def rect(self, x, y, w, h, colour=(0, 0, 0), thickness=0, fill=True):
        colour = self._regularizeColour(colour)
        cv.rectangle(self.window.img, (x, y), (x+w, y+h), colour,-1 if fill else thickness)


    def line(self, x1, y1, x2, y2, colour=(0, 0, 0), thickness=1):
        colour = self._regularizeColour(colour)
        cv.line(self.window.img, (x1, y1), (x2, y2), colour,thickness)

    def ellipse(self, x, y, w, h, colour=(0, 0, 0), thickness=0, fill=True):
        colour = self._regularizeColour(colour)
        cv.ellipse(self.window.img, (x, y, w, h), colour)#, thickness=-1 if fill else thickness)

    # TODO arc
    def arc(self, start_pt, stop_pt, start_angle=0, stop_angle=90, thickness=0):
        pass

    def polygon(self, vertices, thickness=0, fill=True):
        colour = self._regularizeColour(colour)
        cv.polylines(self.window.img, [np.array(vertices).reshape((-1, 1, 2))], fill, colour, thickness)

    def gradient(self, x, y, w, h, colour1=(0, 0, 0), colour2=(0, 0, 0)):
        c1 = np.full((1, h, 3), colour1, dtype=np.uint8)
        c2 = np.full((1, h, 3), colour2, dtype=np.uint8)
        base = np.concatenate([c1, c2], axis=0)
        grad = cv.resize(base, (w, h), cv.INTER_LINEAR)
        self.window[x:x+w,y:y+w] = grad

    def text(self, x, y, font_name=None):
        img = Image.fromarray(self.window)
        draw = ImageDraw.Draw(img)
        draw.text((x, y), text, font = this.fonts.get(font_name), fill = colour)
        self.window = np.array(img)



    
    