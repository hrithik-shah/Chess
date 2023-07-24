import pygame
import os

from sound import Sound
from theme import Theme

class Config:

    def __init__(self):
        self.themes = []
        self._add_themes()
        self.idx = 0
        self.theme = self.themes[self.idx]
        self.font = pygame.font.SysFont('monospace', 18, bold=True)
        self.mute = False
        self.move_sound = Sound(
            os.path.join('C:/Users/primu/Desktop/VSC_Programs/Python/Chess/sounds/move.wav'))
        self.capture_sound = Sound(
            os.path.join('C:/Users/primu/Desktop/VSC_Programs/Python/Chess/sounds/capture.wav'))

    def change_theme(self):
        self.idx += 1
        self.idx %= len(self.themes) # resets iteration
        self.theme = self.themes[self.idx]

    def _add_themes(self):
        green = Theme( (238, 238, 210, 255), (118, 150, 86, 255), (246,246,105,255), (186,202,43,255), '#d6d6bd', '#6a874d' )
        glass = Theme('#6a7283', '#2c323f', '#62829c', '#426179', '#5c6474', '#242a36')
        blue = Theme('#eae9d2', '#4b7399', '#75c7e8', '#268ccc', '#d2d1bd', '#436789')
        grey = Theme('#dcdcdc', '#ababab', '#c0cad0', '#a8b2b8', '#c6c6c6', '#9a9a9a')
        orange = Theme('#fce4b2', '#d08b18', '#fdf159', '#e7c50c', '#e2cda0', '#bb7d16')

        self.themes = [green, glass, blue, grey, orange]

