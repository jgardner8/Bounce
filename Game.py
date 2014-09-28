import pygame
from pygame.locals import K_n, K_r
from Level import Level
from Player import Player
from Timer import Timer

class Game(object):
    """Holds all the game objects and runs the game
    pygame must be initialised before including this."""
    # Constants
    #   Colors
    SCREEN_CLEAR_COLOR = pygame.Color(255, 255, 255)
    PLAYER_COLOR = pygame.Color(0, 0, 0)
    #       Tiles
    SOLID_TILE_COLOR = pygame.Color(128, 128, 128)
    END_TILE_COLOR = pygame.Color(0, 0, 255)

    #   Gameplay
    GAME_NAME = 'Bounce'
    RESOLUTION = (900, 600)
    TILE_SIZE = 15 #60x40 tiles
    DEF_TIME_SCALE = 0.001 #0.001 is standard time, where each unit is per second

    #   Timer
    TIMER_FONT = pygame.font.SysFont("monospace", 20)
    TIMER_COLOR = pygame.Color(0, 0, 0)
    TIMER_POSITION = (800, 15)

    #   Sounds
    BOUNCE_VOLUME = 0.8
    POPCORN_VOLUME = 0.15

    #   Controls
    NEXT_LEVEL_BTN = K_n
    RESTART_BTN = K_r

    def __init__(self):
        self.timer = Timer(self.TIMER_FONT, self.TIMER_COLOR, self.TIMER_POSITION)
        self.time_scale = self.DEF_TIME_SCALE

        self.current_level = 0
        self.load_next_level()

        self.player.POPCORN_SOUND.set_volume(self.POPCORN_VOLUME)

    def restart_level(self):
        player_start = self.level.load_level(self.current_level)
        self.player = Player(player_start, (0, 0), self.PLAYER_COLOR, self.BOUNCE_VOLUME, self.level)
        self.timer.time = 0
        self.level_complete = False

    def load_next_level(self):
        self.current_level += 1
        self.level = Level([res // self.TILE_SIZE for res in self.RESOLUTION], self.TILE_SIZE, self.SOLID_TILE_COLOR, self.END_TILE_COLOR)
        self.restart_level()

    def handle_input(self, key_events):
        for event in key_events:
            if event.key == self.NEXT_LEVEL_BTN:
               self.load_next_level()
            elif event.key == self.RESTART_BTN:
                self.restart_level()

    def update(self, delta, key_events):
        self.handle_input(key_events)
        if not self.level_complete:
            special_collisions = self.player.update(delta)
            self.level_complete = special_collisions == 'level_complete'
            self.timer.update(delta)

    def draw(self, display):
        self.level.draw(display)
        self.player.draw(display)
        self.timer.draw(display)