"""This module implements standard game functions for Py-Climber, such as processing keypresses"""

import sys
import random
from blob_enemy import Blob
import pygame
import pygame.freetype

def check_events(settings, screen, image_res, player, tile_map, enemies):
    """Watch for keyboard and mouse events"""
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()

        elif event.type == pygame.KEYDOWN:
            check_keydown_events(settings, image_res, event, screen, player, tile_map, enemies)
        elif event.type == pygame.KEYUP:
        	check_keyup_events(settings, event, screen, player, enemies)

def reset_game(settings, image_res, screen, player, tile_map, enemies):
    player.rect.bottom = tile_map.player_bounds_rect.bottom
    player.dx = 0.0
    player.dy = 0.0
    player.dying = False
    player.idle_counter = 0
    player.idle_top = False
    player.reset_game = False
    enemies.clear()
    generate_new_random_blob(settings, screen, image_res.enemy_blob_images, tile_map, enemies)
    tile_map.generate_platforms()

def check_keydown_events(settings, image_res, event, screen, player, tile_map, enemies):
    """Respond to key down events"""
    if event.key == pygame.K_ESCAPE:
        sys.exit()

    if event.key == pygame.K_a:
        generate_new_random_blob(settings, screen, image_res.enemy_blob_images, tile_map, enemies)
        
    if event.key == pygame.K_r:
        reset_game(settings, image_res, screen, player, tile_map, enemies)
    
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

def check_keyup_events(settings, event, screen, player, enemies):
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

def generate_new_random_blob(settings, screen, images, tile_map, enemies):
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
    enemies.append(enemy)
    
def blitHelpText(settings, screen):
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

def update_game_objects(settings, tile_map, player, enemies):
    # Enemy
    for enemy in enemies:
        enemy.update(tile_map)

    # Update the player
    player.update(tile_map, enemies)

def draw_game_objects(settings, screen, tile_map, player, enemies):
    # Draw the player
    player.draw()

    # Enemy
    for enemy in enemies:
        enemy.draw()

    # Draw the map - pass True to render a grid overlay on the tiles
    tile_map.draw()

    # Draw help text
    blitHelpText(settings, screen)

def update_screen(settings, screen, image_res, tile_map, player, enemies):
    """Update images and flip screen"""
    # Redraw screen each pass
    screen.fill(settings.bg_color)

    # UPDATES...
    update_game_objects(settings, tile_map, player, enemies)

    # DRAWS...
    draw_game_objects(settings, screen, tile_map, player, enemies)

    # FLIP....
    pygame.display.flip()
