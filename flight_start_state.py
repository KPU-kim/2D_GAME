import game_framework
from pico2d import *
import flight_title_state

name = "StartState"
image = None
logo_time = 0.0


def enter():
    global image
    open_canvas(400,700)
    image = load_image('kpu_credit.png')


def exit():
    global image
    del(image)
    close_canvas()

def update():
    global logo_time

    if(logo_time > 1.0):
        logo_time = 0
       # game_framework.quit()
        game_framework.push_state(flight_title_state)
    delay(0.01)
    logo_time += 0.01


def draw():
    global image
    clear_canvas()
    image.draw_to_origin(0, 0, 400,700)
    update_canvas()


def handle_events():
    events = get_events()



def pause(): pass


def resume(): pass




