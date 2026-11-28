from .entity import Entity
from world.map import Map
from config import *
import pygame

class Player(Entity):
    def __init__(self, pos0):
        super().__init__(pos0)
        self.velocity = PLAYER_VELOCITY

    def move(self, keys, dt, world):
        direction_x = keys[pygame.K_d] - keys[pygame.K_a]
        direction_y = keys[pygame.K_s] - keys[pygame.K_w]

        position_x = self.position[0] + direction_x * self.velocity * dt
        position_y = self.position[1] + direction_y * self.velocity * dt

        if position_x < world.map.border_left:
            position_x = world.map.border_left
        if position_x > world.map.border_right:
            position_x = world.map.border_right
        if position_y < world.map.border_up:
            position_y = world.map.border_up
        if position_y > world.map.border_down:
            position_y = world.map.border_down

        self.position = (position_x, position_y)
        
    def update(self, dt):
        pass

    def render(self, dt, surface):
        pygame.draw.circle(surface,
                           PLAYER_COLOR,
                           self.position,
                           PLAYER_RADIUS)