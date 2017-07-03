"""This module implements standard game functions for Py-Climber, such as processing keypresses"""

import sys
import pygame
import pygame.freetype
from player import Player

def check_events(settings, screen, player):
    """Watch for keyboard and mouse events"""
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()

        elif event.type == pygame.KEYDOWN:
            check_keydown_events(settings, event, screen, player)
        elif event.type == pygame.KEYUP:
        	check_keyup_events(settings, event, screen, player)


def check_keydown_events(settings, event, screen, player):
    """Respond to key down events"""
    if event.key == pygame.K_ESCAPE:
        sys.exit()

    if event.key == pygame.K_r:
        player.rect.top = screen.get_rect().top
        player.dx = 0.0
        player.dy = 0.0
    
    if event.key == pygame.K_LEFT:
        if player.moving_horz == False:
            player.dx = -3.0
            player.moving_horz = True
    
    if event.key == pygame.K_RIGHT:
        if player.moving_horz == False:
            player.dx = 3.0
            player.moving_horz = True
    
    if event.key == pygame.K_F9:
        if settings.fullscreen == True:
            settings.fullscreen = False
            pygame.display.set_mode((800, 600))
        else:
            settings.fullscreen = True
            pygame.display.set_mode((800, 600), pygame.FULLSCREEN)

def check_keyup_events(settings, event, screen, player):
    if event.key == pygame.K_SPACE:
        if player.falling == False:
            player.dy = settings.player_jump_velocity
            player.falling = True
        elif player.air_jumps < player.max_air_jumps:
            player.dy = settings.player_air_jump_velocity
            player.air_jumps += 1

    if event.key == pygame.K_LEFT:
        if player.moving_horz == True:
            player.dx = 0.0
            player.moving_horz = False
    
    if event.key == pygame.K_RIGHT:
        if player.moving_horz == True:
            player.dx = 0.0
            player.moving_horz = False

def blitHelpText(settings, screen):
    """Draws the text explaining what keys do what"""
    color_white = (255, 255, 255)
    font = settings.font
    font.render_to(screen, (10,10), "LEFT/RIGHT arrows to walk", settings.font_color)
    font.render_to(screen, (10,30), "SPACE to jump", settings.font_color)
    font.render_to(screen, (15,50), "...can jump once in air", settings.font_color)
    font.render_to(screen, (10,70), "'r' to reset player position", settings.font_color)
    font.render_to(screen, (10,90), "F9 to toggle fullscreen", settings.font_color)
    font.render_to(screen, (10,120), "ESC to exit", settings.font_color)

def update_screen(settings, screen, image_res, tile_map, player):
    """Update images and flip screen"""
    # Redraw screen each pass
    screen.fill(settings.bg_color)

    # UPDATES...
    # Update the player
    player.update(tile_map)

    # DRAWS...
    # Draw the map - pass True to render a grid overlay on the tiles
    tile_map.blitme(True)

    # Draw the player
    player.blitme()

    # Draw help text
    blitHelpText(settings, screen)

    # FLIP....
    # Make the most recently drawn screen visible
    pygame.display.flip()
