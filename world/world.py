from config import *
from .map import Map
from entities.player import Player
import pygame


class World:
    def __init__(self):
        self.map = Map()

    def update(self, dt):
        self.map.update(dt)

    def render(self, dt, surface):
        self.map.render(dt, surface)
        