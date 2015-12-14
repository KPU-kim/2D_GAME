import random
import json
import os

from pico2d import *

import game_framework
import flight_title_state
import gameover_state
from background import *

from Boss import *
from UI import *
import selback_state


name = "MainState"

dragon = None
enemy_yellow = None
font = None
background = None
ui = None

background_y = 0
background_y_2 = 700


class Kirby:
    PIXEL_PER_METER = (10.0 / 0.2)
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
                dragon.shooting()
        if (event.type, event.key) == (SDL_KEYDOWN, SDLK_v):
            if self.state in (self.RIGHT_RUN, self.LEFT_RUN, self.DOWN_RUN, self.UP_RUN, self.STAND):
                dragon.shooting_skill()
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
        if Kirby.image == None:
            Kirby.image = load_image('dragon_animation2.png')

    def draw(self):
        self.image.clip_draw(self.frame * 173, 0, 173, 126, self.x, self.y)

    def shooting(self):
        newmissile = Missile(self.x, self.y)
        Missiles_1.append(newmissile)

    def shooting_skill(self):
        newmissile2 = Skill_missile(self.x, self.y)
        Missiles_2.append(newmissile2)

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

    sound = None
    sound2 = None
    def __init__(self, x, y):
        self.x, self.y = x, y
        self.image = load_image('C:\\2D\\flight_game_fraemwork\\dragon flight\\shoot1.png')
        if Missile.sound == None:
             Missile.sound = load_wav('C:\\2D\\flight_game_fraemwork\\dragon flight\\dragon flight\\sound\\fire_explo.wav')
             Missile.sound.set_volume(20)
        if Missile.sound2 == None:
             Missile.sound2 = load_wav('C:\\2D\\flight_game_fraemwork\\dragon flight\\dragon flight\\sound\\dragon_death.wav')
             Missile.sound2.set_volume(30)

    def update(self,frame_time):
        distance = Missile.RUN_SPEED_PPS * frame_time
        self.y += distance


    def draw(self):
        if dragon.state in (dragon.RIGHT_RUN, dragon.LEFT_RUN, dragon.UP_RUN, dragon.DOWN_RUN, dragon.STAND):
            self.image.draw(self.x, self.y)

    def get_bb(self):
         return self.x-50, self.y-45, self.x+50, self.y+45


    def draw_bb(self):
        draw_rectangle(*self.get_bb())

class Skill_missile :
    PIXEL_PER_METER = (10.0 / 0.3)
    RUN_SPEED_KMPH = 30.0
    RUN_SPEED_MPM = (RUN_SPEED_KMPH * 1000.0 / 60.0)
    RUN_SPEED_MPS = (RUN_SPEED_MPM / 60.0)
    RUN_SPEED_PPS = (RUN_SPEED_MPS * PIXEL_PER_METER)

    TIME_PER_ACTION = 0.5
    ACTION_PER_TIME = 1.0 / TIME_PER_ACTION
    FRAMES_PER_ACTION = 8
    MOVE_PER_SEC = 500

    def __init__(self, x, y):
        self.x, self.y = x, y
        self.image = load_image('C:\\2D\\flight_game_fraemwork\\dragon flight\\skill-horz.png')


    def update(self,frame_time):
        distance = Skill_missile.RUN_SPEED_PPS * frame_time
        self.y += distance

#--------------------------------------------------#
    def draw(self):
        if dragon.state in (dragon.RIGHT_RUN, dragon.LEFT_RUN, dragon.UP_RUN, dragon.DOWN_RUN, dragon.STAND):
            self.image.draw(self.x, self.y)
#--------------------------------------------------#
    def get_bb(self):
        return self.x-240, self.y+47, self.x+240, self.y-47
#--------------------------------------------------#
    def draw_bb(self):
        draw_rectangle(*self.get_bb())
#--------------------------------------------------#


class Enemy_white:
    PIXEL_PER_METER = (10.0 / 0.3)
    RUN_SPEED_KMPH = 20.0
    RUN_SPEED_MPM = (RUN_SPEED_KMPH * 1000.0 / 60.0)
    RUN_SPEED_MPS = (RUN_SPEED_MPM / 60.0)
    RUN_SPEED_PPS = (RUN_SPEED_MPS * PIXEL_PER_METER)

    TIME_PER_ACTION = 0.5
    ACTION_PER_TIME = 1.0 / TIME_PER_ACTION
    FRAMES_PER_ACTION = 8
    SHOT_PER_SEC = 1
    image = None

    def update(self,frame_time):
        distance = Enemy_white.RUN_SPEED_PPS * frame_time
        self.missile_count += frame_time * self.SHOT_PER_SEC
        if self.missile_count > 2.5:
            self.missile_count = 0
            enemy_missile = Enemy_missile(self.x, self.y)
            Enemy_Missile_List.append(enemy_missile)
        self.frame = (self.frame + 1) % 11
        self.y -= distance

    def __init__(self):
        self.x, self.y = random.randint(60,400-60) , 800
        self.frame = random.randint(0, 10)
        self.run_frames = 0
        self.missile_count = 0


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

    SHOT_PER_SEC = 1
    image = None
    #def __init__(self):
      #  self.image = load_image('C:\\2D\\flight_game_fraemwork\\enemy_whitedragon_animation3.png')

    def update(self,frame_time):
        distance = Enemy_yellow.RUN_SPEED_PPS * frame_time
        self.missile_count += frame_time * self.SHOT_PER_SEC
        if self.missile_count > 2.5:
            self.missile_count = 0
            enemy_missile = Enemy_missile(self.x, self.y)
            Enemy_Missile_List.append(enemy_missile)
        self.frame = (self.frame + 1) % 11
        self.y -= distance

    def __init__(self):
        self.x, self.y = random.randint(60,400-60) , 900
        self.frame = random.randint(0, 10)
        self.run_frames = 0
        self.missile_count = 0


        if Enemy_yellow.image == None:
            Enemy_yellow.image = load_image('C:\\2D\\flight_game_fraemwork\\Image\\enemy\\enemy_yellow_dragon_animation.png')
    def draw(self):
        self.image.clip_draw(self.frame * 120, 0, 120, 120, self.x, self.y)

    def get_bb(self):
         return self.x-50, self.y-50, self.x+50, self.y+50

    def draw_bb(self):
         draw_rectangle(*self.get_bb())

class Enemy_pink:
    PIXEL_PER_METER = (10.0 / 0.3)
    RUN_SPEED_KMPH = 20.0
    RUN_SPEED_MPM = (RUN_SPEED_KMPH * 1000.0 / 60.0)
    RUN_SPEED_MPS = (RUN_SPEED_MPM / 60.0)
    RUN_SPEED_PPS = (RUN_SPEED_MPS * PIXEL_PER_METER)

    TIME_PER_ACTION = 0.5
    ACTION_PER_TIME = 1.0 / TIME_PER_ACTION
    FRAMES_PER_ACTION = 8
    MOVE_PER_SEC = 200
    SHOT_PER_SEC = 1
    image = None

    def update(self, frame_time):
        distance = Enemy_pink.RUN_SPEED_PPS * frame_time
        self.missile_count += frame_time * self.SHOT_PER_SEC
        if self.missile_count > 3:
            self.missile_count = 0
            enemy_missile = Enemy_missile(self.x, self.y)
            Enemy_Missile_List.append(enemy_missile)
        self.frame = (self.frame + 1) % 7
        self.y -= distance


    def __init__(self):
        self.x, self.y = random.randint(60,400-60) , 1200
        self.frame = random.randint(0, 10)
        self.run_frames = 0
        self.missile_count = 0


        if Enemy_pink.image == None:
            Enemy_pink.image = load_image('C:\\2D\\flight_game_fraemwork\\Image\\enemy\\enemy_pink_dragon_animation.png')
    def draw(self):
        self.image.clip_draw(self.frame * 120, 0, 120, 120, self.x, self.y)

    def get_bb(self):
         return self.x-50, self.y-50, self.x+50, self.y+50

    def draw_bb(self):
         draw_rectangle(*self.get_bb())


class Enemy_green:
    PIXEL_PER_METER = (10.0 / 0.3)
    RUN_SPEED_KMPH = 20.0
    RUN_SPEED_MPM = (RUN_SPEED_KMPH * 1000.0 / 60.0)
    RUN_SPEED_MPS = (RUN_SPEED_MPM / 60.0)
    RUN_SPEED_PPS = (RUN_SPEED_MPS * PIXEL_PER_METER)

    TIME_PER_ACTION = 0.5
    ACTION_PER_TIME = 1.0 / TIME_PER_ACTION
    FRAMES_PER_ACTION = 8
    MOVE_PER_SEC = 200
    SHOT_PER_SEC = 1
    image = None

    def update(self, frame_time):
        distance = Enemy_green.RUN_SPEED_PPS * frame_time
        self.missile_count += frame_time * self.SHOT_PER_SEC
        if self.missile_count > 2.5:
             self.missile_count = 0
             enemy_missile = Enemy_missile(self.x, self.y)
             Enemy_Missile_List.append(enemy_missile)
        self.frame = (self.frame + 1) % 7
        self.y -= distance


    def __init__(self):
        self.x, self.y = random.randint(60,400-60) , 5000
        self.frame = random.randint(0, 10)
        self.run_frames = 0
        self.missile_count = 0


        if Enemy_green.image == None:
            Enemy_green.image = load_image('C:\\2D\\flight_game_fraemwork\\Image\\enemy\\enemy_green_dragon_animation.png')
    def draw(self):
        self.image.clip_draw(self.frame * 120, 0, 120, 120, self.x, self.y)

    def get_bb(self):
         return self.x-50, self.y-50, self.x+50, self.y+50

    def draw_bb(self):
         draw_rectangle(*self.get_bb())

class Enemy_missile :
    PIXEL_PER_METER = (10.0 / 0.3)
    RUN_SPEED_KMPH = 40.0
    RUN_SPEED_MPM = (RUN_SPEED_KMPH * 1000.0 / 60.0)
    RUN_SPEED_MPS = (RUN_SPEED_MPM / 60.0)
    RUN_SPEED_PPS = (RUN_SPEED_MPS * PIXEL_PER_METER)

    TIME_PER_ACTION = 0.5
    ACTION_PER_TIME = 1.0 / TIME_PER_ACTION
    FRAMES_PER_ACTION = 8


    def __init__(self, x, y) :
        self.x, self.y = x, y
        self.image = load_image('C:\\2D\\flight_game_fraemwork\\dragon flight\\enemy_shoot.png')
#--------------------------------------------------#
    def update(self, frame_time) :
        distance = Enemy_missile.RUN_SPEED_PPS * frame_time

        self.y -= distance
#--------------------------------------------------#
    def draw(self) :
        self.image.draw(self.x, self.y)
#--------------------------------------------------#
    def draw_bb(self):
        draw_rectangle(*self.get_bb())
#--------------------------------------------------#
    def get_bb(self):
        return self.x-30, self.y-40, self.x+30, self.y+40

#===============================================================================#
class Score :
    font = None
    def __init__(self) :
        self.font = load_font("NanumPen.TTF", 30)
        self.score = 0.0
#--------------------------------------------------#
    def update(self, frame_time) :
        self.score += frame_time
#--------------------------------------------------#
    def draw(self) :
        self.font.draw(20, 680, " SCORE : %d "%(self.score), (255, 255, 255))
#--------------------------------------------------#
    def get_score(self, GET_SCORE) :
        self.score += GET_SCORE
#--------------------------------------------------#

class Ice_cragon: # 보스
    PIXEL_PER_METER = (10.0 / 0.3)
    RUN_SPEED_KMPH = 20.0
    RUN_SPEED_MPM = (RUN_SPEED_KMPH * 1000.0 / 60.0)
    RUN_SPEED_MPS = (RUN_SPEED_MPM / 60.0)
    RUN_SPEED_PPS = (RUN_SPEED_MPS * PIXEL_PER_METER)

    TIME_PER_ACTION = 0.5
    ACTION_PER_TIME = 1.0 / TIME_PER_ACTION
    FRAMES_PER_ACTION = 8
    LEFT_MOVE, RIGHT_MOVE = -1, 1
    image = None
    #def __init__(self):
      #  self.image = load_image('C:\\2D\\flight_game_fraemwork\\enemy_whitedragon_animation3.png')

    def update(self,frame_time):
        distance = Ice_cragon.RUN_SPEED_PPS * frame_time
        self.frame = (self.frame + 1) % 4

        self.y -= distance
        #self.x += 2 * self.direction

        if(self.y <= 620) :
            self.y = 620
            self.x += distance * self.direction
            if(self.x >= 340) :
                self.direction = self.LEFT_MOVE
            elif(self.x <=60):
                self.direction = self.RIGHT_MOVE
    def __init__(self):
        self.x, self.y = 200 , 3000
        self.frame = random.randint(0, 10)
        self.run_frames = 0
        self.LIFE = True
        self.hp = 1500
        self.direction = self.LEFT_MOVE

        if Ice_cragon.image == None:
            Ice_cragon.image = load_image('C:\\2D\\flight_game_fraemwork\\Image\\enemy\\enemy_ice_cragon_animation.png')
    def draw(self):
        self.image.clip_draw(self.frame * 200, 0, 200, 200, self.x, self.y)

    def get_bb(self):
         return self.x-80, self.y-80, self.x+80, self.y+80

    def draw_bb(self):
         draw_rectangle(*self.get_bb())

    def get_hp(self, GET_HP):
        self.hp -= GET_HP
        if(self.hp <= 0) :
            self.LIFE = False
            return self.LIFE
        else :
            return self.LIFE

def enter():
    global dragon, background , enemy_white , enemy_yellow, enemy_pink, enemy_green, Missiles_1, Missiles_2, ice_cragon, Enemy_Missile_List
    global current_time , first_time , ui , score
    dragon = Kirby()
    score = Score()
    background = Background()
    enemy_white = [Enemy_white() for i in range(0)]
    enemy_yellow = [Enemy_yellow() for i in range(0)]
    enemy_pink = [Enemy_pink() for i in range(0)]
    enemy_green = [Enemy_green() for i in range(0)]
    ice_cragon = [Ice_cragon( )for i in range(1)]
    Missiles_1 = [Missile() for i in range(0)]
    Missiles_2 = [Skill_missile() for i in range(0)]
    Enemy_Missile_List = [Enemy_missile() for i in range(0)]
    current_time = get_time()
    first_time = get_time()
    ui = UI()

def exit():
    global dragon, background , enemy_white , enemy_yellow, enemy_pink, enemy_green, Missiles_1, Missiles_2, ice_cragon, ui, Enemy_Missile_List, score
    del(dragon)
    del(score)
    del(background)
    del(enemy_white)
    del(enemy_yellow)
    del(enemy_pink)
    del(enemy_green)
    del(ice_cragon)
    del(Missiles_1)
    del(Missiles_2)
    del(ui)
    del(Enemy_Missile_List)
def pause():#
    pass


def resume():
    pass


def handle_events():
    global dragon,enemy_white , enemy_yellow, enemy_pink, enemy_green
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

#--------몬스터 부르기
def make_monster(time):
    global first_time, enemy_yellow, enemy_white, enemy_pink, enemy_green
    if abs(time - get_time()) > 4:
        first_time = get_time()
        enemy_yellow.append(Enemy_yellow())
        enemy_white.append(Enemy_white())
        enemy_pink.append(Enemy_pink())
        enemy_green.append(Enemy_green())


def update():

    frame_time = get_frame_time()
    make_monster(first_time)
    print(abs(first_time - get_time()))
    score.update(frame_time)
    dragon.update(frame_time)
    ui.update(frame_time)

    # 움직이는 부분
    for white in enemy_white :
        white.update(frame_time)


    for yellow in enemy_yellow :
        yellow.update(frame_time)

    for pink in enemy_pink :
        pink.update(frame_time)

    for green in enemy_green :
        green.update(frame_time)

    for ice in ice_cragon :
        ice.update(frame_time)

    for Missile_1 in Missiles_1:
        Missile_1.update(frame_time)
        if Missile_1.y > 700:
            Missiles_1.remove(Missile_1)

    for Missile_2 in Missiles_2:
        Missile_2.update(frame_time)
        if Missile_2.y >700:
            Missiles_2.remove(Missile_2)

    for member in Enemy_Missile_List :
        is_die = member.update(frame_time)
        if is_die == True :
            Enemy_Missile_List.remove(member)
        if member.y < 50:
            Enemy_Missile_List.remove(member)
        #if  collide(Missile_1,enemy_yellow)

    #충돌부분
    for Missile_1 in Missiles_1:
        for pink in enemy_pink :
            if collide(Missile_1 , pink):
                Missiles_1.remove(Missile_1)
                enemy_pink.remove(pink)
                Missile.sound.play()
                break

    for Missile_1 in Missiles_1:
        for yellow in enemy_yellow :
            if collide(Missile_1 , yellow):
                Missiles_1.remove(Missile_1)
                enemy_yellow.remove(yellow)
                Missile.sound.play()
                break
    for Missile_1 in Missiles_1:
        for white in enemy_white :
            if collide(Missile_1 , white):
                Missiles_1.remove(Missile_1)
                enemy_white.remove(white)
                Missile.sound.play()
                score.get_score(10)
                break

    for Missile_1 in Missiles_1:
        for green in enemy_green :
            if collide(Missile_1 , green):
                Missiles_1.remove(Missile_1)
                enemy_green.remove(green)
                Missile.sound.play()
                score.get_score(10)
                break

    for Missile_1 in Missiles_1:
        for ice in ice_cragon :
            if collide(Missile_1 , ice):
                Missiles_1.remove(Missile_1)

                score.get_score(40)
                ice.get_hp(100)
                if(ice.LIFE == False):
                    ice_cragon.remove(ice)
                    Missile.sound2 .play()
                break

    for enemy_missile in Enemy_Missile_List :
        if collide(enemy_missile, dragon) :
            game_framework.push_state(gameover_state  )

    background.update(frame_time)

#    if score > 100:
#       boss = Boss()



def draw():
    clear_canvas()
    background.draw()
#    background.draw2()
    dragon.draw()
    #dragon.draw_bb()
    ui.draw() # 점수랑 시간
    for white in enemy_white :
        white.draw()
        #white.draw_bb()

    for yellow in enemy_yellow :
        yellow.draw()
        #yellow.draw_bb()

    for pink in enemy_pink :
        pink.draw()
        #pink.draw_bb()

    for green in enemy_green :
        green.draw()
        #green.draw_bb()

    for ice in ice_cragon :
        ice.draw()
        #ice.draw_bb()

    for member in Enemy_Missile_List :
        member.draw()
        #member.draw_bb()

    for Missile_1 in Missiles_1:
        Missile_1.draw()
        #Missile_1.draw_bb()

    for Missile_2 in Missiles_2:
        Missile_2.draw()
        #Missile_2.draw_bb()
    score.draw()
    update_canvas()
    delay(0.04)





#------------------충돌체크--------------------
def collide(a, b):
    left_a, bottom_a, right_a, top_a = a.get_bb()
    left_b, bottom_b, right_b, top_b = b.get_bb()


    if left_a > right_b : return False
    if right_a < left_b : return False
    if top_a < bottom_b : return False
    if bottom_a > top_b : return False

    return True
