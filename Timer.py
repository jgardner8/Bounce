class Timer(object):
    """Draws time elapsed when given clock deltas (from frametimes) to a pygame display"""
    def __init__(self, font, color, position):
        self.font = font
        self.color = color
        self.position = position
        self.restart()

    def restart(self):
        self.time = 0

    def update(self, delta):
        self.time += delta

    def draw(self, display):
        toDraw = self.font.render('{0:.3f}'.format(self.time), 1, self.color)
        display.blit(toDraw, self.position)