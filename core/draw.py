from core.window import Window

class Drawer:
    def __init__(self, window: Window):
        self.window = window
    
    def _regularizeColour(colour):
        if isinstance(colour, Colours):
            return colour.value
        return colour

    
    def rect(self, x, y, w, h, colour=(0, 0, 0), thickness=0, fill=True):
        colour = self._regularizeColour(colour)
        cv.rectangle(self.window.img, (x, y), (x+w, y+h), colour,-1 if fill else thickness)


    def line(self, x1, y1, x2, y2, color=(0, 0, 0), thickness=1):
        colour = self._regularizeColour(colour)
        cv.line(self.window.img, (x1, y1), (x2, y2), colour,thickness)

    def ellipse(self, x, y, w, h color=(0, 0, 0), thickness=0, fill=True):
        colour = self._regularizeColour(colour)
        cv.ellipse(self.window.img, (x, y, w, h), colour, -1 if fill else thickness)

    # TODO arc
    def arc(self, start_pt, stop_pt, start_angle=0, stop_angle=90, thickness=0):
        pass

    def polygon(self, vertices, thickness=0, fill=True):
        colour = self._regularizeColour(colour)
        cv.polylines(self.window.img, [np.array(vertices).reshape((-1, 1, 2))], fill, colour, thickness)

    def gradient(self, x, y, w, h, color1=(0, 0, 0), color2=(0, 0, 0)):
        c1 = np.full((1, h, 3), color1, dtype=np.uint8)
        c2 = np.full((1, h, 3), color2, dtype=np.uint8)
        base = np.concatenate([c1, c2], axis=0)
        grad = cv.resize(base, (w, h), cv.INTER_LINEAR)
        return grad



    
    