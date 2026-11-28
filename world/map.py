from config import *
import pygame

class Map:
    def __init__(self):
        self.width = SCREEN_WIDTH
        self.height = SCREEN_HEIGHT
        self.border_left = 0
        self.border_right = self.width
        self.border_up = 0
        self.border_down = self.height

    def update(self, dt):
        pass

    def render(self, dt, surface):
        pygame.draw.rect(
            surface,
            MAP_COLOR,
            pygame.Rect(0, 0, SCREEN_WIDTH, SCREEN_HEIGHT))
        # Horizontal lines
        for y in range(GRID_SIZE, SCREEN_HEIGHT, GRID_SIZE):
            pygame.draw.line(surface, LINE_COLOR, (0, y), (SCREEN_WIDTH, y), LINE_WIDTH)
        # Vertical lines
        for x in range(GRID_SIZE, SCREEN_WIDTH, GRID_SIZE):
            pygame.draw.line(surface, LINE_COLOR, (x, 0), (x, SCREEN_HEIGHT), LINE_WIDTH)