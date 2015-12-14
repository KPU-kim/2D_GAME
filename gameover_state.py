import game_framework
from pico2d import *
import flight_main_sea
import flight_title_state


name = "gameover"
image = None
sound3 = None

def enter():
    global image , sound3
    if image == None:
        image = load_image('gameover.png')
    if sound3 == None:
        sound3 = load_music('C:\\2D\\flight_game_fraemwork\\game_over.mp3')
        sound3.set_volume(64)
        sound3.play()

def exit():
    global image
    del(image)

#import flight_main_state

def handle_events():
    events = get_events()
    for event in events:
        if event.type == SDL_QUIT:
            game_framework.quit()
        else:
            if (event.type, event.key) == (SDL_KEYDOWN, SDLK_ESCAPE):
                game_framework.quit()
            elif (event.type, event.key) == (SDL_KEYDOWN, SDLK_SPACE):
                game_framework.change_state(flight_title_state)



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






