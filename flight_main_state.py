import random
import json
import os

from pico2d import *

import game_framework
import flight_title_state

global running


name = "MainState"

boy = None
background = None
enemy_white = None
font = None



class Baekground:
    def __init__(self):
        self.image = load_image('C:\\2D\\flight_game_fraemwork\\dragon flight\\dragon flight\\background\\sea.png')

    def draw(self):
        self.image.draw_to_origin(0, 0, 400,700)


class Enemy_white:
    image = None
    def __init__(self):
        self.image = load_image('C:\\2D\\flight_game_fraemwork\\enemy_whitedragon_animation3.png')

    def update(self):
        self.frame = (self.frame + 1) % 11
                #self.y -= 5

    def __init__(self):
        self.x, self.y = 200 , 600
        self.frame = random.randint(0, 10)
        self.run_frames = 0


        if Enemy_white.image == None:
            Enemy_white.image = load_image('C:\\2D\\flight_game_fraemwork\\enemy_whitedragon_animation3.png')
    def draw(self):
        self.image.clip_draw(self.frame * 120, 0, 120, 120, self.x, self.y)

class Boy:
    image = None
    LEFT_RUN, RIGHT_RUN, LEFT_STAND, RIGHT_STAND = 0, 1, 2, 3

    def handel_event(self, event):
        if(event.type, event.key) == (SDL_KEYDOWN, SDLK_LEFT):
            if self.state in (self.LEFT_RUN,self.RIGHT_RUN, self.LEFT_STAND, self.RIGHT_STAND):
                self.state = self.LEFT_RUN
        elif(event.type, event.key) == (SDL_KEYDOWN, SDLK_RIGHT):
            if self.state in (self.LEFT_RUN,self.RIGHT_RUN, self.LEFT_STAND, self.RIGHT_STAND):
                self.state = self.RIGHT_RUN
        elif(event.type, event.key) == (SDL_KEYUP, SDLK_LEFT):
            if self.state in (self.LEFT_RUN, self.RIGHT_RUN):
                self.state = self.LEFT_STAND
        elif(event.type, event.key) == (SDL_KEYUP, SDLK_RIGHT):
            if self.state in (self.RIGHT_RUN, self.LEFT_RUN):
                self.state = self.RIGHT_STAND


    def update(self):
        self.frame = (self.frame + 1) % 11
        if self.state == self.RIGHT_RUN:
            self.x = min(400,self.x +5)
        elif self.state == self.LEFT_RUN:
            self.x = max(0, self.x-5 )
        elif self.state == self.LEFT_STAND:
            pass
        elif self.state == self.RIGHT_STAND:
            pass
        pass

    def __init__(self):
        self.x, self.y = 200 , 60
        self.frame = random.randint(0, 10)
        self.run_frames = 0

        self.state = self.LEFT_STAND
        if Boy.image == None:
            Boy.image = load_image('dragon_animation.png')

    def draw(self):
        self.image.clip_draw(self.frame * 173, 0, 173, 126, self.x, self.y)


def enter():
    global boy, background , enemy_white
    boy = Boy()
    background = Baekground()
    enemy_white = Enemy_white()

def exit():
    global boy, background , enemy_white
    del(boy)
    del(background)
    del(enemy_white)

def pause():
    pass


def resume():
    pass


def handle_events():
    global boy
    events = get_events()
    for event in events:
        if event.type == SDL_QUIT:
            game_framework.quit()
        elif event.type == SDL_KEYDOWN and event.key == SDLK_ESCAPE:

            game_framework.change_state(flight_title_state)
        else:
            boy.handel_event(event)
            pass







def update():
    boy.update()
    enemy_white.update()

def draw():
    clear_canvas()
    background.draw()
    boy.draw()
    enemy_white.draw()
    update_canvas()
    delay(0.02)






