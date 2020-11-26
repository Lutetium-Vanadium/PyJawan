from core.draw import Drawer
from core.rect import Rect
from utils import Color
import numpy as np
import cv2 as cv
from utils.constants import EventType
from types import FunctionType


class Surface:
    def __init__(self, width: int, height: int):
        self.img = np.zeros((height, width, 3), dtype=np.uint8)
        self.drawer = Drawer()

    @property
    def height(self):
        return self.img.shape[0]

    @property
    def width(self):
        return self.img.shape[1]

    @property
    def size(self):
        return self.img.shape[1::-1]

    def draw_rect(self, x: int, y: int, w: int, h: int, color=Color.Black, thickness=1, fill=False):
        self.drawer.rect(self, x, y, w, h, color, thickness, fill)

    def draw_fill(self, color=Color.Black):
        self.drawer.fill(self, color)

    def draw_line(self, x1: int, y1: int, x2: int, y2: int, color=Color.Black, thickness=1):
        self.drawer.line(self, x1, y1, x2, y2, color, thickness)

    def draw_circle(self, x: int, y: int, r: int, color=Color.Black, thickness=1, fill=False):
        self.drawer.circle(self, x, y, r, color, thickness, fill)

    def draw_ellipse(self, x: int, y: int, w: int, h: int, color=Color.Black, angle=0, thickness=1, fill=False):
        self.drawer.ellipse(self, x, y, w, h, color, angle, thickness, fill)

    def draw_curve(self, points: list, color=Color.Black, thickness=0, fill=False, closed=False):
        self.drawer.curve(self, points, color, thickness, fill, closed)

    def draw_polygon(self, vertices: list, color=Color.Black, thickness=0, fill=False):
        self.drawer.polygon(self, vertices, color, thickness, fill)

    def draw_gradient(self, x: int, y: int, w: int, h: int, color1=Color.Black, color2=Color.Black):
        self.drawer.gradient(self, x, y, w, h, color1, color2)

    def draw_text(self, text: str, x: int, y: int, size=10, font_name="sans-serif", font_path="", color=Color.Black):
        self.drawer.text(self, text, x, y, size, font_name, font_path, color)

    def draw_surface(self, to_draw, x: int, y: int):
        self.drawer.surface(self, to_draw, x, y)

    def draw_image(self, path: str, rect: Rect):
        self.drawer.image(self, path, rect)
