import os
from utils.constants import HorizontalAlignment, VerticalAlignment
import cv2 as cv
import numpy as np

from math import factorial
from PIL import Image, ImageDraw, ImageFont
from numpy.core.fromnumeric import shape
from numpy.core.numeric import zeros_like

from utils.color import Color
from core.rect import Rect
# from core.surface import Surface

BASE_DIR = os.path.join(os.path.abspath(os.pardir), "utils", "fonts")


class Drawer:
    def __init__(self):
        self.fonts = {}
        self.images = {}
    # SECTION Helper Functions

    def _bernstein_poly(self, i, n, t):
        return factorial(n) / (factorial(i) * factorial(n - i)) * (t**(n - i)) * (1 - t)**i

    def _bezier_curve(self, points, resol=1000):

        n = len(points)
        x, y = np.array(points).T

        t = np.linspace(0.0, 1.0, resol)

        # TODO: Fix poly_mat
        # poly_mat = np.fromfunction(lambda i, j: self._bernstein_poly(j, n, t[i]) , (resol, n))
        poly_mat = np.array([self._bernstein_poly(i, n - 1, t)
                             for i in range(0, n)])

        xvals = np.dot(x, poly_mat).astype(np.int32)
        yvals = np.dot(y, poly_mat).astype(np.int32)

        return np.vstack([xvals, yvals]).T

    # !SECTION

    def load_font(self, name, path):
        self.fonts.set(name, ImageFont.load_path(path))

    def rect(self, surf, x: int, y: int, w: int, h: int, color=Color.Black, thickness=1, fill=False):
        cv.rectangle(surf.img, (x, y), (x + w, y + h),
                     color.bgr, -1 if fill else thickness)

    def fill(self, surf, color=Color.Black):
        surf.img[:, :] = color.bgr

    def line(self, surf, x1: int, y1: int, x2: int, y2: int, color=Color.Black, thickness=1):
        cv.line(surf.img, (x1, y1), (x2, y2), color.bgr, thickness)

    def circle(self, surf, x: int, y: int, r: int, color=Color.Black, thickness=1, fill=False):
        cv.ellipse(surf.img, (x, y), (r, r),
                   360, 0, 360, color.bgr, thickness=-1 if fill else thickness)

    def ellipse(self, surf, x: int, y: int, w: int, h: int, color=Color.Black, angle=0, thickness=1, fill=False):
        cv.ellipse(surf.img, (x, y), (w // 2, h // 2),
                   angle, 0, 360, color.bgr, thickness=-1 if fill else thickness)

    def arc(self, surf, start_pt: int, stop_pt: int, start_angle=0, stop_angle=90, color=Color.Black, thickness=0):
        # TODO
        pass

    def curve(self, surf, points: list, color=Color.Black, thickness=0, fill=False, closed=False):
        points = self._bezier_curve(points)
        if fill:
            cv.fillPoly(surf.img, [np.array(
                points).reshape((-1, 1, 2))], color.bgr)
        else:
            cv.polylines(surf.img, [np.array(points).reshape(
                (-1, 1, 2))], closed, color.bgr, thickness=thickness)

    def polygon(self, surf, vertices: list, color=Color.Black, thickness=0, fill=False):
        if fill:
            cv.fillPoly(surf.img, [np.array(
                vertices).reshape((-1, 1, 2))], color.bgr)
        else:
            cv.polylines(surf.img, [np.array(vertices).reshape(
                (-1, 1, 2))], True, color.bgr, thickness=thickness)

    def gradient(self, surf, x: int, y: int, w: int, h: int, color1=Color.Black, color2=Color.Black):
        c1 = np.full((1, h, 3), color1.bgr, dtype=np.uint8)
        c2 = np.full((1, h, 3), color2.bgr, dtype=np.uint8)
        base = np.concatenate([c1, c2], axis=0)
        grad = cv.resize(base, (w, h), cv.INTER_LINEAR)
        surf.img[y:y + h, x:x + w] = grad

    def text(
        self, surf, text: str, x: int, y: int,
        size=10, font_name="sans-serif", font_path="", color=Color.Black,
        h_align=HorizontalAlignment.Left,
        v_align=VerticalAlignment.Center
    ):
        if font_name in ("monospace", "serif", "sans-serif"):
            font = ImageFont.truetype(os.path.join(BASE_DIR, f"{font_name}.ttf"), size)
        else:
            font = ImageFont.load(font_path, size)

        img = Image.fromarray(surf.img)
        draw = ImageDraw.Draw(img)
        (w, h) = draw.textsize(text, font=font)

        if h_align == HorizontalAlignment.Center:
            x -= w // 2
        elif h_align == HorizontalAlignment.Right:
            x -= w

        if v_align == VerticalAlignment.Center:
            y -= h // 2
        elif v_align == VerticalAlignment.Bottom:
            y -= h

        draw.text((x, y), text, font=font, fill=color.bgr)
        surf.img = np.array(img)

    def surface(self, surf, to_draw, x: int, y: int,):
        surf.img[y:y + to_draw.height, x:x +
                 to_draw.width] = to_draw.img.copy()

    def image(self, surf, path: str, rect: Rect):
        im = self.images.get(path)
        if im is None:
            im = cv.imread(path, cv.IMREAD_UNCHANGED)
            self.images[path] = im

        im = cv.resize(im, (rect.w, rect.h))
        try:
            mask = 255 * np.zeros((*im.shape[:2], 3), dtype=np.uint8)
            mask[im[:, :, 3] == 0] = 255
            surf.img[rect.y:rect.y + rect.h, rect.x:rect.x + rect.w] = (
                im[:, :, :-1] | surf.img[rect.y:rect.y +
                                         rect.h, rect.x: rect.x + rect.w] & mask
            )

        except:
            surf.img[rect.y: rect.y + rect.h, rect.x: rect.x +
                     rect.w] = im
