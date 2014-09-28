import pygame # get input
from pygame.locals import * # key constants
from Functions.Math import clip

class InputControllerMixIn(object):
    """Used for all entities that are controlled by user input.
    acceleration_power is the amount to change velocity per second
    button is held (excluding physics influence from other component).
    max_speed is a hard limit measured in pixels/sec."""
    def __init__(self, start_position, start_velocity, acceleration_power, max_speed):
        self.position = start_position
        self.velocity = start_velocity
        self.acceleration_power = acceleration_power
        self.max_speed = max_speed

    def update(self, delta):
        input = pygame.key.get_pressed()
        if input[K_LEFT]:
            self.velocity[0] -= self.acceleration_power * delta
        if input[K_RIGHT]:
            self.velocity[0] += self.acceleration_power * delta
        if input[K_DOWN]: #and self.velocity[1] > 0:
            self.velocity[1] += self.acceleration_power * delta
        self.velocity[0] = clip(self.velocity[0], -self.max_speed, self.max_speed)