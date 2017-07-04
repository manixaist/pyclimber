"""This module implements settings for Py-Climber."""
import pygame.freetype

class Settings():
    """A class to store all settings for pyclimber."""

    def __init__(self):
        """Initialize the game's settings."""
        
        # screen settings
        self.screen_width = 800
        self.screen_height = 600
        self.caption = "Py-Climber"
        self.bg_color = (26, 23, 22)
        self.color_key = (255, 0, 255)
        self.fullscreen = False

        # quick font
        self.font = pygame.freetype.SysFont(None, 16)
        self.font_color = (255, 255, 255)

        # Global sprite settings
        self.gravity = 1.35
        self.terminal_velocity = 12
        
        # Player sprite settings
        self.player_width = 24
        self.player_height = 32
        self.player_jump_velocity = -15
        self.player_air_jump_velocity = -10
        self.player_max_air_jumps = 1
        # transparent pixels to offset for horizontal collision (image dependent)
        self.player_sprite_horz_margin = 2
        # transparent pixels to offset for vertical collision (e.g. jumps)
        self.player_sprite_top_margin = 8

        # Player animation names
        self.anim_name_idle_left = 'IDLE.L'
        self.anim_name_idle_right = 'IDLE.R'
        self.anim_name_walk_left = 'WALK.L'
        self.anim_name_walk_right = 'WALK.R'
        self.anim_name_jump_up_left = 'JUMPUP.L'
        self.anim_name_jump_down_left = 'JUMPDOWN.L'
        self.anim_name_jump_up_right = 'JUMPUP.R'
        self.anim_name_jump_down_right = 'JUMPDOWN.R'

        # Tile settings
        self.tile_width = 24
        self.tile_height = 24

        # Size of a "level" TESTING
        # Test map
        self.map_width = 16
        self.map_height = 10
        self.map_playable_width = 10
        self.map_indicies = [-1]
        self.map_number_floors = 8
        self.map_number_subfloors = 1
