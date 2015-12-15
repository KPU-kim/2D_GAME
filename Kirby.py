__author__ = 'Owner'
from pico2d import *

import random

dragon = None
Missiles_1 = None
class Kirby:
    PIXEL_PER_METER = (10.0 / 0.3)
    RUN_SPEED_KMPH = 20.0
    RUN_SPEED_MPM = (RUN_SPEED_KMPH * 1000.0 / 60.0)
    RUN_SPEED_MPS = (RUN_SPEED_MPM / 60.0)
    RUN_SPEED_PPS = (RUN_SPEED_MPS * PIXEL_PER_METER)

    TIME_PER_ACTION = 0.5
    ACTION_PER_TIME = 1.0 / TIME_PER_ACTION
    FRAMES_PER_ACTION = 8

    image = None
    LEFT_RUN, RIGHT_RUN, STAND, UP_RUN, DOWN_RUN = 0, 1, 2, 3, 4

    def handel_event(self, event):
        if (event.type, event.key) == (SDL_KEYDOWN, SDLK_SPACE):
            if self.state in (self.RIGHT_RUN, self.LEFT_RUN, self.DOWN_RUN, self.UP_RUN, self.STAND):
                self.shooting()
        if (event.type, event.key) == (SDL_KEYDOWN, SDLK_LEFT):
            if self.state in (self.STAND, self.RIGHT_RUN, self.UP_RUN, self.DOWN_RUN):
                self.state = self.LEFT_RUN
        elif (event.type, event.key) == (SDL_KEYDOWN, SDLK_RIGHT):
            if self.state in (self.STAND, self.LEFT_RUN, self.UP_RUN, self.DOWN_RUN):
                self.state = self.RIGHT_RUN
        elif (event.type, event.key) == (SDL_KEYDOWN, SDLK_UP):
            if self.state in (self.STAND, self.RIGHT_RUN, self.LEFT_RUN, self.DOWN_RUN):
                self.state = self.UP_RUN
        elif (event.type, event.key) == (SDL_KEYDOWN, SDLK_DOWN):
            if self.state in (self.STAND, self.RIGHT_RUN, self.LEFT_RUN, self.UP_RUN):
                self.state = self.DOWN_RUN
        elif (event.type, event.key) == (SDL_KEYUP, SDLK_LEFT):
            if self.state in (self.LEFT_RUN,):
                self.state = self.STAND
        elif (event.type, event.key) == (SDL_KEYUP, SDLK_RIGHT):
            if self.state in (self.RIGHT_RUN,):
                self.state = self.STAND
        elif (event.type, event.key) == (SDL_KEYUP, SDLK_UP):
            if self.state in (self.UP_RUN,):
                self.state = self.STAND
        elif (event.type, event.key) == (SDL_KEYUP, SDLK_DOWN):
            if self.state in (self.DOWN_RUN,):
                self.state = self.STAND

    def update(self,frame_time):
        distance = Kirby.RUN_SPEED_PPS * frame_time
        self.frame = (self.frame + 1) % 11
        if self.state == self.RIGHT_RUN:
            self.x = min(400,self.x + distance)
        elif self.state == self.LEFT_RUN:
            self.x = max(0, self.x - distance )
        elif self.state == self.UP_RUN:
            self.y = min(700,self.y + distance)
        elif self.state == self.DOWN_RUN:
            self.y = max(0,self.y - distance)
        pass

    def __init__(self):
        self.x, self.y = 200 , 60
        self.frame = random.randint(0, 10)
        self.run_frames = 0

        self.state = self.STAND
        self.Missiles_1 = list()
        if Kirby.image == None:
            Kirby.image = load_image('dragon_animation2.png')

    def draw(self):
        self.image.clip_draw(self.frame * 173, 0, 173, 126, self.x, self.y)

    def shooting(self):
        newmissile = Missile(self.x, self.y)
        self.Missiles_1.append(newmissile)

    def get_bb(self):
         return self.x-50, self.y-55, self.x+50, self.y+55


    def draw_bb(self):
        draw_rectangle(*self.get_bb())

class Missile:
    PIXEL_PER_METER = (10.0 / 0.3)
    RUN_SPEED_KMPH = 30.0
    RUN_SPEED_MPM = (RUN_SPEED_KMPH * 1000.0 / 60.0)
    RUN_SPEED_MPS = (RUN_SPEED_MPM / 60.0)
    RUN_SPEED_PPS = (RUN_SPEED_MPS * PIXEL_PER_METER)

    TIME_PER_ACTION = 0.5
    ACTION_PER_TIME = 1.0 / TIME_PER_ACTION
    FRAMES_PER_ACTION = 8

    global dragon
    def __init__(self, x, y):
        self.x, self.y = x, y
        self.image = load_image('C:\\2D\\flight_game_fraemwork\\dragon flight\\shoot1.png')

    def update(self,frame_time):
        distance = Missile.RUN_SPEED_PPS * frame_time
        self.y += distance
        #if(self.y > 700):
         #   self.y = 0
          #  del Missile_1

    def draw(self):
        if dragon.state in (dragon.RIGHT_RUN, dragon.LEFT_RUN, dragon.UP_RUN, dragon.DOWN_RUN, dragon.STAND):
            self.image.draw(self.x, self.y)

    def get_bb(self):
         return self.x-50, self.y-45, self.x+50, self.y+45


    def draw_bb(self):
        draw_rectangle(*self.get_bb())
