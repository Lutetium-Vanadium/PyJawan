from core.window import Window

class Drawer:
    def __init__(self, window: Window):
        self.window = window
    
    def _regularizeColour(colour):
        if isinstance(colour, Colours):
            return colour.value
        return colour

    
    def rect(self, x, y, width, height, colour = [0, 0, 0]):
        colour = self._regularizeColour(colour)
        self.window.img[y:y+height, x:x+width] = colour

    def square(self, x, y, side, colour = [0, 0, 0]):
        colour = self._regularizeColour(colour)
        self.window.img[y:y+side, x:x+side] = colour