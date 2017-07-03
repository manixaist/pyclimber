"""This module implements the player object (sprite) for Py-Climber"""
import pygame
from pygame.sprite import Sprite
from tilemap import Tilemap

class Player(Sprite):
    """Player object"""

    def __init__(self, settings, screen, images):
        """Initialize the player sprite"""
        super().__init__()
        self.settings = settings
        self.screen = screen
        self.images = images
        self.screen_rect = screen.get_rect()
        # All images are the same size, so set the rect to the first one
        self.rect = images[0].get_rect()
        self.rect.top = self.screen_rect.top
        self.rect.left = self.screen_rect.width / 2
        self.dx = 0.0
        self.dy = 0.0
        self.moving_horz = False
        self.falling = False
        self.falling_frames = 0
        self.air_jumps = 0
        self.max_air_jumps = settings.player_max_air_jumps

    def update(self, tile_map):
        """Updates the player sprite's position"""
        # The dy should be controlled by 'gravity' only for now - jumps will impart an
        # Initial up velocity (done in the keyhandler), then gravity acts here on update.
        # Without some sort of gravity approximation, sprites would move at the same speed
        # while in the air and seem very light, like they're walking on the moon in low gravity
        # only worse.  Not a problem for a top-down 2D game :)

        # If not on the ground floor, just assume we're falling (for now this will be true)
        if self.rect.bottom < tile_map.player_bounds_rect.bottom and self.falling == False:
            self.falling = True
            self.falling_frames = 1

        if self.falling:
            # As long as the player is continually falling, the 'speed' increases each
            # frame by the acceleration until some terminal speed
            if self.dy < self.settings.terminal_velocity:
                self.dy += self.settings.gravity
            self.rect.centery += self.dy
            self.falling_frames += 1

        # Bounds check on bottom edge
        if self.rect.bottom > tile_map.player_bounds_rect.bottom:
            self.rect.bottom = tile_map.player_bounds_rect.bottom
            self.dy = 0.0
            self.falling = False
            self.air_jumps = 0

        # Left/Right bounds containment check
        if (self.dx > 0 and self.rect.right - self.settings.player_sprite_horz_margin < tile_map.player_bounds_rect.right):
            self.rect.centerx += self.dx
        elif (self.dx < 0 and self.rect.left + self.settings.player_sprite_horz_margin > tile_map.player_bounds_rect.left):
            self.rect.centerx += self.dx

    def blitme(self):
        """Draws the player at its current position on the screen"""
        self.screen.blit(self.images[0], self.rect)