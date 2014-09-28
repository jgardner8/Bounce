import pygame
      
class DrawAsCircleMixIn(object):
    """Represents an entity as a circle."""
    def __init__(self, color, radius):
        self.color = color
        self.radius = radius

    def draw(self, position, display): #position represents top-left, not centre as in draw.circle
        pygame.draw.circle(display, self.color, (int(position[0]) + self.radius, int(position[1]) + self.radius), self.radius)