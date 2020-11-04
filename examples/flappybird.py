import os
import sys
import traceback
import clr
from random import randint
from GUI_elements import *
from utils.constants import FRAME_RATE, EventType
from utils.color import Color
import math

win = Window(1920, 1080)
draw = Drawer()

av_time = 0
c = 0


def main(dt: int):
    print(dt)


win.loop(main)

win.close()


class Tooltip():
    def __init__(self, text, flip=False, size=(300, 30), textHt=None,
                 textCol=clr.black, col=clr.white, outline=False):
        if textHt == None:
            textHt = int(2 * size[1]/3)
        self.surf = pg.Surface(size)
        self.size = size
        self.rect = self.surf.get_rect()
        self.text = text
        self.textHt = textHt
        self.textCol = textCol
        self.col = col
        self.outline = outline
        self.flip = flip

    def show(self, screen, thickness=4):
        textSurf = pg.font.SysFont(pg.font.get_default_font(
        ), self.textHt).render(self.text, True, self.textCol)
        textRect = textSurf.get_rect()
        textRect.center = self.rect.center
        self.surf.fill(self.col)
        if self.outline:
            pg.draw.line(self.surf, self.textCol, (0, 0),
                         (self.size[0], 0), thickness)
            pg.draw.line(self.surf, self.textCol, (
                self.size[0]-thickness//2, self.size[1]-thickness//2), (self.size[0], 0), thickness)
            pg.draw.line(self.surf, self.textCol, (
                self.size[0]-thickness//2, self.size[1]-thickness//2), (0, self.size[1]), thickness)
            pg.draw.line(self.surf, self.textCol,
                         (0, self.size[1]), (0, 0), thickness)
        self.surf.blit(textSurf, textRect.topleft)
        if self.flip:
            pos = pg.mouse.get_pos()[
                0] - self.size[0], pg.mouse.get_pos()[1] - self.size[1]
        else:
            pos = pg.mouse.get_pos()
        screen.blit(self.surf, pos)


'''---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------'''


def Quit(screen):
    fade(screen, True, 0.5)
    pg.quit()
    exit()


def text(screen, x, y, size, text, colour=clr.white, center=None):
    textSurf = pg.font.SysFont(
        pg.font.get_default_font(), size).render(text, True, colour)
    if center != None:
        textRect = textSurf.get_rect()
        textRect.center = center
        x, y = textRect.topleft
    screen.blit(textSurf, (x, y))


def lose(screen, screenCenter, score, txt='Crashed!'):
    surf = pg.Surface((400, 200))
    surf.fill(clr.light_light_gray)
    surfRect = surf.get_rect()
    surfRect.center = screenCenter
    text(surf, 0, 0, 30, ("Your Score is: "+str(score)), clr.black, (200, 30))
    text(surf, 0, 0, 30, txt, clr.black, (200, 70))
    new = Button(30, 125, 140, 50, 'new game', textHeight=30, outline=True)
    home = Button(230, 125, 140, 50, 'home', textHeight=30, outline=True)
    new.show(surf, surfRect.topleft)
    home.show(surf, surfRect.topleft)
    pg.draw.line(surf, clr.black, (0, 0), (0, 200))
    pg.draw.line(surf, clr.black, (0, 199), (399, 199))
    pg.draw.line(surf, clr.black, (399, 199), (399, 0))
    pg.draw.line(surf, clr.black, (400, 0), (0, 0))

    screen.blit(surf, surfRect.topleft)
    return new, home, surfRect.topleft


black = pg.Color("BLACK")
blue = pg.Color("BLUE")

dark_dark_gray = pg.Color(33, 33, 33)
dark_gray = pg.Color(67, 67, 67)
dark_green = pg.Color(30, 180, 10)

gray = pg.Color(125, 125, 125)
green = pg.Color(0, 255, 0)
green_screen = pg.Color(0, 200, 0)

light_gray = pg.Color(200, 200, 200)
light_green = pg.Color(150, 255, 150)
light_light_gray = pg.Color(240, 240, 240)
light_orange = pg.Color(255, 178, 102)
light_red = pg.Color(255, 102, 102)

orange = pg.Color(255, 128, 0)

purple = pg.Color(170, 0, 210)

red = pg.Color(255, 0, 0)

select_green = pg.Color("LIGHTGREEN")
sky = pg.Color("SKYBLUE")
white = pg.Color("WHITE")

yellow = pg.Color("YELLOW")import pygame as pg
pg.init()

SPAZ_MODE = False

if SPAZ_MODE:
    A = 0.05
    UP = -25
else:
    A = 2
    UP = -50

################################################################################################################################################################################################


class Pipe():
    def __init__(self, x, y, flip, ht, wd=100, speed=3, topHt=40, botWd=None,
                 col=clr.green, high_col=clr.light_green, shad_col=clr.dark_green):
        self.surf = pg.Surface((wd, ht))
        self.size = [wd, ht]
        self.coord = [x, y]
        self.topHt = topHt
        self.top_rect = pg.Rect(0, 0, wd, topHt)
        if botWd == None:
            botWd = 4*wd//5
        self.botWd = botWd
        self.bot_rect = pg.Rect((wd - botWd)//2, topHt, botWd, (ht - topHt))
        self.colScheme = [high_col, col, shad_col]
        # True for top and False for bottom
        self.flip = flip
        self.speed = speed

    def show(self, screen, screenHt, i, pipe_list, block):
        if self.coord[0] < (-self.size[0]):
            if self.flip:
                self.size[1] = randint(0, block-1) * screenHt//block
            else:
                self.size[1] = screenHt - \
                    (pipe_list[i % (len(pipe_list)//2)
                               ].size[1] + screenHt//block)
            self.coord[0] = 1400

        self.surf.fill(clr.sky)

        pg.draw.rect(self.surf, self.colScheme[1], self.top_rect)
        pg.draw.rect(
            self.surf, self.colScheme[0], (self.top_rect.topleft, (self.size[0]//5, self.topHt)))
        pg.draw.rect(self.surf, self.colScheme[2], ((
            4 * self.size[0]//5, 0), (self.size[0]//5, self.topHt)))
        pg.draw.rect(self.surf, self.colScheme[1], self.bot_rect)
        pg.draw.rect(
            self.surf, self.colScheme[0], (self.bot_rect.topleft, (self.botWd//5, self.bot_rect[3])))
        pg.draw.rect(self.surf, self.colScheme[2], ((
            (4 * self.botWd//5) + self.bot_rect.left, self.bot_rect.top), (self.botWd//5, self.bot_rect[3])))

        pg.draw.line(self.surf, clr.black, self.top_rect.topleft,
                     self.top_rect.topright, 5)
        pg.draw.line(self.surf, clr.black,
                     self.top_rect.bottomright, self.top_rect.topright, 5)
        pg.draw.line(self.surf, clr.black, self.top_rect.bottomleft,
                     self.top_rect.bottomright, 5)
        pg.draw.line(self.surf, clr.black,
                     self.top_rect.bottomleft, self.top_rect.topleft, 5)

        pg.draw.line(self.surf, clr.black, self.bot_rect.topleft,
                     self.bot_rect.topright, 5)
        pg.draw.line(self.surf, clr.black,
                     self.bot_rect.bottomright, self.bot_rect.topright, 5)
        pg.draw.line(self.surf, clr.black,
                     self.bot_rect.bottomleft, self.bot_rect.topleft, 5)

        self.surf.set_colorkey(clr.sky)

        self.surf = pg.transform.flip(self.surf, False, self.flip)

        screen.blit(self.surf, self.coord)

    def move(self):
        self.coord[0] -= self.speed

    def crash(self, bird):
        surfRect = self.surf.get_rect()
        surfRect[0] = self.coord[0]
        surfRect[1] = self.coord[1]
        return (surfRect.colliderect(bird.rect))


class Bird():
    def __init__(self, x, y, pic_up, pic_down):
        self.initpos = (x, y)
        self.pos = [x, y]
        self.pic_up = pic_up
        self.pic_down = pic_down
        self.speed = 0
        self.rect = (self.pos, (40, 40))
        self.v = 0

    def show(self, screen):
        if self.v > 0:
            screen.blit(self.pic_down, self.pos)
        else:
            screen.blit(self.pic_up, self.pos)

    def is_dead(self, screenHt):
        return self.pos[1] > screenHt

    def move(self, t, a=A):
        if SPAZ_MODE:
            self.v += a * t/2
        else:
            self.v += a
        if self.v > 15:
            self.v = 15
        elif self.v < -25:
            self.v = -25

        self.pos[1] += self.v


################################################################################################################################################################################################
def cloud(screen, x, y, r=20):
    pg.draw.circle(screen, clr.white, (x, (y - r)), r)
    pg.draw.circle(screen, clr.white, (x + (r + 8), y), r)
    pg.draw.circle(screen, clr.white, ((x + int(2.5*r)), (y + r)), r)
    pg.draw.circle(screen, clr.white, ((x - r), (y + r//2)), r)
    pg.draw.circle(screen, clr.white, ((x+5), (y+5)), r)
    pg.draw.circle(screen, clr.white, ((x+r), (y+r)), r)
    pg.draw.rect(screen, clr.sky, (x-3*r, y+r, 8*r, r))


def day_sky(screen):
    screen.fill(clr.sky)
    cloud(screen, 220, 150)
    cloud(screen, 947, 324)
    cloud(screen, 670, 500)


def mainLoop(screencol, textcol, prev_screen=None, rect_pos=None):
    pg.display.set_caption('Flappy Bird')
    start = True
    screenWd, screenHt = 1120, 630
    screenCenter = (screenWd//2, screenHt//2)
    screen = pg.display.set_mode((screenWd, screenHt))
    clock = pg.time.Clock()
    FPS = 25
    alive = True
    play = False
    score = 0
    count = 0
    temp = 0
    block = 3
    paused = False
    center = (screenWd // 2, 100)
    star_pos = [(randint(0, screenWd), randint(0, screenHt))
                for i in range(10)]

    randintlist = [(randint(0, block-1) * screenHt//block) for i in range(5)]
    randintlist[0] = block//2 * screenHt//block

    if not SPAZ_MODE:
        pic_up = pg.image.load(os.path.join(
            os.getcwd(), "python_pictures", "bird_up.png"))
        pic_down = pg.image.load(os.path.join(
            os.getcwd(), "python_pictures", "bird_down.png"))
    else:
        pic_up = pg.image.load(os.path.join(
            os.getcwd(), "python_pictures", "bird_up_SPAZ.png"))
        pic_down = pg.image.load(os.path.join(
            os.getcwd(), "python_pictures", "bird_down_SPAZ.png"))

    top_pipe1 = Pipe(500, 0, True, randintlist[0])
    bot_pipe1 = Pipe(500, (randintlist[0] + screenHt//block),
                     False, (screenHt - (randintlist[0] + screenHt//block)))
    top_pipe2 = Pipe(800, 0, True, randintlist[1])
    bot_pipe2 = Pipe(800, (randintlist[1] + screenHt//block),
                     False, (screenHt - (randintlist[1] + screenHt//block)))
    top_pipe3 = Pipe(1100, 0, True, randintlist[2])
    bot_pipe3 = Pipe(1100, (randintlist[2] + screenHt//block),
                     False, (screenHt - (randintlist[2] + screenHt//block)))
    top_pipe4 = Pipe(1400, 0, True, randintlist[3])
    bot_pipe4 = Pipe(1400, (randintlist[3] + screenHt//block),
                     False, (screenHt - (randintlist[3] + screenHt//block)))
    top_pipe5 = Pipe(1700, 0, True, randintlist[4])
    bot_pipe5 = Pipe(1700, (randintlist[4] + screenHt//block),
                     False, (screenHt - (randintlist[4] + screenHt//block)))

    butt_mode = Button(1075, 15, 20, 20)

    bird = Bird(50, 200, pic_up, pic_down)

    pipe_list = [top_pipe1, top_pipe2, top_pipe3, top_pipe4, top_pipe5,
                 bot_pipe1, bot_pipe2, bot_pipe3, bot_pipe4, bot_pipe5]

    while True:
        for event in pg.event.get():
            if event.type == pg.QUIT:
                Quit(screen)
            if event.type == pg.KEYDOWN:
                if event.key == pg.K_ESCAPE:
                    fade(screen, True, col=screencol)
                    return False, screencol, textcol
                if event.key == pg.K_SPACE and alive:
                    if paused:
                        paused = False
                    elif play == False:
                        play = True
                    else:
                        bird.move(count, UP)
                elif event.key == pg.K_p and alive:
                    if paused:
                        paused = False
                    else:
                        paused = True
                        text(screen, 0, 0, 50, "Paused", textcol, center)
                elif event.key == pg.K_n:
                    return True, screencol, textcol
                elif event.key == pg.K_h:
                    if play:
                        paused = True
                    fade(screen, True, col=screencol)
                    help_screen(FLAPPY_BIRD, screencol, textcol)
                elif event.key == pg.K_m:
                    if screencol == clr.black:
                        screencol = clr.white
                        textcol = clr.black
                    else:
                        screencol = clr.black
                        textcol = clr.white

        if butt_mode.get_click():
            if screencol == clr.black:
                screencol = clr.white
                textcol = clr.black
            else:
                screencol = clr.black
                textcol = clr.white

        if screencol == clr.black:
            screen.fill(screencol)
            for star in star_pos:
                pg.draw.circle(screen, clr.white, star, 3)
        else:
            screen.fill(clr.sky)
            day_sky(screen)

        for i in range(len(pipe_list)):
            if alive and paused == False and play:
                pipe_list[i].move()
            pipe_list[i].show(screen, screenHt, i, pipe_list, block)
            if pipe_list[i].crash(bird):
                alive = False
                new, home, origin = lose(screen, screenCenter, score)

        if paused:
            text(screen, 0, 0, 50, "Paused", textcol, center)
        else:
            if alive and play:
                if bird.is_dead(screenHt):
                    alive = False
                bird.move(count)

        if screencol == clr.black:
            sun(screen)
        else:
            moon(screen)

        if alive == False:
            new, home, origin = lose(screen, screenCenter, score)
            if home.get_click(origin):
                fade(screen, True, col=screencol)
                return False, screencol, textcol
            if new.get_click(origin):
                return True, screencol, textcol

        if paused == False and play:
            count += 1
        if count % 25 == 0 and alive and paused == False and play:
            score += 1

        text(screen, screenWd - 70, 5, 30, str(score), textcol)

        bird.show(screen)

        if play == False:
            text(screen, 0, 0, 30, "Press space to start", textcol, (560, 250))

        if start and prev_screen != None:
            expand(screen, screen.copy(), [
                   rect_pos[0], rect_pos[1]+90, 200, 113], prev_screen)
            start = False
        else:
            pg.display.update()
        clock.tick(FPS)

# try:
##    restart = mainLoop()
# while restart:
##        restart = mainLoop()
# except:
# traceback.print_exc()
# finally:
# pg.quit
