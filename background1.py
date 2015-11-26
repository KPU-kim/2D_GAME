import random
from pico2d import *

background1_y = 0
background1_y_2 = 700

class Background1:
    def __init__(self):
        self.image = load_image('C:\\2D\\flight_game_fraemwork\\dragon flight\\dragon flight\\background\\spring.png')
        self.image2 = load_image('C:\\2D\\flight_game_fraemwork\\dragon flight\\dragon flight\\background\\spring.png')
        self.bgm = load_music('C:\\2D\\flight_game_fraemwork\\dragon flight\\dragon flight\\bgm\\dragon_flight.mp3')
        self.bgm.set_volume(30)
        self.bgm.repeat_play()
    def update(self):
        global background1_y, background1_y_2
        background1_y -=5
        background1_y_2 -=5
        if(background1_y_2 == 0):
            background1_y = 0
            background1_y_2 = 700
    def draw(self):
        global background1_y, background1_y_2
        self.image.draw_to_origin(0, background1_y, 400,700)
    def draw2(self):
        global background1_y, background1_y_2
        self.image.draw_to_origin(0, background1_y_2, 400,700)
