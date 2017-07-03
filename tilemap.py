"""This module implements a 2D tilemap for Py-Climber"""

import pygame

class Tilemap():
    """Represents a collection of tile (sprites) that represent a map"""

    def __init__(self, settings, screen, map_indicies, images):
        self.settings = settings
        self.screen = screen
        self.images = images
        self.indicies = map_indicies

        # TODO - should put a Group() of sprites together based on the indicies
        # and use them instead, since eventually we'll use that for collision, etc
    
    def blitme(self):
        """Draws the tilemap."""

        # This is really just for testing to see if it renders properly based on index

        # Loop through each row and render it, simple for now, map fits on the screen
        # skipping the Tile entirely for now and just rendering from the indicies
        # This could work for tiles that were never dynamic (reacting to collisions)
        x_offset = 128
        y_offset = 64
        rect = pygame.Rect((x_offset, y_offset), (self.settings.tile_width, self.settings.tile_height))
        tiles_draw_per_row = 0

        for index in self.indicies:
            if index >= 0:
                self.screen.blit(self.images[index], rect)
            tiles_draw_per_row += 1
            rect.left += self.settings.tile_width

            # Every row worth of tiles, drop down one level and reset the x coord
            if tiles_draw_per_row == self.settings.map_width:
                rect.top += self.settings.tile_height
                rect.left = x_offset
                tiles_draw_per_row = 0
