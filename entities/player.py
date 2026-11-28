from .entity import Entity
from world.map import Map
from config import *
import math
import pygame

class Player(Entity):
    def __init__(self, pos0):
        super().__init__(pos0)
        self.velocity_x = 0
        self.velocity_y = 0

    def move(self, keys, dt, world):
        direction = pygame.math.Vector2(
            keys[pygame.K_d] - keys[pygame.K_a],
            keys[pygame.K_s] - keys[pygame.K_w],
        )
        if direction.length_squared() > 0:
            direction.normalize_ip()  # so diagonals aren't faster

        target_x = direction.x * PLAYER_MAX_VELOCITY
        target_y = direction.y * PLAYER_MAX_VELOCITY

        blend = min(PLAYER_RESPONSIVENESS * dt, 1)
        self.velocity_x += (target_x - self.velocity_x) * blend
        self.velocity_y += (target_y - self.velocity_y) * blend

        new_x = self.position[0] + self.velocity_x * dt
        new_y = self.position[1] + self.velocity_y * dt

        half = PLAYER_RADIUS

        # left and right
        if new_x - half < world.map.border_left:
            new_x = world.map.border_left + half
            self.velocity_x = 0
        elif new_x + half > world.map.border_right:
            new_x = world.map.border_right - half
            self.velocity_x = 0

        # up and down
        if new_y - half < world.map.border_up:
            new_y = world.map.border_up + half
            self.velocity_y = 0
        elif new_y + half > world.map.border_down:
            new_y = world.map.border_down - half
            self.velocity_y = 0

        self.position = (new_x, new_y)

    def update(self, dt):
        pass

    def render(self, dt, surface):
        pygame.draw.circle(surface,
                           PLAYER_COLOR,
                           self.position,
                           PLAYER_RADIUS)