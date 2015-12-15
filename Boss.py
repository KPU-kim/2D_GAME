__author__ = 'Owner'
from pico2d import *
#from Kirby_missile import *
import random


class Ice_cragon:
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
        distance = Ice_cragon.RUN_SPEED_PPS * frame_time
        self.frame = (self.frame + 1) % 4
        self.y -= 5

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