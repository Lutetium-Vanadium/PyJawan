import sys
sys.path.append("../")
from core import Window, Drawer, Surface, Rect, KeyDownEvent
from engine import Sprite
from utils import FRAME_RATE, EventType, Color
import os
from random import randint
from typing import Tuple


# SECTION Constants

MAX_VERTICAL_VEL = -15
MIN_VERTICAL_VEL = 15
SPEED = 10
SLIT_WIDTH = 200
PIPE_SEP = 100
UP_ACCEL = -50
DOWN_ACCEL = 50
GRAVITY = 3

# !SECTION Constants

# SECTION Helper functions


def random_height(win_height) -> Tuple[int, int]:
    top = randint(0, win_height - SLIT_WIDTH - 1)
    bottom = randint(0, win_height - top - SLIT_WIDTH)
    return top, bottom

# !SECTION

# SECTION Classes


class Pipe(Sprite):
    def __init__(self, start_x: int, top: int, bottom: int, speed: int):
        super().__init__(start_x, 0, 100, 100)
        self.top = top
        self.bottom = bottom
        self.speed = speed

    def render(self, surf: Surface):
        if not self.alive:
            return

        if surf.height < (self.top + self.bottom):
            raise RuntimeError(
                f"Pipe must have opening: surface height: {surf.height}, pipe height: {self.top}, {self.bottom}")

        surf.draw_rect(self.rect.x, 0, 10, self.top,
                       color=Color.Black, fill=True)

        surf.draw_rect(self.rect.x, surf.height - self.bottom, 10, self.bottom,
                       color=Color.Black, fill=True)

    def update(self):
        self.rect.x -= self.speed

        if self.rect.x <= 0:
            self.rect.x = win_rect.w


class Bird(Sprite):
    def __init__(self, x, y, up_im: str, down_im: str, accel=GRAVITY):
        super().__init__(x, y, 40, 40)
        self.accel = accel
        self.up_im = up_im
        self.down_im = down_im
        self.vertical_velocity = 0

    def livent(self):
        print("Life is soup, I am fork")
        self.alive = False

    def jump(self):
        self.accel = UP_ACCEL

    def render(self, surf: Surface):
        if not self.alive:
            return
        if self.vertical_velocity > 0:
            surf.drawer.image(surf, self.down_im, self.rect)
        else:
            surf.drawer.image(surf, self.up_im, self.rect)

    def update(self, win_height: int):
        if not self.alive:
            return

        print(self.vertical_velocity, self.accel)
        self.vertical_velocity += self.accel
        self.vertical_velocity = max(self.vertical_velocity, MAX_VERTICAL_VEL)
        self.vertical_velocity = min(self.vertical_velocity, MIN_VERTICAL_VEL)
        self.rect.y += self.vertical_velocity

        if self.rect.y < 0 or self.rect.y > win_height:
            self.livent()

        self.accel = GRAVITY

        self.accel = GRAVITY

# !SECTION

# SECTION Main functionality


win = Window(1280, 720)
win_rect = Rect(0, 0, 1280, 720)

heights = [random_height(win.height) for i in range(win_rect.w // PIPE_SEP)]
pipes = [Pipe(win_rect.w - i * PIPE_SEP, h[0], h[1], SPEED)
         for i, h in enumerate(heights)]

bird = Bird(100, 360, "./assets/bird_up.png",
            "./assets/bird_down.png")


# def handle_key(e: KeyDownEvent):
#     if e.key ==


win.on(EventType.KeyDown, 'space-handler', print)


def main(dt: int):
    win.draw_image("./assets/flappy-bird-1.png", win_rect)
    for pipe in pipes:
        pipe.render(win)
        pipe.update()

    bird.render(win)
    bird.update(win.height)


win.off(EventType.KeyDown, 'space-handler')
win.loop(main)
win.close()
