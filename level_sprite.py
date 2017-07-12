"""This module implements a sprite that shows the level text"""
from flyin_sprite import FlyInSprite

class LevelSprite(FlyInSprite):
    """Static image sprite for 'LEVEL' text"""
    
    def __init__(self, settings, screen):
        """Init the sprite"""
        super().__init__(settings, screen, settings.image_res.level_image)
        self.set_start_position(self.screen_rect.bottom, self.screen_rect.left + self.settings.tile_width, 0, -20, 20)
