# TODO:
# FEATURES:
# - collectables which reduce timer
# - slow motion button/meter
# - difficulty levels (speed)

# Imports
import pygame
from pygame.locals import *
pygame.mixer.pre_init(frequency=22050, size=-16, channels=2, buffer=4)
pygame.init()
from Game import Game

# Setup
game = Game()
clock = pygame.time.Clock()
display = pygame.display.set_mode(game.RESOLUTION)
game_running = True

# Functions
def exit_requested(event):
    return event.type == QUIT or (event.type == KEYDOWN and event.key == K_ESCAPE)

def set_caption_to_frame_time(game_name):
    pygame.display.set_caption(game_name + ': ' + str(clock.get_rawtime()) + 'ms/Frame')

# Game Loop
while game_running:
    # Clear Display
    display.fill(game.SCREEN_CLEAR_COLOR)
    
    # Handle Events
    key_events = []
    for event in pygame.event.get():
        if event.type == KEYDOWN:
            key_events.append(event)
        game_running = not exit_requested(event)

    # Update/Draw
    delta = clock.get_time() * game.time_scale
    game.update(delta, key_events)
    game.draw(display)

    # Show Display
    pygame.display.update()
    clock.tick()
    set_caption_to_frame_time(game.GAME_NAME)

# Cleanup
pygame.quit()