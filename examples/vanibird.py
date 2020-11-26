import sys
sys.path.append("../")
from core import Window, Drawer, Surface, Rect, KeyDownEvent, Key
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
PIPE_SEP = 250
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
    def __init__(self, start_x: int, top: int, bottom: int, speed: int, win_height: int):
        super().__init__(start_x, 0, 100, 100)
        self.top = top
        self.width = 10
        self.bottom = bottom
        self.speed = speed
        self.win_height = win_height

    def render(self, surf: Surface):
        if not self.alive:
            return

        if surf.height < (self.top + self.bottom):
            raise RuntimeError(
                f"Pipe must have opening: surface height: {surf.height}, pipe height: {self.top}, {self.bottom}")

        surf.draw_rect(self.rect.x, 0, self.width, self.top,
                       color=Color.Black, fill=True)

        surf.draw_rect(self.rect.x, surf.height - self.bottom, self.width, self.bottom,
                       color=Color.Black, fill=True)

    def update(self):
        self.rect.x -= self.speed

        if self.rect.x <= 0:
            self.rect.x = win_rect.w

    def collides(self, sprite: Sprite) -> bool:
        return sprite.rect.collides(
            Rect(self.rect.x, 0, self.width, self.top)
        ) or sprite.rect.collides(
            Rect(self.rect.x, self.win_height -
                 self.bottom, self.width, self.bottom)
        )


class Bird(Sprite):
    def __init__(self, x, y, up_im: str, down_im: str, accel=GRAVITY):
        super().__init__(x, y, 40, 40)
        self.accel = accel
        self.up_im = up_im
        self.down_im = down_im
        self.vertical_velocity = 0

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

        self.vertical_velocity += self.accel
        self.vertical_velocity = max(self.vertical_velocity, MAX_VERTICAL_VEL)
        self.vertical_velocity = min(self.vertical_velocity, MIN_VERTICAL_VEL)
        self.rect.y += self.vertical_velocity

        if self.rect.y < 0 or self.rect.y >= win_height - self.rect.h:
            self.kill()
        self.accel = GRAVITY

# !SECTION

# SECTION Main functionality


win = Window(1280, 720)
win_rect = Rect(0, 0, 1280, 720)

heights = [random_height(win.height) for i in range(win_rect.w // PIPE_SEP)]
pipes = [Pipe(win_rect.w - i * PIPE_SEP + 100, h[0], h[1], SPEED, win.height)
         for i, h in enumerate(heights)]

bird = Bird(100, 360, "./assets/bird_up.png",
            "./assets/bird_down.png",)


def handle_key(e: KeyDownEvent):
    if e.key == Key.space:
        bird.jump()


win.on(EventType.KeyDown, 'space-handler', handle_key)


def main(dt: int):
    if bird.alive:
        win.draw_image("./assets/flappy-bird-1.png", win_rect)
        bird.render(win)

        for pipe in pipes:
            if pipe.collides(bird):
                bird.kill()
            pipe.render(win)
            pipe.update()

        bird.update(win.height)


win.loop(main, 20)
win.off(EventType.KeyDown, 'space-handler')
win.close()
