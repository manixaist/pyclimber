"""This module implements settings for Py-Climber."""

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

        # Tile settings
        self.tile_width = 24
        self.tile_height = 24

        # Size of a "level" TESTING
        # Test map
        self.map_width = 16
        self.map_height = 10
        self.map_indicies = [-1, 6, 3, 13, 13, 13, 13, 13, 13, 13, 13, 13, 13, 4, 8, -1,
                             -1, 6, 8, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, 6, 8, -1,
                             -1, 6, 8, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, 6, 8, -1,
                             -1, 6, 8, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, 6, 8, -1,
                             -1, 6, 8, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, 6, 8, -1,
                             -1, 6, 8, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, 6, 8, -1,
                             -1, 6, 8, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, 6, 8, -1,
                             -1, 6, 8, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, 6, 8, -1,
                             -1, 6, 9,  1,  1,  1,  1,  1,  1,  1,  1,  1,  1,10, 8, -1,
                             -1, 6, 7,  7,  7,  7,  7,  7,  7,  7,  7,  7,  7, 7, 8, -1]
