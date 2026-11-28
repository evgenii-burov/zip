from config import *
from world.world import World
from entities.player import Player
import pygame

class Game:
    def __init__(self):
        pygame.init()
        self.screen = pygame.display.set_mode((1280, 720))
        self.clock = pygame.time.Clock()
        self.running = False
        self.world = World()
        self.player = Player(SCREEN_CENTER)

    def run(self):
        self.running = True
        while self.running:
            dt = self.clock.tick(FPS) / 1000
            self.handle_events(dt)
            self.update(dt)
            self.render(dt)
        pygame.quit()

    def handle_events(self, dt):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.running = False
        keys=pygame.key.get_pressed()
        self.player.move(keys, dt, self.world)

    def update(self, dt):
        self.world.update(dt)
        self.player.update(dt)

    def render(self, dt):
        self.world.render(dt, self.screen)
        self.player.render(dt, self.screen)
        pygame.display.flip()


if __name__ == '__main__':
    game = Game()
    game.run()
