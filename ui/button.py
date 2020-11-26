from core import Rect, Surface, Drawer, Window
from utils.constants import EventType
from types import FunctionType
from utils import Color


class Button:
    def __init__(self, x: int, y: int, w: int, h: int, text='',
                 text_col=Color.Black, hov_text_col=Color.Black,
                 font_size=16,
                 bg_col=Color.LightGray, hov_bg_col=Color.Gray,
                 border_radius=0, is_visible=True):
        self.x = x
        self.y = y
        self.w = h
        self.h = h
        self.text = text
        self.text_col = text_col
        self.hov_text_col = hov_text_col
        self.font_size = font_size
        self.bg_col = bg_col
        self.hov_bg_col = hov_bg_col
        self.border_radius = border_radius
        self.is_visible = is_visible
        self.id = 'button-' + str(id(self))
        self.is_hovering = False
        self.click_handler = None

    def _is_hovering(self, e):
        print(e.x, e.y)
        self.is_hovering = self.x < e.x < (
            self.x + self.w) and self.y < e.y < (self.y + self.h)

    def on_click(self, f: FunctionType):
        self.click_handler = f

    def register(self, window: Window):
        window.on(EventType.MouseMove, self.id, self._is_hovering)
        window.on(EventType.MouseClick, self.id, lambda e: self.click_handler(
            e) if self.click_handler else None)

    def destory(self, window: Window):
        window.off(EventType.MouseMove, self.id)
        window.off(EventType.MouseClick, self.id)

    def draw(self, surf: Surface):
        text_col = self.hov_text_col if self.is_hovering else self.text_col
        bg_col = self.hov_bg_col if self.is_hovering else self.bg_col

        if self.border_radius == 0:
            surf.draw_rect(self.x, self.y, self.w,
                           self.h, bg_col, fill=True)
        else:
            surf.draw_circle(self.x+self.border_radius, self.y +
                             self.border_radius, self.border_radius, color=bg_col, fill=True)

            surf.draw_circle(self.x+self.border_radius, self.y + self.h -
                             self.border_radius, self.border_radius, color=bg_col, fill=True)

            surf.draw_circle(self.x+self.w-self.border_radius, self.y +
                             self.border_radius, self.border_radius, color=bg_col, fill=True)

            surf.draw_circle(self.x+self.w-self.border_radius, self.y + self.h -
                             self.border_radius, self.border_radius, color=bg_col, fill=True)

            surf.draw_rect(self.x + self.border_radius, self.y, self.w - 2 *
                           self.border_radius, self.border_radius, color=bg_col, fill=True)

            surf.draw_rect(self.x, self.y+self.border_radius, self.w,
                           self.h-2*self.border_radius, color=bg_col, fill=True)

            surf.draw_rect(self.x + self.border_radius, self.y+self.h-self.border_radius, self.w - 2*self.border_radius,
                           self.border_radius, color=bg_col, fill=True)

        if self.text and len(self.text):
            surf.draw_text(self.text, self.x + 2, self.y + self.h/2 -
                           self.font_size / 2, self.font_size, color=text_col)
