class GravityMixIn(object):
    """Applies a gravity force, separate to the usual physics."""
    def __init__(self, start_velocity, gravity_force=1000):
        self.velocity = list(start_velocity)
        self.gravity_force = gravity_force
    
    def update(self, delta):
        self.velocity[1] += self.gravity_force * delta