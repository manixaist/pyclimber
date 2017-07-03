"""This module implements a tile object for Py-Climber"""

import pygame
from pygame.sprite import Sprite

class Tile(Sprite):
    """A single map tile - not currently used"""

    def __init__(self, image=None):
        # Solid block will obstruct collision and is the default for now
        self.solid = True
       
        # If no image, then no drawing in that location, otherwise it should
        # reference the previously loaded pygame.Surface
        self.image = image

        # Set default location info (rect)
        self.rect = self.image.get_rect()
