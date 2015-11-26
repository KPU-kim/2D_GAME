import random
import json
import os

from pico2d import *

import game_framework
import flight_title_state
from background import *

import selback_state


name = "MainState"

dragon = None
#background = None

enemy_yellow = None
font = None
background = None

#Missiles_1 =list()
background_y = 0
background_y_2 = 700


#class Baekground:
#    def __init__(self):
#        self.image = load_image('C:\\2D\\flight_game_fraemwork\\dragon flight\\dragon flight\\background\\sea.png')
#        self.image2 = load_image('C:\\2D\\flight_game_fraemwork\\dragon flight\\dragon flight\\background\\sea.png')

#    def update(self):
#        global background_y, background_y_2
#        background_y -=5
#        background_y_2 -=5
#        if(background_y_2 == 0):
#            background_y = 0
#            background_y_2 = 700
#    def draw(self):
#        global background_y, background_y_2
#        self.image.draw_to_origin(0, background_y, 400,700)
#    def draw2(self):
#        global background_y, background_y_2
#        self.image.draw_to_origin(0, background_y_2, 400,700)

class Enemy_white:
    image = None
    #def __init__(self):
      #  self.image = load_image('C:\\2D\\flight_game_fraemwork\\enemy_whitedragon_animation3.png')

    def update(self):
        self.frame = (self.frame + 1) % 11
        self.y -= 5

    def __init__(self):
        self.x, self.y = random.randint(60,400-60) , random.randint(400,600)
        self.frame = random.randint(0, 10)
        self.run_frames = 0


        if Enemy_white.image == None:
            Enemy_white.image = load_image('C:\\2D\\flight_game_fraemwork\\Image\\enemy\\enemy_whitedragon_animation3.png')

    def draw(self):
        self.image.clip_draw(self.frame * 120, 0, 120, 120, self.x, self.y)

    def get_bb(self):
         return self.x-50, self.y-50, self.x+50, self.y+50

    def draw_bb(self):
         draw_rectangle(*self.get_bb())

class Enemy_yellow:
    PIXEL_PER_METER = (10.0 / 0.3)
    RUN_SPEED_KMPH = 20.0
    RUN_SPEED_MPM = (RUN_SPEED_KMPH * 1000.0 / 60.0)
    RUN_SPEED_MPS = (RUN_SPEED_MPM / 60.0)
    RUN_SPEED_PPS = (RUN_SPEED_MPS * PIXEL_PER_METER)

    TIME_PER_ACTION = 0.5
    ACTION_PER_TIME = 1.0 / TIME_PER_ACTION
    FRAMES_PER_ACTION = 8

    image = None
    #def __init__(self):
      #  self.image = load_image('C:\\2D\\flight_game_fraemwork\\enemy_whitedragon_animation3.png')

    def update(self,frame_time):
        distance = Enemy_yellow.RUN_SPEED_PPS * frame_time
        self.frame = (self.frame + 1) % 11

        self.y -= distance
        #self.y -= 5

    def __init__(self):
        self.x, self.y = random.randint(60,400-60) , 800
        self.frame = random.randint(0, 10)
        self.run_frames = 0


        if Enemy_yellow.image == None:
            Enemy_yellow.image = load_image('C:\\2D\\flight_game_fraemwork\\Image\\enemy\\enemy_yellow_dragon_animation.png')
    def draw(self):
        self.image.clip_draw(self.frame * 120, 0, 120, 120, self.x, self.y)

    def get_bb(self):
         return self.x-50, self.y-50, self.x+50, self.y+50

    def draw_bb(self):
         draw_rectangle(*self.get_bb())

class Ice_cragon:
    image = None
    #def __init__(self):
      #  self.image = load_image('C:\\2D\\flight_game_fraemwork\\enemy_whitedragon_animation3.png')

    def update(self):
        self.frame = (self.frame + 1) % 4
                #self.y -= 5

    def __init__(self):
        self.x, self.y = 200 , 450
        self.frame = random.randint(0, 10)
        self.run_frames = 0


        if Ice_cragon.image == None:
            Ice_cragon.image = load_image('C:\\2D\\flight_game_fraemwork\\Image\\enemy\\enemy_ice_cragon_animation.png')
    def draw(self):
        self.image.clip_draw(self.frame * 200, 0, 200, 200, self.x, self.y)

    def get_bb(self):
         return self.x-80, self.y-80, self.x+80, self.y+80

    def draw_bb(self):
         draw_rectangle(*self.get_bb())

class Enemy_pink:
    image = None
    #def __init__(self):
      #  self.image = load_image('C:\\2D\\flight_game_fraemwork\\enemy_whitedragon_animation3.png')

    def update(self):
        self.frame = (self.frame + 1) % 7
        self.y -= 5

    def __init__(self):
        self.x, self.y = random.randint(60,400-60) , 700
        self.frame = random.randint(0, 10)
        self.run_frames = 0


        if Enemy_pink.image == None:
            Enemy_pink.image = load_image('C:\\2D\\flight_game_fraemwork\\Image\\enemy\\enemy_pink_dragon_animation.png')
    def draw(self):
        self.image.clip_draw(self.frame * 120, 0, 120, 120, self.x, self.y)

    def get_bb(self):
         return self.x-50, self.y-50, self.x+50, self.y+50

    def draw_bb(self):
         draw_rectangle(*self.get_bb())

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
    LEFT_RUN, RIGHT_RUN, LEFT_STAND, RIGHT_STAND, UP_RUN, DOWN_RUN, UP_STAND, DOWN_STAND = 0, 1, 2, 3, 4, 5, 6, 7

    def handel_event(self, event):
        if (event.type, event.key) == (SDL_KEYDOWN, SDLK_SPACE):
            if self.state in (self.RIGHT_RUN, self.LEFT_RUN, self.LEFT_STAND, self.RIGHT_STAND, self.UP_RUN, self.DOWN_RUN, self.UP_STAND, self.DOWN_STAND):
                dragon.shooting()
        if(event.type, event.key) == (SDL_KEYDOWN, SDLK_LEFT):
            if self.state in (self.LEFT_RUN,self.RIGHT_RUN, self.LEFT_STAND, self.RIGHT_STAND, self.UP_STAND, self.DOWN_STAND):
                self.state = self.LEFT_RUN
        elif(event.type, event.key) == (SDL_KEYDOWN, SDLK_RIGHT):
            if self.state in (self.LEFT_RUN,self.RIGHT_RUN, self.LEFT_STAND, self.RIGHT_STAND, self.UP_STAND, self.DOWN_STAND):
                self.state = self.RIGHT_RUN
        elif(event.type, event.key) == (SDL_KEYDOWN, SDLK_UP):
            if self.state in (self.LEFT_RUN,self.RIGHT_RUN, self.LEFT_STAND, self.RIGHT_STAND, self.UP_STAND, self.DOWN_STAND):
                self.state = self.UP_RUN
        elif(event.type, event.key) == (SDL_KEYDOWN, SDLK_DOWN):
            if self.state in (self.LEFT_RUN,self.RIGHT_RUN, self.LEFT_STAND, self.RIGHT_STAND, self.UP_STAND, self.DOWN_STAND):
                self.state = self.DOWN_RUN
        elif(event.type, event.key) == (SDL_KEYUP, SDLK_LEFT):
            if self.state in (self.LEFT_RUN, self.RIGHT_RUN):
                self.state = self.LEFT_STAND
        elif(event.type, event.key) == (SDL_KEYUP, SDLK_RIGHT):
            if self.state in (self.RIGHT_RUN, self.LEFT_RUN):
                self.state = self.RIGHT_STAND
        elif(event.type, event.key) == (SDL_KEYUP, SDLK_UP):
            if self.state in (self.UP_RUN,):
                self.state = self.UP_STAND
        elif(event.type, event.key) == (SDL_KEYUP, SDLK_DOWN):
            if self.state in (self.DOWN_RUN,):
                self.state = self.DOWN_STAND

    def update(self,frame_time):
        distance = Kirby.RUN_SPEED_PPS * frame_time
        self.frame = (self.frame + 1) % 11
        if self.state == self.RIGHT_RUN:
            self.x = min(400,self.x + distance)
        elif self.state == self.LEFT_RUN:
            self.x = max(0, self.x - distance )
        elif self.state == self.LEFT_STAND:
            pass
        elif self.state == self.RIGHT_STAND:
            pass
        elif self.state == self.UP_RUN:
            self.y = min(700,self.y + distance)
        elif self.state == self.DOWN_RUN:
            self.y = max(0,self.y - distance)
        pass

    def __init__(self):
        self.x, self.y = 200 , 60
        self.frame = random.randint(0, 10)
        self.run_frames = 0

        self.state = self.LEFT_STAND
        if Kirby.image == None:
            Kirby.image = load_image('dragon_animation2.png')

    def draw(self):
        self.image.clip_draw(self.frame * 173, 0, 173, 126, self.x, self.y)

    def shooting(self):
        newmissile = Missile(self.x, self.y)
        Missiles_1.append(newmissile)

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
        if dragon.state in (dragon.RIGHT_RUN, dragon.LEFT_RUN, dragon.LEFT_STAND, dragon.RIGHT_STAND, dragon.UP_RUN, dragon.DOWN_RUN, dragon.UP_STAND, dragon.DOWN_STAND):
            self.image.draw(self.x, self.y)

    def get_bb(self):
         return self.x-50, self.y-45, self.x+50, self.y+45


    def draw_bb(self):
        draw_rectangle(*self.get_bb())

def enter():
    global dragon, background , enemy_white , enemy_yellow, enemy_pink, Missiles_1, ice_cragon
    global current_time , first_time
    dragon = Kirby()
    background = Background()
    enemy_white = [Enemy_white() for i in range(0)]
    enemy_yellow = [Enemy_yellow() for i in range(0)]
    enemy_pink = [Enemy_pink() for i in range(0)]
    ice_cragon = [Ice_cragon( )for i in range(1)]
    Missiles_1 = [Missile() for i in range(0)]
    current_time = get_time()
    first_time = get_time()


def exit():
    global dragon, background , enemy_white , enemy_yellow, enemy_pink, Missiles_1, ice_cragon
    del(dragon)
    del(background)
    del(enemy_white)
    del(enemy_yellow)
    del(enemy_pink)
    del(ice_cragon)
    del(Missiles_1)

def pause():
    pass


def resume():
    pass


def handle_events():
    global dragon,enemy_white , enemy_yellow, enemy_pink
    events = get_events()
    for event in events:
        if event.type == SDL_QUIT:
            game_framework.quit()
        elif event.type == SDL_KEYDOWN and event.key == SDLK_ESCAPE:
            game_framework.change_state(selback_state)
        elif event.type == SDL_KEYDOWN and event.key == SDLK_1:
            enemy_white.append(Enemy_white())
            enemy_yellow.append(Enemy_yellow())
            enemy_pink.append(Enemy_pink())
        else:
            dragon.handel_event(event)
            pass


def get_frame_time():
    global current_time
    frame_time = get_time() - current_time
    current_time += frame_time
    return frame_time

def make_monster(time):
    global first_time, enemy_yellow
    if abs(time - get_time()) > 2:
        first_time = get_time()
        enemy_yellow.append(Enemy_yellow())




def update():

    frame_time = get_frame_time()
    make_monster(first_time)
    print(abs(first_time - get_time()))
    dragon.update(frame_time)
    for white in enemy_white :
        white.update()
    # 움직이는 부분
    for yellow in enemy_yellow :
        yellow.update(frame_time)

    for pink in enemy_pink :
        pink.update()
    for ice in ice_cragon :
        ice.update()
    for Missile_1 in Missiles_1:
        Missile_1.update(frame_time)
        if Missile_1.y > 700:
            Missiles_1.remove(Missile_1)
        #if  collide(Missile_1,enemy_yellow)

    #충돌부분
    for Missile_1 in Missiles_1:
        for pink in enemy_pink :
            if collide(Missile_1 , pink):
                Missiles_1.remove(Missile_1)
                enemy_pink.remove(pink)
                break
    for Missile_1 in Missiles_1:
        for yellow in enemy_yellow :
            if collide(Missile_1 , yellow):
                Missiles_1.remove(Missile_1)
                enemy_yellow.remove(yellow)
                break
    for Missile_1 in Missiles_1:
        for white in enemy_white :
            if collide(Missile_1 , white):
                Missiles_1.remove(Missile_1)
                enemy_white.remove(white)
                break
    for Missile_1 in Missiles_1:
        for ice in ice_cragon :
            if collide(Missile_1 , ice):
                Missiles_1.remove(Missile_1)
                ice_cragon.remove(ice)
                break
    background.update()

def draw():
    clear_canvas()
    background.draw()
    background.draw2()
    dragon.draw()
    dragon.draw_bb()
    for white in enemy_white :
        white.draw()
        white.draw_bb()
    for yellow in enemy_yellow :
        yellow.draw()
        yellow.draw_bb()
    for pink in enemy_pink :
        pink.draw()
        pink.draw_bb()
    for ice in ice_cragon :
        ice.draw()
        ice.draw_bb()


    for Missile_1 in Missiles_1:
        Missile_1.draw()
        Missile_1.draw_bb()
    update_canvas()
    delay(0.04)






def collide(a, b):
    left_a, bottom_a, right_a, top_a = a.get_bb()
    left_b, bottom_b, right_b, top_b = b.get_bb()


    if left_a > right_b : return False
    if right_a < left_b : return False
    if top_a < bottom_b : return False
    if bottom_a > top_b : return False

    return True
