"""This module implements a static sprite that flys into position"""
from pygame.sprite import Sprite


class FlyInSprite(Sprite):
    """A static image sprite that moves to a final position over a number of frames"""
    def __init__(self, settings, screen, image):
        """Init the sprite base class"""
        super().__init__()

        # cache these objects
        self.settings = settings
        self.screen = screen
        self.screen_rect = self.screen.get_rect()
        self.image = image
        self.rect = self.image.get_rect()
        self.dx = 0.0
        self.dy = 0.0
        self.target_top = 0
        self.target_left = 0
        self.start_top = 0
        self.start_left = 0
        self.frames_max = 0
        self.frame_current = 0

    def set_start_position(self, top, left, dx, dy, frames):
        """Sets the initial position and state of the sprite.  It can be off-screen"""
        self.start_left = left
        self.start_top = top
        self.dx = dx
        self.dy = dy
        self.frames_max = frames
        self.reset_position()

    def reset_position(self):
        """Resets the position - best used after set_start_position, but it will work with the init'd defaults as well"""
        self.rect.top = self.start_top
        self.rect.left = self.start_left
        self.frame_current = 0

    def update(self):
        """Move the sprite based on its velocities.  This does not interact with any other objects, so the logic is simple"""

        # No gravity here, these objects will fly at a constant rate
        if self.frame_current < self.frames_max:
            self.rect.left += self.dx
            self.rect.top += self.dy
            self.frame_current += 1

    def draw(self):
        """Draws the image at the sprite's current location"""
        self.screen.blit(self.image, self.rect)

