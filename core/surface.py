import numpy as np
import cv2 as cv
from utils.constants import EventType
from types import FunctionType


class Surface:
    def __init__(self, width: int, height: int, name=""):
        self.img = np.zeros((height, width, 3), dtype=np.uint8)

    @property
    def height(self):
        return self.img.shape[0]

    @property
    def width(self):
        return self.img.shape[1]

    @property
    def size(self):
        return self.img.shape[1::-1]
