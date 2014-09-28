from MixIns.DrawAsCircleMixIn import DrawAsCircleMixIn
from MixIns.InputControllerMixIn import InputControllerMixIn
from MixIns.MovableMixIn import MovableMixIn
from MixIns.GravityMixIn import GravityMixIn
from MixIns.CollisionsMixIn import CollisionsMixIn
from MixIns.SoundMixIn import SoundMixIn

class Player(MovableMixIn, DrawAsCircleMixIn, InputControllerMixIn, GravityMixIn, CollisionsMixIn, SoundMixIn):
    """the player sprite"""
    def __init__(self, position, velocity, color, bounce_volume, level):
        ACCELERATION_POWER = 2000
        MAX_SPEED = 600
        DEF_BOUNCE_FACTOR = 0.8
        COLLISION_BOX_SHRINK = 1
        InputControllerMixIn.__init__(self, position, velocity, ACCELERATION_POWER, MAX_SPEED)
        DrawAsCircleMixIn.__init__(self, color, level.tile_size // 2 + COLLISION_BOX_SHRINK)
        MovableMixIn.__init__(self, position, velocity)
        GravityMixIn.__init__(self, velocity)
        CollisionsMixIn.__init__(self, position, velocity, DEF_BOUNCE_FACTOR, bounce_volume, level)
        SoundMixIn.__init__(self)

    def update(self, delta):
        InputControllerMixIn.update(self, delta)
        GravityMixIn.update(self, delta)
        special_collisions = CollisionsMixIn.update(self)
        MovableMixIn.update(self, delta)
        if special_collisions == 'level_end':
            self.POPCORN_SOUND.play()
            return 'level_complete'

    def draw(self, display):
        DrawAsCircleMixIn.draw(self, self.position, display)