"""This module implements the platform block object (sprite) for Py-Climber"""
import pygame
from pygame.sprite import Sprite

class Block(Sprite):
    """Block object"""

    def __init__(self, settings, screen, image):
        """Initialize the block, not much to do other than save the params"""
        super().__init__()
        self.settings = settings
        self.screen = screen
        self.image = image
        self.rect = self.image.get_rect()
        self.screen_rect = screen.get_rect()

    # 'draw' is required by pygame.Sprite.Group for drawing in batches
    def draw(self):
        """Draws the block at its current position on the screen"""
        self.screen.blit(self.image, self.rect)
        