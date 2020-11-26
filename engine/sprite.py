from core import Surface, Rect


class Sprite:
    def __init__(self, x, y, w, h):
        self.rect = Rect(x, y, w, h)
        self.alive = True

    def render(self, surf: Surface):
        pass

    def update(self, delta: int):
        pass

    def kill(self):
        print('Life is soup, I am fork -', str(self))
        self.alive = False

    def collides(self, sprite) -> bool:
        return self.rect.collides(sprite.rect)
