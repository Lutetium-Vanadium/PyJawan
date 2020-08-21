import numpy as np
import cv2 as cv
from utils.constants import EventType
from types import FunctionType
import time
from core.event import *
from pynput import mouse, keyboard


class Window():
    def __init__(self, width: int, height: int, name="GUI lib"):
        self.name = name
        self.img = np.zeros((height, width, 3), dtype=np.uint8)
        self.window = cv.namedWindow(
            name, cv.WINDOW_NORMAL | cv.WINDOW_GUI_NORMAL)
        cv.resizeWindow(name, width, height)
        self.handlers = {
            EventType.Keypress: {},
            EventType.MouseClick: {},
            EventType.MouseMove: {}
        }
        self.mouseEvent = None

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

    # def loop(self, main: FunctionType, delay: int):
    #     while self.render():
    #         current_time = time.time()
    #         key = cv.waitKey(delay) &  0xFF
    #         dt = time.time() - current_time
    #         if dt > delay:
    #             time.sleep(delay - dt)
    #         main()

    def close(self):
        cv.destroyAllWindows()

    def on(self, event_type: EventType, handler_id: str, fn: FunctionType):
        self.handlers[event_type][handler_id] = fn

    def off(self, event_type: EventType, handler_id: str):
        self.handlers[event_type].pop(handler_id)

    def _callHandler(self, event_type: EventType, event: Event):
        if event_type == EventType.MouseMove:
            self.mouseEvent = event

        for handler in self.handlers[event_type].values():
            hander(event)

    def _registerListener(self):
        with pynput.mouse.Listener(on_move=lambda x, y: self._callHandler(EventType.MouseMove, MouseMoveEvent(x, y, self.mouseEvent)) as listener:
            listener.join()
