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
                #self.y -= 5

    def __init__(self):
        self.x, self.y = 200 , 600
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
    image = None
    #def __init__(self):
      #  self.image = load_image('C:\\2D\\flight_game_fraemwork\\enemy_whitedragon_animation3.png')

    def update(self):
        self.frame = (self.frame + 1) % 11
                #self.y -= 5

    def __init__(self):
        self.x, self.y = 320 , 600
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
                #self.y -= 5

    def __init__(self):
        self.x, self.y = 80 , 600
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

    def update(self):
        self.frame = (self.frame + 1) % 11
        if self.state == self.RIGHT_RUN:
            self.x = min(400,self.x + 5)
        elif self.state == self.LEFT_RUN:
            self.x = max(0, self.x - 5 )
        elif self.state == self.LEFT_STAND:
            pass
        elif self.state == self.RIGHT_STAND:
            pass
        elif self.state == self.UP_RUN:
            self.y = min(700,self.y + 5)
        elif self.state == self.DOWN_RUN:
            self.y = max(0,self.y - 5)
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
    global dragon
    def __init__(self, x, y):
        self.x, self.y = x, y
        self.image = load_image('C:\\2D\\flight_game_fraemwork\\dragon flight\\shoot1.png')

    def update(self):
        self.y += 5
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
    dragon = Kirby()
    background = Background()
    enemy_white = Enemy_white()
    enemy_yellow = Enemy_yellow()
    enemy_pink = Enemy_pink()
    ice_cragon = Ice_cragon()
    Missiles_1 = list()



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
    global dragon
    events = get_events()
    for event in events:
        if event.type == SDL_QUIT:
            game_framework.quit()
        elif event.type == SDL_KEYDOWN and event.key == SDLK_ESCAPE:

            game_framework.change_state(selback_state)
        else:
            dragon.handel_event(event)
            pass




def update():
    dragon.update()
    enemy_white.update()
    #global missile
    enemy_yellow.update()
    enemy_pink.update()
    ice_cragon.update()
    for Missile_1 in Missiles_1:
        Missile_1.update()

    for Missile_1 in Missiles_1:
        if collide(dragon , enemy_white):
            print("collision")
    background.update()

def draw():
    clear_canvas()
    background.draw()
    background.draw2()
    dragon.draw()
    dragon.draw_bb()
    enemy_white.draw()
    enemy_white.draw_bb()
    enemy_yellow.draw()
    enemy_yellow.draw_bb()
    enemy_pink.draw()
    enemy_pink.draw_bb()
    ice_cragon.draw()
    ice_cragon.draw_bb()


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
    if top_a > bottom_b : return False
    if bottom_a < top_b : return False

    return True
