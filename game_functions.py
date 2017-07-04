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


def check_keydown_events(settings, image_res, event, screen, player, tile_map, enemies):
    """Respond to key down events"""
    if event.key == pygame.K_ESCAPE:
        sys.exit()

    if event.key == pygame.K_a:
        enemy = Blob(settings, screen, image_res.enemy_blob_images)
        enemy.rect.left =  random.randint(tile_map.player_bounds_rect.left, tile_map.player_bounds_rect.right - settings.enemy_blob_width)
        enemy.rect.top = tile_map.player_bounds_rect.top
        if random.randint(0, 100) > 50:
            enemy.facing_left = True
            enemy.set_current_animation(settings.anim_name_walk_left)
            enemy.dx = -1 * settings.enemy_blob_dx
        enemies.append(enemy)
        
    if event.key == pygame.K_r:
        player.rect.bottom = tile_map.player_bounds_rect.bottom
        player.dx = 0.0
        player.dy = 0.0
        enemies.clear()
        enemy = Blob(settings, screen, image_res.enemy_blob_images)
        enemy.rect.centerx = tile_map.player_bounds_rect.centerx
        enemy.rect.top = tile_map.player_bounds_rect.top
        enemies.append(enemy)
        tile_map.generate_platforms()
    
    if event.key == pygame.K_LEFT:
        if player.dx == 0.0:
            player.dx = -1 * settings.player_dx
            player.facing_left = True
    
    if event.key == pygame.K_RIGHT:
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
        if player.falling == False:
            player.dy = settings.player_jump_velocity
            player.falling = True
        elif player.air_jumps < player.max_air_jumps:
            player.dy = settings.player_air_jump_velocity
            player.air_jumps += 1

    if event.key == pygame.K_LEFT:
        if player.dx != 0.0:
            player.dx = 0.0
    
    if event.key == pygame.K_RIGHT:
        if player.dx != 0.0:
            player.dx = 0.0

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
    # Update the player
    player.update(tile_map)

    # Enemy
    for enemy in enemies:
        enemy.update(tile_map)

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
