class Rect:
    def __init__(self, x: int, y: int, w: int, h: int):
        if w < 0:
            w = -w
            x = x-w

        if h < 0:
            h = -h
            y = y-h

        self.x = x
        self.y = y
        self.w = w
        self.h = h

    def area(self) -> int:
        return self.w * self.h

    def collides(self, rect) -> bool:
        return rect.x < self.x < rect.x + rect.w and rect.y < self.y < rect.y + rect.h

    def top_left(self):
        return (self.x, self.y)

    def top_right(self):
        return (self.x+self.w, self.y)

    def bottom_left(self):
        return (self.x, self.y+self.w)

    def bottom_right(self):
        return (self.x+self.w, self.y+self.h)

    def center(self):
        return (self.x+self.w//2, self.y+self.h//2)
