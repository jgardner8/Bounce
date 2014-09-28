class MovableMixIn(object):
    """Makes an object movable by integrating a velocity into their position each update."""
    def __init__(self, start_position, start_velocity):
        self.position = list(start_position)
        self.velocity = list(start_velocity)

    def update(self, delta):
        self.position[0] += self.velocity[0] * delta
        self.position[1] += self.velocity[1] * delta