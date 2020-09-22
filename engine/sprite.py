from core import Surface, Rect


class Sprite:
    def __init__(self):
        self.rect = Rect()
        self.alive = True

    def render(self, surf: Surface):
        pass

    def update(self, delta: int):
        pass

    def kill(self):
        self.alive = False

    def collides(self, sprite: Sprite) -> bool:
        return self.rect.collides(sprite.rect)
