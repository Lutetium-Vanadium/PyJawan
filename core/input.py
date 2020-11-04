from pynput import mouse, keyboard
from pyautogui import


class Input:
    pass


class Mouse(Input):
    def __init__(self):
        self.x = mouseX
        self.y = mouseY
        self.button = button
        self.pressed = pressed
