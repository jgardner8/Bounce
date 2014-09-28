import pygame
import os

class SoundMixIn(object):
    BOUNCE_SOUND = pygame.mixer.Sound(os.path.join('Sounds', 'bounce.wav'))
    POPCORN_SOUND = pygame.mixer.Sound(os.path.join('Sounds', 'popcorn.wav'))