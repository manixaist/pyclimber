"""This module implements standard game functions for Py-Climber, such as processing keypresses"""

import sys
import random
from blob_enemy import Blob
import pygame
import pygame.freetype

def check_events(settings, screen, tile_map):
    """Watch for keyboard and mouse events"""
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()

        elif event.type == pygame.KEYDOWN:
            check_keydown_events(settings, event, screen, tile_map)
        elif event.type == pygame.KEYUP:
        	check_keyup_events(settings, event, screen, tile_map)

def reset_game(settings, screen, tile_map):
    player = tile_map.player
    player.rect.bottom = tile_map.player_bounds_rect.bottom
    player.dx = 0.0
    player.dy = 0.0
    player.dying = False
    player.idle_counter = 0
    player.idle_top = False
    player.reset_game = False
    tile_map.enemies.empty()
    generate_new_random_blob(settings, screen, settings.image_res.enemy_blob_images, tile_map)
    tile_map.generate_platforms()
    tile_map.blob_exit.stop_gibbing()

def check_keydown_events(settings, event, screen, tile_map):
    """Respond to key down events"""
    player = tile_map.player
    if event.key == pygame.K_ESCAPE:
        sys.exit()

    if event.key == pygame.K_a:
        generate_new_random_blob(settings, screen, settings.image_res.enemy_blob_images, tile_map)
        
    if event.key == pygame.K_r:
        reset_game(settings, screen, tile_map)
    
    if event.key == pygame.K_LEFT:
        if not player.idle_top:
            if player.dx == 0.0:
                player.dx = -1 * settings.player_dx
                player.facing_left = True
    
    if event.key == pygame.K_RIGHT:
        if not player.idle_top:
            if player.dx == 0.0:
                player.dx = settings.player_dx
                player.facing_left = False
        
    if event.key == pygame.K_F9:
        if settings.fullscreen == True:
            settings.fullscreen = False
            pygame.display.set_mode((800, 600))
        else:
            settings.fullscreen = True
            pygame.display.set_mode((800, 600), pygame.FULLSCREEN)

def check_keyup_events(settings, event, screen, tile_map):
    player = tile_map.player
    if event.key == pygame.K_SPACE:
        if not player.idle_top:
            if player.falling == False:
                player.dy = settings.player_jump_velocity
                player.falling = True
            elif player.air_jumps < player.max_air_jumps:
                player.dy = settings.player_air_jump_velocity
                player.air_jumps += 1

    if event.key == pygame.K_LEFT:
        if not player.idle_top:
            if player.dx != 0.0:
                player.dx = 0.0
        
    if event.key == pygame.K_RIGHT:
        if not player.idle_top:
            if player.dx != 0.0:
                player.dx = 0.0

def generate_new_random_blob(settings, screen, images, tile_map):
    """Generate a new blob enemy and add it to the list"""
    # How this should work:  First pick a floor, this is the middle_row of the triad created
    # when generating the map, e.g. not the floor and not a level where blocks can appear
    floor_number = random.randint(0, settings.map_number_floors - 2)

    # Secondly pick a side, left or right (this will affect placement and initial velocity, etc)
    facing_left = random.choice([True, False])

    # Calculate initial position / velocity / facing flags
    enemy = Blob(settings, screen, images)
    enemy.rect.bottom = settings.tile_height * ( 2 + (3 * floor_number))
    enemy.rect.left = 3 * settings.tile_width + tile_map.x_offset
    enemy.dx = settings.enemy_blob_dx

    if facing_left:
        enemy.rect.left += 10 * settings.tile_width
        enemy.dx *= -1.0
        enemy.facing_left = True
        enemy.set_current_animation(settings.anim_name_walk_left)
    else:
        enemy.facing_left = False
        enemy.set_current_animation(settings.anim_name_walk_right)

    # Add it to the list
    tile_map.enemies.add(enemy)
    
def blit_help_text(settings, screen):
    """Draws the text explaining what keys do what"""
    color_white = (255, 255, 255)
    font = settings.font
    font.render_to(screen, (10,10), "LEFT/RIGHT arrows to walk", settings.font_color)
    font.render_to(screen, (10,30), "SPACE to jump", settings.font_color)
    font.render_to(screen, (15,50), "...can jump once in air", settings.font_color)
    font.render_to(screen, (10,70), "'r' to reset", settings.font_color)
    font.render_to(screen, (10,90), "'a' to add a new enemy", settings.font_color)
    font.render_to(screen, (10,120), "F9 to toggle fullscreen", settings.font_color)
    font.render_to(screen, (10,140), "ESC to exit", settings.font_color)

def update_game_objects(settings, tile_map):
    tile_map.update()

def draw_game_objects(settings, screen, tile_map):
    # Draw the map - pass True to render a grid overlay on the tiles
    tile_map.draw()

    # Draw help text
    blit_help_text(settings, screen)

def update_screen(settings, screen, tile_map):
    """Update images and flip screen"""
    # Redraw screen each pass
    screen.fill(settings.bg_color)

    # UPDATES...
    update_game_objects(settings, tile_map)

    # DRAWS...
    draw_game_objects(settings, screen, tile_map)

    # FLIP....
    pygame.display.flip()
