"""This module is the main entry for the Py-Climber game"""

import sys
import time
import pygame
import game_functions as gf
from pygame.sprite import Group
from image_resources import ImageResources
from settings import Settings
from tilemap import Tilemap

def run_game():
    # Startup pygame object
    pygame.init()

    # Load our settings object and image resources, disk I/O that can be done in advance
    settings = Settings()
    image_res = ImageResources(settings)

    # Create the main screen to render to based on settings
    screen = pygame.display.set_mode((settings.screen_width, settings.screen_height))
    pygame.display.set_caption(settings.caption)
    
    # Create a 2D tilemap - this takes a list of indices and an image list to produce a tiled surface
    tile_map = Tilemap(settings, screen, settings.map_indicies, image_res.tile_images)

    # Use pygame's simple loop management for a fixed 30 FPS
    clock = pygame.time.Clock()
    while True:
        # Should make sure each frame spends at least 1/30 seconds in this loop
        # downside is wasted sleep on fast hardware and slow hardware will lag
        # but slow hardware will always lag and implementing a time-delta based
        # loop for this simple game is IMHO overkill.
        clock.tick(30)

        # Process system events (key-presses, joystick, etc)
        gf.check_events(settings, screen)

        # Update the game (this will update all sub-object and render them to the screen)
        gf.update_screen(settings, screen, image_res, tile_map)

# Invokes the function above when the script is run
run_game()
