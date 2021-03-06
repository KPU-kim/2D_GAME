__author__ = 'Owner'

import random
from pico2d import *

background_y = 0
background_y_2 = 700

class Background:
    move_y = 100
    def __init__(self):
        self.image = load_image('dragon flight\\dragon flight\\background\\sea.png')
        #self.image2 = load_image('C:\\2D\\flight_game_fraemwork\\dragon flight\\dragon flight\\background\\sea.png')
        self.bgm = load_music('dragon flight\\dragon flight\\bgm\\dragon_flight2.mp3')
        self.bgm.set_volume(30)
        self.bgm.repeat_play()
        self.y = 0

    def update(self, frame_time):
        speed = frame_time * self.move_y
        self.y += speed
        if(self.y >= 700) :
            self.y = 0

    def draw(self):
        self.image.clip_draw(0, int(self.y), 400, int(700-self.y)+1, 200, int((700 - self.y)/2))
        self.image.clip_draw(0, 0, 400, int(self.y)+1, 200, 700 - int(700 - (700 - self.y))/2)

