__author__ = 'Owner'
from pico2d import *

class UI:

    def __init__(self):

        self.font = load_font("NanumPen.TTF", 30)

    def update(self, frame_time):
        self.time = get_time()


    def draw(self):

        self.font.draw(310, 680, "time: %d" % (self.time), (255, 255, 255))

        pass

