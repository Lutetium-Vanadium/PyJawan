import cv2 as cv
import numpy as np

from scipy.special import comb
from PIL import Image, ImageDraw, ImageFont

from utils.color import Color

class Drawer:
    def __init__(self, window):
        self.window = window
        self.fonts = {}

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


    def load_font(self, name, path):
        self.fonts.set(name, ImageFont.load_path(path))


    def rect(self, x, y, w, h, color=Color.Black, thickness=1, fill=False):
        cv.rectangle(self.window.img, (x, y), (x+w, y+h), color.bgr, -1 if fill else thickness)


    def line(self, x1, y1, x2, y2, color=Color.Black, thickness=1):
        cv.line(self.window.img, (x1, y1), (x2, y2), color.bgr, thickness)


    def ellipse(self, x, y, w, h, color=Color.Black, angle=0, thickness=1, fill=False):
        cv.ellipse(self.window.img, (x+w//2, y+h//2), (w//2, h//2), angle, 0, 360, color.bgr, thickness=-1 if fill else thickness)


    def arc(self, start_pt, stop_pt, start_angle=0, stop_angle=90, color=Color.Black, thickness=0):
        pass

  
    def curve(self, points, color=Color.Black, thickness=0, fill=False, closed=False):
        points = self._bezier_curve(points)
        if fill:
            cv.fillPoly(self.window.img, [np.array(points).reshape((-1, 1, 2))], color.bgr)
        else:
            cv.polylines(self.window.img, [np.array(points).reshape((-1, 1, 2))], closed, color.bgr, thickness=thickness)


    def polygon(self, vertices, color=Color.Black, thickness=0, fill=False):
        if fill:
            cv.fillPoly(self.window.img, [np.array(vertices).reshape((-1, 1, 2))], color.bgr)
        else:
            cv.polylines(self.window.img, [np.array(vertices).reshape((-1, 1, 2))], closed, color.bgr, thickness=thickness)


    def gradient(self, x, y, w, h, color1=Color.Black, color2=Color.Black):
        c1 = np.full((1, h, 3), color1.bgr, dtype=np.uint8)
        c2 = np.full((1, h, 3), color2.bgr, dtype=np.uint8)
        base = np.concatenate([c1, c2], axis=0)
        grad = cv.resize(base, (h, w), cv.INTER_LINEAR)
        self.window.img[x:x+w,y:y+h] = grad


    def text(self, text, x, y, size=10, font_name="sans-serif", font_path="", color=Color.Black):
        if font_name in ("monospace", "serif", "sans-serif"):
            font = ImageFont.truetype(f"utils/fonts/{font_name}.ttf", size)
        else:
            font = ImageFont.load(font_path, size)
        img = Image.fromarray(self.window.img)
        draw = ImageDraw.Draw(img)
        draw.text((x, y), text, font=font, fill=color.bgr)
        self.window.img = np.array(img)
