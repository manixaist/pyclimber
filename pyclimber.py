"""This module is the main entry for the Py-Climber game"""

import game_functions as gf
from image_resources import ImageResources
from settings import Settings
from tilemap import Tilemap
from player import Player
from blob_enemy import Blob
import random
import pygame

def run_game():
    """Main entry point for Py-Climber"""

    # Startup pygame object
    pygame.init()

    random.seed()

    # Load our settings object and image resources, disk I/O that can be done in advance
    settings = Settings()
    image_res = ImageResources(settings)

    # Create the main screen to render to based on settings
    screen = pygame.display.set_mode((settings.screen_width, settings.screen_height))
    pygame.display.set_caption(settings.caption)
    
    # Create a 2D tilemap - this takes a list of indices and an image list to produce a tiled surface
    tile_map = Tilemap(settings, screen, settings.map_indicies, image_res.tile_images, image_res.block_image)

    # Overwrite default indices with generated map 
    tile_map.generate_basic_map(settings.map_number_floors , settings.map_number_subfloors)

    # Create player
    player = Player(settings, screen, image_res.player_sprite_images, tile_map)

    # Create an enemies list
    enemies = []

    # Reset the game
    gf.reset_game(settings, image_res, screen, player, tile_map, enemies)

    # Use pygame's simple loop management for a fixed 30 FPS
    clock = pygame.time.Clock()
    new_enemy_counter = 0
    while True:
        # Should make sure each frame spends at least 1/30 seconds in this loop
        # downside is wasted sleep on fast hardware and slow hardware will lag
        # but slow hardware will always lag and implementing a time-delta based
        # loop for this simple game is IMHO overkill.
        clock.tick(30)

        # Process system events (key-presses, joystick, etc)
        gf.check_events(settings, screen, image_res, player, tile_map, enemies)

        # Update the game (this will update all sub-object and render them to the screen)
        gf.update_screen(settings, screen, image_res, tile_map, player, enemies)

        if player.reset_game:
            gf.reset_game(settings, image_res, screen, player, tile_map, enemies)

        new_enemy_counter += 1
        if new_enemy_counter >= settings.enemy_generation_rate:
            new_enemy_counter = 0
            gf.generate_new_random_blob(settings, screen, image_res.enemy_blob_images, tile_map, enemies)

# Invokes the function above when the script is run
run_game()
