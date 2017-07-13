"""This module implements the time bonus for killing a blob"""
from src.level_timer import LevelTimer
import random
import pygame

class TimeBonus():
    """Time reduction for killing a blob"""

    def __init__(self, enemy_rect, text, milliseconds, level_timer, font):
        """save the initial state"""
        self.ms_reduction = milliseconds
        self.enemy_rect = enemy_rect
        self.dy = -4
        self.frame = 0
        self.frame_delay = 2
        self.frames_max = 80
        self.total_frames = 0
        self.font = font
        self.text = text
        self.text_rect = self.font.get_rect(self.text)
        self.text_rect.left = self.enemy_rect.left
        self.text_rect.top = self.enemy_rect.top
        self.color = (255, 0, 0)

        level_timer.elapsed_time_ms = max(0, level_timer.elapsed_time_ms - milliseconds)

    def alive(self):
        """Check if max frames has expired"""
        return self.total_frames < self.frames_max

    def update(self):
        """Move the text"""
        self.frame += 1
        self.total_frames += 1
        if self.frame > self.frame_delay:
            self.frame = 0
            self.text_rect.move_ip(0, self.dy)
            self.color = (random.choice([255, 0]), 0, random.choice([255, 0]))

    def draw(self, screen):
        """Draw the current text"""
        if self.total_frames < self.frames_max and self.text_rect.top >= 0:
            self.font.render_to(screen, (self.text_rect.left, self.text_rect.top), self.text, self.color)
        

