"""This module implements a 2D tilemap for Py-Climber"""

import pygame

class Tilemap():
    """Represents a collection of tile (sprites) that represent a map"""

    def __init__(self, settings, screen, map_indicies, images):
        self.settings = settings
        self.screen = screen
        self.images = images
        self.indicies = map_indicies
        self.screen_rect = screen.get_rect()
        self.sprite_rect = pygame.Rect((0,0), (0,0))
    
    def generate_basic_map(self, number_of_floors, number_of_subfloor_rows=0):
        """Builds a basic tiled map - this depends on the index ordering of the tiles image"""
        # Every 'floor' that is not the bottom or below contains 3 tile rows of the same pattern
        # So just make number_of_floors - 1 entries for those, then generate the bottom 'floor'
        # which just has a different 3rd row of indices.  If tiles below that are needed for
        # looks then they all use the same pattern
        empty_row = [-1, 6, 8, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, 6, 8, -1]
        bottom_row = [-1, 6, 9,  1,  1,  1,  1,  1,  1,  1,  1,  1,  1, 10, 8, -1]
        sub_row = [-1, 6, 7,  7,  7,  7,  7,  7,  7,  7,  7,  7,  7, 7, 8, -1]

        row_index = 0
        new_indices = []
        while row_index < (number_of_floors - 1):
            new_indices.extend(empty_row)
            new_indices.extend(empty_row)
            new_indices.extend(empty_row)
            row_index += 1

        # bottom floor
        new_indices.extend(empty_row)
        new_indices.extend(empty_row)
        new_indices.extend(bottom_row)

        # optional sub-bottom floor row
        row_index = 0
        while row_index < number_of_subfloor_rows:
            new_indices.extend(sub_row)
            row_index += 1

        x_offset = (self.screen_rect.width - (self.settings.map_width * self.settings.tile_width)) // 2
        x_offset += self.settings.tile_width * ((self.settings.map_width - self.settings.map_playable_width)/2)
        self.sprite_rect.left = x_offset
        self.sprite_rect.width = self.settings.map_playable_width * self.settings.tile_width
        self.sprite_rect.height = self.screen_rect.height
        self.sprite_rect.left = x_offset
        self.sprite_rect.bottom = self.screen_rect.height - ((number_of_subfloor_rows + 1) * self.settings.tile_height)
        
        self.indicies.clear()
        self.indicies.extend(new_indices)

    def blitme(self, draw_grid_overlay=False):
        """Draws the tilemap."""

        # Center the map horizontally
        x_offset = (self.screen_rect.width - (self.settings.map_width * self.settings.tile_width)) // 2
        # Make the bottom of the map align with the bottom of the screen
        number_of_rows = len(self.indicies) / self.settings.map_width
        map_height = number_of_rows * self.settings.tile_height
        y_offset = self.screen_rect.height - map_height
        rect = pygame.Rect((x_offset, y_offset), (self.settings.tile_width, self.settings.tile_height))
        tiles_draw_per_row = 0

        # Loop through each row and render it, simple for now, map fits on the screen
        for index in self.indicies:
            if index >= 0:
                self.screen.blit(self.images[index], rect)
                if draw_grid_overlay:
                    color_red = (255, 0, 0)
                    pygame.draw.rect(self.screen, color_red, rect, 1)
            tiles_draw_per_row += 1
            rect.left += self.settings.tile_width

            # Every row worth of tiles, drop down one level and reset the x coord
            if tiles_draw_per_row == self.settings.map_width:
                rect.top += self.settings.tile_height
                rect.left = x_offset
                tiles_draw_per_row = 0