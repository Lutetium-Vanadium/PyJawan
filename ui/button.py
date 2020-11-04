from core import Rect, Surface, Drawer
from utils import Color


class Button:
    def __init__(self, x, y, w, h, text='',
                 text_col=Color.Black, hov_text_col=Color.Black,
                 font_size=16,
                 bg_col=Color.LightGray, hov_bg_col=Color.Gray,
                 border_radius=0, is_visible=True):
        self.x = x
        self.y = y
        self.w = h
        self.h = h
        self.text_col = text_col
        self.hov_text_col = hov_text_col
        self.font_size = font_size
        self.bg_col = bg_col
        self.hov_bg_col = hov_bg_col
        self.border_radius = border_radius
        self.is_visible = is_visible

    def draw(self, draw: Drawer, surf: Surface):
        if self.border_radius == 0:
            draw.rect(surf, self.x, self.y, self.w,
                      self.h, self.bg_col, fill=True)
        else:
            draw.circle(surf, self.x+self.border_radius, self.y +
                        self.border_radius, self.border_radius, color=self.bg_col)
            draw.circle(surf, self.x+self.border_radius, self.y + self.w -
                        self.border_radius, self.border_radius, color=self.bg_col)
            draw.circle(surf, self.x+self.w-self.border_radius, self.y +
                        self.border_radius, self.border_radius, color=self.bg_col)
            draw.circle(surf, self.x+self.w-self.border_radius, self.y + self.w -
                        self.border_radius, self.border_radius, color=self.bg_col)

            draw.rect(surf, self.x + self.border_radius, self.y, self.w - 2 *
                      self.border_radius, self.border_radius, self.bg_col, fill=True)
            draw.rect(surf, self.x, self.y+self.border_radius, self.w,
                      self.h-self.border_radius, self.bg_col, fill=True)
            draw.rect(surf, self.x + self.border_radius, self.y+self.h-self.border_radius, self.w - 2*self.border_radius,
                      self.border_radius, self.bg_col, fill=True)

        #     def show(self, surface, origin=None, canvas=None):
        #         if origin == None: None, font_size = None, text_color = Color.Black,
        #                  colour = Color.LightGray, hover_col = Color.LightGray, is_visible = True, activated = True, outline = False,
        #                  hover = True, value = None, surfpos = (0, 0), enabled_selected = True):
        #             origin=self.surfpos
        #         if self.is_hover(origin) and self.hovour:
        #             if self.img:
        #                 image=self.hover_img
        #             else:
        #                 colour=self.hovourColour
        #         else:
        #             if self.img:
        #                 image=self.img
        #             else:
        #                 colour=self.colour
        #         if self.img:
        #             image.set_alpha(self.alpha)
        #             surface.blit(image, self.xy)
        #         elif not self.is_visible:
        #             pg.draw.rect(surface, colour, self.rect)
        #         if self.enabled_selected and self.selected:
        #             thickness=3
        #             col=clr.select_green
        #         else:
        #             thickness=1
        #             col=self.textColour
        #         if self.is_size:
        #             pg.draw.line(surface, clr.black, (450, 50),
        #                          (550, 50), canvas.thick)
        #         if self.outline:
        #             pg.draw.line(surface, col, self.rect.topleft,
        #                          self.rect.topright, thickness)
        #             pg.draw.line(surface, col, self.rect.bottomright,
        #                          self.rect.topright, thickness)
        #             pg.draw.line(surface, col, self.rect.bottomleft,
        #                          self.rect.bottomright, thickness)
        #             pg.draw.line(surface, col, self.rect.bottomleft,
        #                          self.rect.topleft, thickness)
        #         text_surf=pg.font.SysFont(pg.font.get_default_font(), self.font_size).render(
        #             self.text, True, self.textColour)
        #         text_rect = text_surf.get_rect()
        #         text_rect.center = self.rect.center
        #         text_surf.set_alpha(self.alpha)
        #         surface.blit(text_surf, text_rect)
        #
        #     def get_click(self, origin=None):
        #         if origin == None:
        #             origin = self.surfpos
        #         temp = (self.activated and pg.mouse.get_pressed()
        #                 [0] and self.is_hover(origin))
        #         if self.flag == False and temp:
        #             self.flag = True
        #             return temp
        #         if self.flag and temp == False:
        #             self.flag = False
        #         return False
        #
