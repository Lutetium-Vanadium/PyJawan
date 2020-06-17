import cv2 as cv
import numpy as np

from scipy.special import comb
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

    
    def rect(self, x, y, w, h, colour=(0, 0, 0), thickness=1, fill=False):
        colour = self._regularizeColour(colour)
        cv.rectangle(self.window.img, (x, y), (x+w, y+h), colour,-1 if fill else thickness)


    def line(self, x1, y1, x2, y2, colour=(0, 0, 0), thickness=1):
        colour = self._regularizeColour(colour)
        cv.line(self.window.img, (x1, y1), (x2, y2), colour,thickness)


    def ellipse(self, x, y, w, h, colour=(0, 0, 0), angle=0, thickness=1, fill=False):
        colour = self._regularizeColour(colour)
        cv.ellipse(self.window.img, (x+w//2, y+h//2), (w//2, h//2), angle, 0, 360, colour, thickness=-1 if fill else thickness)


    def arc(self, start_pt, stop_pt, start_angle=0, stop_angle=90, thickness=0):
        pass

  
    def curve(self, points, colour=(0, 0, 0), thickness=0, fill=False, closed=False):
        colour = self._regularizeColour(colour)
        points = self._bezier_curve(points)
        if fill:
            cv.fillPoly(self.window.img, [np.array(points).reshape((-1, 1, 2))], colour)
        else:
            cv.polylines(self.window.img, [np.array(points).reshape((-1, 1, 2))], closed, colour, thickness=thickness)


    def polygon(self, vertices, colour=(0, 0, 0), thickness=0, fill=False):
        colour = self._regularizeColour(colour)
        if fill:
            cv.fillPoly(self.window.img, [np.array(vertices).reshape((-1, 1, 2))], colour)
        else:
            cv.polylines(self.window.img, [np.array(vertices).reshape((-1, 1, 2))], closed, colour, thickness=thickness)



    def gradient(self, x, y, w, h, colour1=(0, 0, 0), colour2=(0, 0, 0)):
        colour1 = self._regularizeColour(colour1)
        colour2 = self._regularizeColour(colour2)
        c1 = np.full((1, h, 3), colour1, dtype=np.uint8)
        c2 = np.full((1, h, 3), colour2, dtype=np.uint8)
        base = np.concatenate([c1, c2], axis=0)
        grad = cv.resize(base, (h, w), cv.INTER_LINEAR)
        self.window.img[x:x+w,y:y+h] = grad


    def text(self, text, x, y, font_name=None, color=(0, 0, 0)):
        color = self._regularizeColour(color)
        img = Image.fromarray(self.window.img)
        draw = ImageDraw.Draw(img)
        draw.text((x, y), text, font = self.fonts.get(font_name), fill=color)
        self.window.img = np.array(img)

    # SECTION Helper Functions

    def _bernstein_poly(self, i, n, t):
        return comb(n, i) * ( t**(n-i) ) * (1 - t)**i

    def _bezier_curve(self, points, resol=1000):

        n = len(points)
        x, y = np.array(points).T

        t = np.linspace(0.0, 1.0, resol)


        # TODO: Fix poly_mat
        # poly_mat = np.fromfunction(lambda i, j: self._bernstein_poly(j, n, t[i]) , (resol, n))
        poly_mat = np.array([self._bernstein_poly(i, n-1, t) for i in range(0, n)])

        xvals = np.dot(x, poly_mat).astype(np.int32)
        yvals = np.dot(y, poly_mat).astype(np.int32)

        return np.vstack([xvals, yvals]).T
    
    # !SECTION