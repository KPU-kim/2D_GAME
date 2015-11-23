import game_framework
from pico2d import *
import flight_main_sea
import flight_main_spring
import flight_main_desert

name = "selbackState"
image = None


def enter():
    global image
    image = load_image('select_back.png')


def exit():
    global image
    del(image)

#import flight_main_state

def handle_events():
    global x, y
    events = get_events()
    for event in events:
        if event.type == SDL_QUIT:
            game_framework.quit()

        elif event.type == SDL_MOUSEMOTION:
            x, y = event.x, 700 - event.y

        elif event.type == SDL_MOUSEBUTTONDOWN:
            x, y = event.x, 700 - event.y
            if x > 130 and x < 258 and y > 29 and y < 199:
                game_framework.change_state(flight_main_sea)
            if x > 130 and x < 258 and y > 260 and y < 432:
                game_framework.change_state(flight_main_desert)
            if x > 130 and x < 258 and y > 488 and y < 658:
                game_framework.change_state(flight_main_spring)


        else:
            if (event.type, event.key) == (SDL_KEYDOWN, SDLK_ESCAPE):
                game_framework.quit()
            #elif (event.type, event.key) == (SDL_KEYDOWN, SDLK_SPACE):
            #    game_framework.change_state(flight_main_state)



def draw():
    clear_canvas()
    image.draw_to_origin(0, 0, 400,700)
    update_canvas()


def update():
    pass


def pause():
    pass


def resume():
    pass
