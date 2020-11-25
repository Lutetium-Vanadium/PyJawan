import os
from random import randint
from core import Window, Drawer, Surface
from engine import Sprite
from utils.constants import FRAME_RATE, EventType
from utils.color import Color
from core import Window, Drawer

win = Window(1920, 1080)

av_time = 0
c = 0


def main(dt: int):
    print(dt)


win.loop(main)

win.close()


class Pipe(Sprite):
    def __init__(self, top: int, bottom: int, type: str, speed: float):
        super().__init__()
        self.top = top
        self.bottom = bottom
        self.spawned = False

    def render(self, surf: Surface):
        if !self.alive:
            return

        if !self.spawned:
            self.rect.x = surf.width

        if surf.width > (self.top + self.bottom):
            raise RuntimeError("Pipe must have opening")

        surf.drawer.line(surf, self.rect.x, 0, self.rect.x,
                         self.top, color=Color.Black, thickness=10)
        surf.drawer.line(surf, self.rect.x, surf.width,
                         self.rect.x, surf.bottom, color=Color.Black, thickness=10)

    def update(self, delta: float):
        if !self.spawned:
            self.rect.x = surf.width

        self.rect.x -= speed*delta

        if self.rect.x <= 0:
            self.kill()
