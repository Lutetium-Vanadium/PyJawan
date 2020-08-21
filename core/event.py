from pynput import mouse, keyboard

class Event:
    pass

class KeydownEvent(Event):
    def __init__(self, key: keyboard.Key):
        self.key = key

    @property
    def char(self):
        try:
            return self.key.char
        except AttributeError:
            return None

class KeyupEvent(Event):
    def __init__(self, key: keyboard.Key):
        self.key = key

    @property
    def char(self):
        try:
            return self.key.char
        except AttributeError:
            return None

class MouseMoveEvent(Event):
    def __init__(self, mouseX: int, mouseY: int, prev_event):
        self.x = mouseX
        self.y = mouseY
        if prev_event == None:
            self.prev_x = prev_event.x
            self.prev_y = prev_event.y
        else:
            self.prev_x = None
            self.prev_y = None
    
    @property
    def dx(self):
        if self.prev_x != None:
            return self.x - self.prev_x
    
    @property
    def dy(self):
        if self.prev_y != None:
            return self.y - self.prev_y
    
    @property
    def distance(self):
        if self.prev_x != None and self.prev_y != None:
            return (self.x*self.x + self.y*self.y) ** 0.5

class MouseClickEvent(Event):
    def __init__(self, mouseX: int, mouseY: int, button: mouse.Button, pressed: bool):
        self.x = mouseX
        self.y = mouseY
        self.button = button
        self.pressed = pressed

# TODO see onscroll