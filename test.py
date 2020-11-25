import cv2 as cv
import numpy as np
import time

from core import Window, Drawer

from utils import FRAME_RATE, EventType, Color
from ui import Button

win = Window(1920, 1080)
draw = Drawer()

av_time = 0
c = 0

button = Button(100, 20, 300, 79, bg_col=Color.RebeccaPurple,
                hov_bg_col=Color.Red, border_radius=10)

button.register(win)
button.on_click(print)

# draw.polygon(win, [[200, 390], [420, 104], [66, 88]], Color(
#     np.random.randint(0, 256**3-1)), thickness=1, fill=True)
# draw.text(win, "Hello, World!", 100, 200, 50,
#           color=Color(np.random.randint(0, 256**3-1)))
# draw.line(win, 0, 0, 50, 50,
#           color=Color(np.random.randint(0, 256**3-1)))
# draw.ellipse(win, 100, 200, 50, 100,
#              color=Color(np.random.randint(0, 256**3-1)), fill=True)
# draw.rect(win, 100, 100, 50, 100,
#           color=Color(np.random.randint(0, 256**3-1)))
# draw.gradient(win, 200, 300, 50, 60,
#               color1=Color(np.random.randint(0, 256**3-1)), color2=Color(np.random.randint(0, 256**3-1)))
# draw.curve(win, [[200, 390], [420, 104], [66, 88]], Color(
#     np.random.randint(0, 256**3-1)), thickness=1, fill=True)
# draw.image(win, "test.jpg", 70, 80)

# draw.circle(win, 100, 200, 50, color=Color(
#     np.random.randint(0, 256**3-1)), fill=True)
# draw.rect(win, 100, 200, 10, 10, color=Color.Red, fill=True)

while True:
    key = cv.waitKey(100) & 0xFF

    if key == 27:
        break

    t = time.time()

    button.draw(draw, win)

    if not win.render():
        break

    time.sleep(1./FRAME_RATE)
    av_time = (av_time*c + time.time()-t)/(c+1)

    # print(av_time)
    c += 1


win.close()
