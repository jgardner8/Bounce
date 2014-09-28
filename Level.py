import pygame
import os
from Tile import Tile

class Level(object):
    """A level to play on, a collection of tiles."""
    def __init__(self, field_size, tile_size, solid_color, level_end_color):
        self.solid_color = solid_color
        self.level_end_color = level_end_color
        self.tile_size = tile_size
        self.tiles = [[Tile(solid=False) for _ in range(field_size[1])] for _ in range(field_size[0])] # 2d list
        self.num_levels = self.get_num_of_levels()

    def draw(self, display):
        for x in range(len(self.tiles)):
            for y in range(len(self.tiles[x])):
                if self.tiles[x][y].solid:
                    pygame.draw.rect(display, self.solid_color, (x*self.tile_size, y*self.tile_size, self.tile_size, self.tile_size))
                elif (x, y) == self.level_end:
                    x_pos, y_pos = x * self.tile_size, y * self.tile_size
                    pygame.draw.polygon(display, self.level_end_color,                              #triangle
                                        [(x_pos + self.tile_size // 2, y_pos + 2),                  #top
                                         (x_pos + 1, y_pos + self.tile_size - 1),                   #right
                                         (x_pos + self.tile_size - 1, y_pos + self.tile_size - 1)]) #left
    def __getitem__(self, xy):
        x, y = xy
        return self.tiles[x][y]

    def size(self):
        return len(self.tiles), len(self.tiles[0])

    def get_num_of_levels(self):
        """Gets the number of defined levels in the levels/ directory"""
        i = 1
        while os.path.isfile(self.construct_file_path(i)):
            i += 1
        return i-1

    def construct_file_path(self, level_num):
        return os.path.join("Levels", "level" + str(level_num) + ".bmp")

    def load_level(self, level_num):
        """Turns self into the level object represented by the level file "level" + level_num + ".bmp".
        level files are simply 24-bit bitmaps, where each pixel corresponds to a position
        in the level, and the tile type depends on the color.
        Returns the position to start the player at."""
        # Color constants
        SOLID_COLOR = (0, 0, 0)
        START_COLOR = (255, 0, 0)
        END_COLOR = (0, 0, 255)

        # Image loading
        safe_level_num = (level_num - 1) % self.num_levels + 1
        bmp = pygame.image.load(self.construct_file_path(safe_level_num))
        assert (bmp.get_width() == self.size()[0] and bmp.get_height() == self.size()[1]), \
            'Level image should be {}x{} pixels in size.'.format(*self.size())

        # Load into level
        pixels = pygame.PixelArray(bmp)
        for x in range(pixels.shape[0]):
            for y in range(pixels.shape[1]):
                if pixels[x, y] == bmp.map_rgb(SOLID_COLOR):
                    self.tiles[x][y] = Tile(solid=True)
                elif pixels[x, y] == bmp.map_rgb(START_COLOR):
                    player_start = (x * self.tile_size, y * self.tile_size)
                elif pixels[x, y] == bmp.map_rgb(END_COLOR):
                    level_end = x, y

        # Check level is valid
        assert ('player_start' in locals()), \
            "No player start position (colour {} in RGB) was defined in the level image.".format(START_COLOR)
        assert ('level_end' in locals()), \
            "No level end position (color {} in RGB) was defined in the level image.".format(END_COLOR)

        # Complete level setup
        self.level_end = level_end
        return player_start