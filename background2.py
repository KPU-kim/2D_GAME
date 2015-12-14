import random
from pico2d import *

background2_y = 0
background2_y_2 = 700

class Background2:
    move_y = 100
    def __init__(self):
        self.image = load_image('C:\\2D\\flight_game_fraemwork\\dragon flight\\dragon flight\\background\\desert.png')
        self.image2 = load_image('C:\\2D\\flight_game_fraemwork\\dragon flight\\dragon flight\\background\\desert.png')
        self.bgm = load_music('C:\\2D\\flight_game_fraemwork\\dragon flight\\dragon flight\\bgm\\my_friend_dragon.mp3')
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
