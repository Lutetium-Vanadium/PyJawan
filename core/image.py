
import numpy as np
import cv2 as cv
from utils.constants import EventType
from types import FunctionType

from core.surface import Surface


class Image(Surface):
    def __init__(self, path):
        self.img = cv.imread(path)
        if not self.img:
            raise RuntimeError(
                f"Image at \"{path}\" does not exist. Please give the right path to the image")

    @property
    def height(self):
        return self.img.shape[0]

    @property
    def width(self):
        return self.img.shape[1]

    @property
    def size(self):
        return self.img.shape[1::-1]
