"""Particle object module for Py-Climber"""
import pygame

class Particle():
    """A single particle object which is owned by the generator"""
    def __init__(self, screen, settings, x, y, dx, dy, width, color):
        """Save the initial state"""
        self.x = x
        self.y = y
        self.dx = dx
        self.dy = dy
        self.color = color
        self.screen = screen
        self.screen_rect = self.screen.get_rect()
        self.settings = settings
        self.width = width

    def update(self):
        """Update the particle's velocity and position"""
        self.x += self.dx
        self.dy += self.settings.gravity
        if self.dy > self.settings.terminal_velocity:
            self.dy = self.settings.terminal_velocity
        self.y += self.dy

    def alive(self):
        """Once the particle has left the screen, it's not useful, so consider it dead"""
        return self.y <= self.screen_rect.bottom

    def draw(self):
        """Draw the particle at its current location"""
        # We're not a sprite, so just draw a simple filled rect
        pygame.draw.rect(self.screen, self.color, (self.x, self.y, self.width, self.width))