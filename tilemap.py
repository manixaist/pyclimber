"""This module implements a 2D tilemap for Py-Climber"""

import pygame
import random
from block import Block
from pygame.sprite import Group

class Tilemap():
    """Represents a collection of tile (sprites) that represent a map"""

    def __init__(self, settings, screen, map_indicies, images, block_image):
        self.settings = settings
        self.screen = screen
        self.images = images
        self.indicies = map_indicies
        self.screen_rect = screen.get_rect()
        self.player_bounds_rect = pygame.Rect((0,0), (0,0))
        self.block_image = block_image
        self.block_groups = []

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
        self.player_bounds_rect.top = 0
        self.player_bounds_rect.left = x_offset
        self.player_bounds_rect.width = self.settings.map_playable_width * self.settings.tile_width
        self.player_bounds_rect.height = self.screen_rect.height - ((number_of_subfloor_rows + 1) * self.settings.tile_height)
        
        self.indicies.clear()
        self.indicies.extend(new_indices)
        
        self.generate_platforms()

    def generate_platforms(self):
        """Make groups of sprites that contain the blocks for the player to stand on"""

        # Every block is contained within the self.player_bounds_rect

        # Find each "row" of tiles that can contain blocks and add some
        # Eligible rows are every 3rd row starting from the 2nd to top, except the very bottom floor
        row_rect = pygame.Rect((self.player_bounds_rect.left, self.player_bounds_rect.top + (self.settings.tile_height * 2)), 
            (self.player_bounds_rect.width, self.settings.tile_width)) 
        
        self.block_groups.clear()
        for row in range(0, (self.settings.map_number_floors-1)):
            new_group = Group()
            # Skip one column per row randomly
            skip_col = random.randint(0, self.settings.map_playable_width-1)
            # Each column in the eligble row has 4 valid placements for a block
            # Note - there are more permutations, these are just the ones allowed
            # OO OO OO OO
            # XX OX OX OO
            for col in range(0, self.settings.map_playable_width):
                if col == skip_col:
                    continue

                # TESTING - for now always fill the top 2 quadrants of the tile with blocks
                new_block_left = Block(self.settings, self.screen, self.block_image)
                new_block_right = Block(self.settings, self.screen, self.block_image)
                new_block_left.rect.top = row_rect.top
                new_block_left.rect.left = row_rect.left + col * self.settings.tile_width
                new_block_right.rect = new_block_left.rect.move(new_block_right.rect.width, 0)
                new_group.add(new_block_left)
                new_group.add(new_block_right)
            
            # Each row is it's own group.  This should limit collision checks later
            self.block_groups.append(new_group)
            # Shif the bounding rect down one floor
            row_rect = row_rect.move(0, self.settings.tile_height * 3)

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

        # Draw the blocks
        for group in self.block_groups:
            # This works because each block has 'image' member defined
            group.draw(self.screen)