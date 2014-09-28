from math import floor, fabs

class CollisionsMixIn(object):
    """handles collisions with the level"""
    def __init__(self, start_position, start_velocity, bounce_factor, bounce_volume_factor, level):
        """Bounce factor controls how much speed is lost when bouncing. 1 = no speed lost, 0 = all speed lost.
        Bounce volume factor controls the volume of the bounces, which is multiplied by the ball velocity. 0 is no sound."""
        self.position = list(start_position)
        self.velocity = list(start_velocity)
        self.bounce_factor = bounce_factor
        self.bounce_volume_factor = bounce_volume_factor
        self.level = level

    def collide(self, position, velocity, axis=-1):
        """axis defines the axis to check for collisions on. -1 = both, 0 = x, 1 = y"""
        def calculate_volume(speed):
            IMPACT_SCALE = 1500 #used to translate impact into a range approximately 0-1 for set_volume()
            MIN_IMPACT = 28 #smallest impact that can create sound
            return (fabs(speed) - MIN_IMPACT) / IMPACT_SCALE * self.bounce_volume_factor

        def bounce(axis):
            vol = calculate_volume(self.velocity[axis])
            self.BOUNCE_SOUND.set_volume(vol)
            self.BOUNCE_SOUND.play()
            self.velocity[axis] = -self.velocity[axis] * self.bounce_factor

        def normalise_position(position):
            """object position measured in tiles"""
            return floor(position[0] / self.level.tile_size), floor(position[1] / self.level.tile_size)

        def collide_on_left(pos):
            #Collide with screen boundary
            if self.position[0] < 0: #hit edge of screen
                bounce(0)
                self.position[0] = 0 #set position to collision position
                return
            #Collide with tile
            if pos[1] < self.level.size()[1]: #y pos not outside level
                if self.level[pos[0], pos[1]].solid: #hit tile on left
                    if not self.level[pos[0] + 1, pos[1]].solid: #tile to right (current tile) is not solid
                        bounce(0) #bounce on x axis
                        self.position[0] = (pos[0] + 1) * self.level.tile_size #set position to collision position

        def collide_on_right(pos):
            #Collide with screen boundary
            if pos[0] >= self.level.size()[0] - 1: #hit edge of screen
                bounce(0) #bounce on x axis
                self.position[0] = (self.level.size()[0] - 1) * self.level.tile_size #set position to collision position
                return
            #Collide with tile
            if pos[1] < self.level.size()[1]: #y pos not outside level
                if self.level[pos[0] + 1, pos[1]].solid: #hit tile on right
                    if not self.level[pos[0], pos[1]].solid: #tile to left (current tile) is not solid
                        bounce(0) #bounce on x axis
                        self.position[0] = pos[0] * self.level.tile_size #set position to collision position

        def collide_on_top(pos):
            #Collide with screen boundary
            if self.position[1] < 0: #hit edge of screen
                bounce(1)
                self.position[1] = 0 #set position to collision position
                return
            #Collide with tile
            if pos[0] < self.level.size()[0]: #x pos not outside level
                if self.level[pos[0], pos[1]].solid: #hit tile above
                    if not self.level[pos[0], pos[1] + 1].solid: #tile below (current tile) is not solid
                        bounce(1) #bounce on y axis
                        self.position[1] = (pos[1] + 1) * self.level.tile_size #set position to collision position

        def collide_on_bottom(pos):
            #Collide with screen boundary
            if pos[1] >= self.level.size()[1] - 1: #hit edge of screen
                bounce(1) #bounce on y axis
                self.position[1] = (self.level.size()[1] - 1) * self.level.tile_size #set position to collision position
                return
            #Collide with tile
            if pos[0] < self.level.size()[0]: #x pos not outside level
                if self.level[pos[0], pos[1] + 1].solid: #hit tile below
                    if not self.level[pos[0], pos[1]].solid: #tile above (current tile) is not solid
                        bounce(1) #bounce on y axis
                        self.position[1] = pos[1] * self.level.tile_size #set position to collision position

        if axis != 1:
            if velocity[0] < 0:
                collide_on_left(normalise_position(position))
            elif velocity[0] > 0:
                collide_on_right(normalise_position(position))
        if axis != 0:
            if velocity[1] < 0:
                collide_on_top(normalise_position(position))
            elif velocity[1] > 0:
                collide_on_bottom(normalise_position(position))

    def special_collisions(self):
        """Returns any special objects hit, such as a level end."""
        test = self.position[0] // self.level.tile_size, self.position[1] // self.level.tile_size

        if (self.position[0] // self.level.tile_size == self.level.level_end[0]
        and self.position[1] // self.level.tile_size == self.level.level_end[1]):
            return 'level_end'

    def update(self):
        """Calculates bouncing for every collision, and returns any special objects hit, such as a level end."""
        #As ball can be between tiles, there is 2 extra collision checks, one for x and one for y axis
        self.collide(self.position, self.velocity) #collision 1
        self.collide((self.position[0], self.position[1] + self.level.tile_size), self.velocity, 0)
        self.collide((self.position[0] + self.level.tile_size, self.position[1]), self.velocity, 1)
        return self.special_collisions()