import numpy as np
import cv2 as cv
from utils.constants import EventType
from types import FunctionType
import time
from core.event import *
from pynput import mouse, keyboard
from core.surface import Surface


class Window(Surface):
    def __init__(self, width: int, height: int, name="PyJawan"):
        super().__init__(width, height)
        self.name = name
        self.window = cv.namedWindow(
            name, cv.WINDOW_NORMAL | cv.WINDOW_GUI_NORMAL)
        cv.resizeWindow(name, width, height)
        self.handlers = {
            EventType.KeyUp: {},
            EventType.KeyDown: {},
            EventType.MouseClick: {},
            EventType.MouseMove: {}
        }
        self.mouseEvent = None
        self._registerListener()
        self.stop = False

    @property
    def height(self):
        return self.img.shape[0]

    @property
    def width(self):
        return self.img.shape[1]

    @property
    def size(self):
        return self.img.shape[1::-1]

    def render(self):
        if cv.getWindowProperty(self.name, 4) == 0:
            return False

        cv.imshow(self.name, self.img)

        return True

    def loop(self, main: FunctionType, delay=50):
        while self.render() or not self.stop:
            current_time = time.time()
            key = cv.waitKey(delay) & 0xFF
            dt = time.time() - current_time
            main(dt)
            dt = time.time() - current_time
            if dt < delay:
                time.sleep((delay - dt) / 1000)

    def quit(self):
        self.stop = True

    def close(self):
        cv.destroyAllWindows()

    def on(self, event_type: EventType, handler_id: str, fn: FunctionType):
        self.handlers[event_type][handler_id] = fn

    def off(self, event_type: EventType, handler_id: str):
        self.handlers[event_type].pop(handler_id)

    def _callHandler(self, event_type: EventType, event: Event):
        if event_type == EventType.MouseMove or event_type == EventType.MouseClick:
            win_rect = cv.getWindowImageRect(self.name)
            event.x -= win_rect[0]
            event.y -= win_rect[1]

            event.x *= self.width / win_rect[2]
            event.y *= self.height / win_rect[3]

            # Out of bounds
            if event.x < 0 or event.x >= self.width or event.y < 0 or event.y >= self.height:
                return

        if event_type == EventType.MouseMove:
            self.mouseEvent = event

        for handler in self.handlers[event_type].values():
            handler(event)

    def _registerListener(self):
        mouse_listener = mouse.Listener(
            on_move=lambda x, y: self._callHandler(
                EventType.MouseMove, MouseMoveEvent(x, y, self.mouseEvent)),
            on_click=lambda x, y, btn, pressed: self._callHandler(
                EventType.MouseClick, MouseClickEvent(x, y, btn, pressed))
        )

        mouse_listener.start()

        key_listener = keyboard.Listener(
            on_press=lambda key: self._callHandler(
                EventType.KeyDown, KeyDownEvent(key)),
            on_release=lambda key: self._callHandler(
                EventType.KeyUp, KeyUpEvent(key))
        )

        key_listener.start()
