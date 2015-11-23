__author__ = 'Owner'

import random
from pico2d import *

background_y = 0
background_y_2 = 700

class Background:
    def __init__(self):
        self.image = load_image('C:\\2D\\flight_game_fraemwork\\dragon flight\\dragon flight\\background\\sea.png')
        self.image2 = load_image('C:\\2D\\flight_game_fraemwork\\dragon flight\\dragon flight\\background\\sea.png')
        self.bgm = load_music('C:\\2D\\flight_game_fraemwork\\dragon flight\\dragon flight\\bgm\\dragon_flight2.mp3')
        self.bgm.set_volume(60)
        self.bgm.repeat_play()

    def update(self):
        global background_y, background_y_2
        background_y -=5
        background_y_2 -=5
        if(background_y_2 == 0):
            background_y = 0
            background_y_2 = 700
    def draw(self):
        global background_y, background_y_2
        self.image.draw_to_origin(0, background_y, 400,700)
    def draw2(self):
        global background_y, background_y_2
        self.image.draw_to_origin(0, background_y_2, 400,700)