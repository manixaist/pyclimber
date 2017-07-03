"""This module implements standard game functions for Py-Climber, such as processing keypresses"""

import sys
import pygame

def check_events(settings, screen):
    """Watch for keyboard and mouse events"""
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()

        elif event.type == pygame.KEYDOWN:
            check_keydown_events(settings, event, screen)
        #elif event.type == pygame.KEYUP:
        #	check_keyup_events(settings, event)


def check_keydown_events(settings, event, screen):
    """Respond to key down events"""
    if event.key == pygame.K_q:
        sys.exit()
    elif event.key == pygame.K_F9:
        if settings.fullscreen == True:
            settings.fullscreen = False
            pygame.display.set_mode((800, 600))
        else:
            settings.fullscreen = True
            pygame.display.set_mode((800, 600), pygame.FULLSCREEN)

#def check_keyup_events(settings, event, ship):
#    pass

def update_screen(settings, screen, image_res, tile_map):
    """Update images and flip screen"""
    # Redraw screen each pass
    screen.fill(settings.bg_color)
    
    # Draw the map
    tile_map.blitme()

    # Draw the player
    # TODO

    # Make the most recently drawn screen visible
    pygame.display.flip()
